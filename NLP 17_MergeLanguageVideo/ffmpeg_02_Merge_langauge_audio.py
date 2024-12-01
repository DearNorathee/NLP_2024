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
output_name = "BigBang All S06E01_v03.mkv"


video_folder = Path(r"H:\D_Video_Python\Merge Language Video\tests\inputs")
audio_folder = Path(r"H:\D_Video_Python\Merge Language Video\tests\inputs")
output_folder = Path(r"H:\D_Video_Python\Merge Language Video\tests\outputs")

video_path = video_folder / video_name
audio_path = audio_folder / audio_name
output_path = output_folder / output_name


command = [
    # worked Now yeahhh.... (a:2)
    'ffmpeg',
    '-i', str(video_path),
    '-i', str(audio_path),
    '-map', '0',
    '-map', '1:a',
    '-metadata:s:a:2', 'language=fre',
    '-metadata:s:a:2', 'title=French',
    '-c', 'copy',
    str(output_path)
]


command07 = [
# test multiple audio
    # worked Now yeahhh.... (a:2)
    'ffmpeg',
    '-i', str(video_path),
    '-i', str(audio_path),
    '-i', str(audio_path),
    '-i', str(audio_path),
    '-map', '0',
    '-map', '1:a',
    '-map', '2:a',
    '-map', '3:a',
    
    '-metadata:s:a:2', 'language=fre',
    '-metadata:s:a:2', 'title=French',
    
    '-metadata:s:a:3', 'language=spa',
    '-metadata:s:a:3', 'title=Spanish',
    '-metadata:s:a:4', 'language=ger',
    '-metadata:s:a:4', 'title=German',
    
    '-c', 'copy',
    str(output_path)
]


command02 = [
    'ffmpeg',
    '-i', str(video_path),
    '-itsoffset', '10',
    '-i', str(audio_path),
    '-c:a', 'copy',
    '-c:v', 'copy',
    # '-metadata:s:a:3', 'language=fre',
    '-map', '0:a:0',
    '-map', '1:v:0',
    str(output_path)
]

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




vt.merge_audio_to_video(
    input_video_path = video_path, 
    input_audio_path = audio_path, 
    audio_language_code_3alpha = "fre", 
    audio_title = "French02", 
    output_folder = output_folder, 
    output_name = output_name)

vt.merge_audio_to_video(
    input_video_path = video_path, 
    input_audio_path = [audio_path,audio_path,audio_path], 
    audio_language_code_3alpha = ["fre","spa","ger"], 
    audio_title = ["French02","Spanish","German"], 
    output_folder = output_folder, 
    output_name = output_name)

path01 = r"C:\Users\Heng2020\OneDrive\Python NLP\NLP 06_ffmpeg\BigBang All S06E01.mkv" 
metadata01 = get_metadata(path01)

metadata01 = get_metadata(video_path)
