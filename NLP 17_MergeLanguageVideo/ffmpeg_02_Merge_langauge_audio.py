# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:53:30 2023

@author: Heng2020
"""

from pathlib import Path
from langcodes import Language
import langcodes
import pycountry
import video_toolkit as vt
from typing import Union, List
import subprocess
# NEXT: merge_media_to_video(work with both sub and audio as input)(NOT STARTED)
# merge

# https://www.geekyhacker.com/synchronize-audio-and-video-with-ffmpeg/

# quick impact analysis
# for S06E01
# FR filesize = 917 MB
# PR filesize = 586 MB
# (total 1503)

# reduce mem by 23%
# merged filesize = 616 MB


video_name = "BigBang PT S06E01.mkv"
audio_name = "BigBang FR S06E01_FR.mp3"
output_name = "BigBang All S06E01_v06.mkv"


video_folder = Path(r"C:\C_Video_Python\Merge Language Video\tests\inputs")
audio_folder = Path(r"C:\C_Video_Python\Merge Language Video\tests\inputs")
output_folder = Path(r"C:\C_Video_Python\Merge Language Video\tests\outputs")

video_path = video_folder / video_name
audio_path = audio_folder / audio_name
output_path = output_folder / output_name

sub_path1 = r"C:\C_Video_Python\Merge Language Video\tests\inputs\BigBang PT S03E01.srt"
sub_path2 = r"C:\C_Video_Python\Merge Language Video\tests\inputs\BigBang PT S03E02.srt"
sub_path3 = r"C:\C_Video_Python\Merge Language Video\tests\inputs\BigBang PT S03E03.srt"
sub_path4 = r"C:\C_Video_Python\Merge Language Video\tests\inputs\BigBang PT S03E04.srt"

command = [
    # worked Now yeahhh.... (a:2)
    'ffmpeg',
    '-i', str(video_path),
    '-i', str(audio_path),
    '-map', '0',
    '-map', '1:a',
    '-metadata:s:a:2', 'language=por',
    '-metadata:s:a:2', 'title=EP1',
    '-c', 'copy',
    str(output_path)
]


command07 = [
# test multiple audio
    # worked Now yeahhh.... (a:2)
    'ffmpeg',
    '-i', str(video_path),
    '-i', str(sub_path1),

    '-map', '0',
    '-map', '1:s',
    
    '-metadata:s:s:1', 'language=por',
    '-metadata:s:s:1', 'title=EP1',

    '-c', 'copy',
    str(output_path)
]

command02 = [
# test multiple subtitle
    # worked Now yeahhh.... (a:2)
    'ffmpeg',
    '-i', str(r"C:\C_Video_Python\Merge Language Video\tests\outputs\BigBang All S06E01_v04.mkv"),
    '-i', str(sub_path2),

    '-map', '0',
    '-map', '1:s',
    
    '-metadata:s:s:2', 'language=fre',
    '-metadata:s:s:2', 'title=EP2',

    '-c', 'copy',
    str(r"C:\C_Video_Python\Merge Language Video\tests\outputs\BigBang All S06E01_v05.mkv")
]

vt.get_all_metadata(r"C:\C_Video_Python\Merge Language Video\tests\inputs\BigBang All S06E01_already_have_sub.mkv")
vt.get_subtitle_index(r"C:\C_Video_Python\Merge Language Video\tests\inputs\BigBang All S06E01_already_have_sub.mkv")
vt.get_subtitle_extension()

command03 = [
    'ffmpeg',
    '-i', str(video_path),               # First input: video file
    '-i', str(audio_path),               # Second input: audio file
    '-filter_complex', '[1:a]atrim=start=3[audio]',  # Trim first 3 seconds from audio
    '-map', '0:v',                       # Map video stream from the first input
    '-map', '[audio]',                   # Map the trimmed audio stream
    '-metadata:s:a:0', 'language=fre',  # Set the language of the audio stream
    '-metadata:s:a:0', 'title=French',  # Set the title of the audio stream
    '-c:v', 'copy',                      # Copy video codec
    '-c:a', 'aac',                       # Transcode audio to maintain sync after trimming
    str(output_path)
]

command04 = [

    'ffmpeg',
    '-i', str(video_path),
    # you can change the sign from positive or negative
    # positive means you delay the audio
    # negative means you faster the audio played
    '-itsoffset', '-00:00:02.00',
    '-i', str(audio_path),
    '-filter:a', 'atempo=1.03361',
    '-map', '0',
    '-map', '1:a',
    '-metadata:s:a:2', 'language=fre',
    '-metadata:s:a:2', 'title=French',
    '-c', 'copy',
    str(output_path)
]

command05 = [

    'ffmpeg',
    '-i', str(video_name),
    # you can change the sign from positive or negative
    # positive means you delay the audio
    # negative means you faster the audio played
    '-itsoffset', '-3',
    '-i', str(audio_name),
    '-map', '0',
    '-map', '1:a',
    '-metadata:s:a:2', 'language=fre',
    '-metadata:s:a:2', 'title=French',
    '-c', 'copy',
    str(output_name)
]

command06 = [
    # worked Now yeahhh.... (a:2)
    'ffmpeg',
    '-i', str(video_name),
    '-i', str(audio_name),
    '-map', '0',
    '-map', '1:a',
    '-metadata:s:a:2', 'language=fre',
    '-metadata:s:a:2', 'title=French',
    '-c', 'copy',
    str(output_name)
]

cmd_line = ' '.join(command)
cmd_line

result = subprocess.run(command, text=True, stderr=subprocess.PIPE)

result = subprocess.run(command07, text=True, stderr=subprocess.PIPE)

result02 = subprocess.run(command02, text=True, stderr=subprocess.PIPE)
result03 = subprocess.run(command03, text=True, stderr=subprocess.PIPE)
result04 = subprocess.run(command04, text=True, stderr=subprocess.PIPE)

select_result = result

if select_result.returncode != 0:
    print("Error encountered:")
    print(result.stderr)



# vt.merge_audio_to_video(
#     input_video_path = video_path, 
#     input_audio_path = audio_path, 
#     audio_language_code_3alpha = "fre", 
#     audio_title = "French02", 
#     output_folder = output_folder, 
#     output_name = output_name)

# vt.merge_audio_to_video(
#     input_video_path = video_path, 
#     input_audio_path = [audio_path,audio_path,audio_path], 
#     audio_language_code_3alpha = ["fre","spa","ger"], 
#     audio_title = ["French02","Spanish","German"], 
#     output_folder = output_folder, 
#     output_name = output_name)

vt.merge_sub_to_video(
    input_video_path = video_path, 
    input_subtitle_path = [sub_path1]
    , subtitle_lang_code_3alpha = "fre"
    , subtitle_title = "EP1"
    , output_folder = output_folder
    , output_name = output_name
    ,replace=True
    )

vt.merge_sub_to_video(
    input_video_path = video_path, 
    input_subtitle_path = [sub_path1,sub_path2,sub_path3,sub_path4]
    , subtitle_lang_code_3alpha = ["fre","spa","ger","fre"]
    , subtitle_title = ["EP1","EP2","EP3","EP4"]
    , output_folder = output_folder
    , output_name = output_name)



