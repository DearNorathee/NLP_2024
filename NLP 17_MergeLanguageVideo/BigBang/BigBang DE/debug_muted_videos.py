# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 09:44:06 2025

@author: Norat
"""
import os_toolkit as ost
from pprint import pprint
import shutil
from tqdm import tqdm
import video_toolkit as vt
from pathlib import Path
import pandas as pd
import dataframe_short as ds
import subprocess
import os

# season 9 seems to have no audio at all
# https://chatgpt.com/share/688eec89-376c-8001-8424-73d203adadf7

# chatGPT suggested that it could be because of negative timestamp,
# It's likely to be the case because I saw the same warnings when I did merge the video manually(1 video)

media_path:str = r"C:/Users/Norat/OneDrive/D_Code/Python/Python NLP/NLP 02/NLP_2024/NLP 17_MergeLanguageVideo/BigBang/BigBang DE/BigBang PT Season 09_media info.xlsx"

media_info_df_season = pd.read_excel(media_path)


episode_1_media_info = media_info_df_season.loc[media_info_df_season['input_video_name'].isin(["BigBang PT S09E01.mkv"])]

episode_1_media_info.loc[:,'output_folder'] = r"C:\C_Video_Python\Merge Language Video\BigBang Merged\BigBang Season 09\test_02"
# vt.merge_media_to1video(episode_1_media_info,errors="raise")
vt.merge_media_to_video(episode_1_media_info,errors="raise")

##################### Manual loop



season = 8
season_str = str(season).zfill(2)

video_folder_path = fr'C:\C_Video\BigBang Portuguese\BigBang PT Season {season_str}'
# cut-front time
# audio_de_folder_path = fr'C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Subtitle\German Netflix\cut_front_1_sec'
# sub_de_folder_path = fr'C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Audio\German\cut_front_1_sec'

# original time
audio_de_folder_path = fr'C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Audio\German\original'
sub_de_folder_path = fr'C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Subtitle\German Netflix\original_no_speakers'


sub_pt_folder_path = fr'C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Subtitle\Portuguese_ori'
output_folder = fr'C:\C_Video_Python\Merge Language Video\BigBang Merged\BigBang Season {season_str}\test_01'

video_paths = ost.get_full_filename(video_folder_path, extension=['.mkv'])
audio_de_paths = ost.get_full_filename(audio_de_folder_path)
sub_de_paths = ost.get_full_filename(sub_de_folder_path)
sub_pt_paths = ost.get_full_filename(sub_pt_folder_path)

print(len(video_paths))
print(len(audio_de_paths))
print(len(sub_de_paths))
print(len(sub_pt_paths))

ost.delete_files_in_folder(output_folder)

for i in tqdm(range(len(video_paths)),desc = "mergeing video"):

    output_name = os.path.basename(video_paths[i])
    output_path = str(Path(output_folder) / output_name)
    
    ffmpeg_cmd_02 = [
        "ffmpeg",
        # "-fflags", "+genpts",
        "-i", video_paths[i],
        "-i", audio_de_paths[i],
        "-i", sub_de_paths[i],
        "-i", sub_pt_paths[i],
        # Map: video, German audio first, then all PT audios, then German subs
        "-map", "0:v:0",
        "-map", "0:a",  # 0-> refer to input, :a get all of audio from the video(which has input_index 0)
        "-map", "1:a:0",
        "-map", "2:s:0",
        "-map", "3:s:0",

        # Codecs
        "-c:v", "copy",
        "-c:s", "srt",
        "-c:a", "copy",         # copy all audios by default
        # "-c:a:0", "aac",        # re-encode ONLY the German track to fix timestamps
        # "-b:a:0", "192k",

        # Metadata
        "-metadata:s:a:2", "language=deu",
        "-metadata:s:a:2", "title=German_Netflix",
        "-metadata:s:s:0", "language=deu",
        "-metadata:s:s:0", "title=German_Netflix",
        "-metadata:s:s:1", "language=por",
        "-metadata:s:s:1", "title=Portuguese Brazilian",

        # Keep PT as default audio (make German non-default, first PT audio default)
        #  a:0, a:1 needs to be here as well otherwise it would not work
        "-disposition:a:0", "0",
        "-disposition:a:1", "default",
        "-disposition:a:2", "0",

        output_path
    ]


    # test 1 video
    result = subprocess.run(
        ffmpeg_cmd_02,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,  # Redirects stderr to stdout
        text=True,
        check=True
    )
    

############################################## test 1 video

output_name = os.path.basename(video_paths[0])
output_path = str(Path(output_folder) / output_name)

ffmpeg_cmd_02 = [
    "ffmpeg",
    # "-fflags", "+genpts",
    "-i", video_paths[0],
    "-i", audio_de_paths[0],
    "-i", sub_de_paths[0],
    "-i", sub_pt_paths[0],
    # Map: video, German audio first, then all PT audios, then German subs
    "-map", "0:v:0",
    "-map", "0:a",  # 0-> refer to input, :a get all of audio from the video(which has input_index 0)
    "-map", "1:a:0",
    "-map", "2:s:0",
    "-map", "3:s:0",

    # Codecs
    "-c:v", "copy",
    "-c:s", "srt",
    "-c:a", "copy",         # copy all audios by default
    # "-c:a:0", "aac",        # re-encode ONLY the German track to fix timestamps
    # "-b:a:0", "192k",

    # Metadata
    "-metadata:s:a:2", "language=deu",
    "-metadata:s:a:2", "title=German_Netflix",
    "-metadata:s:s:0", "language=deu",
    "-metadata:s:s:0", "title=German_Netflix",
    "-metadata:s:s:1", "language=por",
    "-metadata:s:s:1", "title=Portuguese Brazilian",

    # Keep PT as default audio (make German non-default, first PT audio default)
    #  a:0, a:1 needs to be here as well otherwise it would not work
    "-disposition:a:0", "0",
    "-disposition:a:1", "default",
    "-disposition:a:2", "0",

    output_path
]


# test 1 video
result = subprocess.run(
    ffmpeg_cmd_02,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,  # Redirects stderr to stdout
    text=True,
    check=True
)

############################## manual cmd command
ffmpeg_cmd = [
    "ffmpeg",
    # "-fflags",
    # "+genpts",
    "-i",
    r"C:\C_Video\BigBang Portuguese\BigBang PT Season 09\BigBang PT S09E02.mkv",
    "-i",
    r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 09\Season 09 Subtitle\German Netflix\cut_front_1_sec/BigBang DE S09E02.srt",
    "-i",
    r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 09\Season 09 Audio\German\cut_front_1_sec/BigBang DE S09E02_DE.mp3",
    "-map", "0",
    "-map", "1:s",
    "-map", "2:a",
    "-metadata:s:s:1", "language=deu",
    "-metadata:s:s:1", "title=German_Netflix",
    "-metadata:s:a:2", "language=deu",
    "-metadata:s:a:2", "title=German_Netflix",
    "-c", "copy",
    r"C:\C_Video_Python\Merge Language Video\BigBang Merged\BigBang Season 09\test_02\BigBang PT S09E02.mkv"
]

# for now I'll use this command to generate manually for BigBang season8&9, I'll generalize later
# include_audio_in_from_ori_video = True
# include_sub_in_from_ori_video = False

# -map <input_index>:<stream_type>:<stream_index>
ffmpeg_cmd_02 = [
    "ffmpeg",
    # "-fflags", "+genpts",
    "-i", r"C:\C_Video\BigBang Portuguese\BigBang PT Season 09\BigBang PT S09E02.mkv",
    "-i", r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 09\Season 09 Subtitle\German Netflix\cut_front_1_sec/BigBang DE S09E02.srt",
    "-i", r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 09\Season 09 Audio\German\cut_front_1_sec/BigBang DE S09E02_DE.mp3",
    "-i", r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 08\Season 08 Subtitle\Portuguese_ori\BigBang PT S08E01.srt",
    # Map: video, German audio first, then all PT audios, then German subs
    "-map", "0:v:0",
    "-map", "0:a",  # 0-> refer to input, :a get all of audio from the video(which has input_index 0)
    "-map", "2:a:0",
    "-map", "1:s:0",
    "-map", "3:s:0",

    # Codecs
    "-c:v", "copy",
    "-c:s", "srt",
    "-c:a", "copy",         # copy all audios by default
    # "-c:a:0", "aac",        # re-encode ONLY the German track to fix timestamps
    # "-b:a:0", "192k",

    # Metadata
    "-metadata:s:a:2", "language=deu",
    "-metadata:s:a:2", "title=German_Netflix",
    "-metadata:s:s:0", "language=deu",
    "-metadata:s:s:0", "title=German_Netflix",
    "-metadata:s:s:1", "language=por",
    "-metadata:s:s:1", "title=Portuguese Brazilian",

    # Keep PT as default audio (make German non-default, first PT audio default)
    #  a:0, a:1 needs to be here as well otherwise it would not work
    "-disposition:a:0", "0",
    "-disposition:a:1", "default",
    "-disposition:a:2", "0",

    r"C:\C_Video_Python\Merge Language Video\BigBang Merged\BigBang Season 09\test_02\BigBang PT S09E02_v02.mkv"
]

# include_audio_in_from_ori_video = False
# include_sub_in_from_ori_video = False

ffmpeg_cmd_03 = [
    "ffmpeg",
    # "-fflags", "+genpts+igndts",
    # "-copyts",
    # "-start_at_zero",
    # "-avoid_negative_ts", "make_zero",
    "-i", r"C:\C_Video\BigBang Portuguese\BigBang PT Season 09\BigBang PT S09E02.mkv",
    "-i", r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 09\Season 09 Subtitle\German Netflix\cut_front_1_sec/BigBang DE S09E02.srt",
    "-i", r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 09\Season 09 Audio\German\cut_front_1_sec/BigBang DE S09E02_DE.mp3",
    "-map", "0:v:0",
    "-map", "1:s:0",
    "-map", "2:a:0",
    "-c:v", "copy",
    "-c:s", "srt",
    "-c:a", "copy",
    "-disposition:a:0", "default",
    "-metadata:s:a:0", "language=deu",
    "-metadata:s:a:0", "title=German_Netflix",
    "-metadata:s:s:0", "language=deu",
    "-metadata:s:s:0", "title=German_Netflix",
    r"C:\C_Video_Python\Merge Language Video\BigBang Merged\BigBang Season 09\test_02\BigBang PT S09E02_v03.mkv"
]

result = subprocess.run(
    ffmpeg_cmd_02,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,  # Redirects stderr to stdout
    text=True,
    check=True
)

