# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 10:10:57 2025

@author: Norat
"""

# not successfull with stable_whisper yet
import video_toolkit as vt
import os
import stable_whisper
import whisper
import torch
from playsound import playsound
import modeling_tool as mlt
import os_toolkit as ost
from pathlib import Path
import shutil
# env: stable_whisper_2.19.0

# openai-whisper=20240930
# stable-ts=2.19.0
# faster-whisper=1.1.1

# get and store the German episode name

root_video_input_path = r'D:\D_Videos\Series\The 100_DE\S01'
file_name = ost.get_filename(root_video_input_path,extension=vt.VIDEO_ALL_EXTENSIONS)

############################################# rename to standardized name
video_input_dict: dict[int,str] = {}

out_root_audio_path_dict: dict[int,str] = {}
out_root_sub_path_dict: dict[int,str] = {}

out_audio_path_dict: dict[int,str] = {}
out_sub_path_dict: dict[int,str] = {}

for season in range(1,8):
    season_str = str(season).zfill(2)
    video_input_path = fr'D:\D_Videos\Series\The 100_DE\S{season_str}'
    video_input_dict[season] = video_input_path

for season, video_input_path in video_input_dict.items():
    ost.auto_rename_series(folder_path = video_input_path, prefix = "The 100", suffix="_DE")

for season in range(1,8):
    season_str = str(season).zfill(2)
    root_audio_path = Path(fr'C:\C_Video_Python\The 100\The 100 Season {season_str}\Season {season_str} Audio')
    root_sub_path = Path(fr'C:\C_Video_Python\The 100\The 100 Season {season_str}\Season {season_str} Subtitle')
    out_root_audio_path_dict[season] = root_audio_path
    out_root_sub_path_dict[season] = root_sub_path


######## create German folder
for season, _ in out_root_audio_path_dict.items():
    out_german_audio_path = out_root_audio_path_dict[season] / "German"
    out_german_sub_path = out_root_sub_path_dict[season]  / "German Amazon Auto"
    
    out_audio_path_dict[season] = out_german_audio_path
    out_sub_path_dict[season] = out_german_sub_path
    
    
    # remove folders that I created incorrectly prior
    wrong_path_01 = out_root_audio_path_dict[season]  / "German Amazon Auto"
    wrong_path_02 = out_root_sub_path_dict[season]  / "German"
    if wrong_path_01.exists() and wrong_path_01.is_dir():
        shutil.rmtree(out_root_audio_path_dict[season]  / "German Amazon Auto")
        
    if wrong_path_02.exists() and wrong_path_02.is_dir():   
        shutil.rmtree(out_root_sub_path_dict[season]  / "German")
    out_german_audio_path.mkdir(parents=True,exist_ok=True)
    out_german_sub_path.mkdir(parents=True,exist_ok=True)

for season, _ in out_root_audio_path_dict.items():
    out_german_audio_path = out_root_audio_path_dict[season] / "German"
    out_german_sub_path = out_root_sub_path_dict[season]  / "German Amazon Auto"
    
    out_audio_path_dict[season] = out_german_audio_path
    out_sub_path_dict[season] = out_german_sub_path
    
# took about 13 min for season 1
################## extract audio
# for season, _ in video_input_dict.items():
#     print(f'extract subtitle season {season}. Done :> ')
#     vt.extract_audio(filepaths = video_input_dict[season], output_folder = out_audio_path_dict[season])

# vt.extract_audio(filepaths = video_input_dict[1], output_folder = out_audio_path_dict[1])

for season, _ in video_input_dict.items():
    vt.extract_subtitle(filepaths = video_input_dict[season], output_folder = out_sub_path_dict[season])
    print(f'extract subtitle season {season}. Done :> ')
vt.extract_subtitle(filepaths = video_input_dict[2], output_folder = out_sub_path_dict[2])
print('Extract subtitle all season done:>')


sub_path01 = r"D:\D_Videos\Series\The 100_DE\S03\The 100 S03E03_DE.srt"
sub_df_01 = vt.sub_to_df(sub_path01)

sub_path02 = r"D:\D_Videos\Series\The 100_DE\The_100 - season 3.en\The 100 - 3x03 - Ye Who Enter Here.720p HDTV.AVS.en.srt"
sub_df_02 = vt.sub_to_df(sub_path02)



