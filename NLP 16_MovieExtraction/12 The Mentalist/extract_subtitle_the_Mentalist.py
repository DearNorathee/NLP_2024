# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 14:13:04 2025

@author: Norat
"""
# the scripts works now(tested)
import video_toolkit as vt
import os_toolkit as ost
from typing import Dict, Literal, Union, List
from pathlib import Path
import os

import py_string_tool as pst

# rename video files
# for season in range(1,13):
#     season_str = str(season).zfill(2)
#     video_path_01 = fr'C:\DVDFab\StreamFab\Output\Amazon\The Big Bang Theory\S{season_str}'
#     ost.auto_rename_series(folder_path = video_path_01, prefix = "The Big Bang Theory_")

#%%
# create working folder
subtitle_folders = [
    'Amazon_temp',
    "Korean",
    "Chinese_Traditional",
    "Arabic",
    "Hebrew",
    "Russian",
    "Greek",
    "Czech",
    "Turkish",
    "Swedish",
    "Finnish",
    "Romanian",
    "Portuguese_EU",
    "Portuguese_Brazil",
    "Polish",
    "Norwegian",
    "Dutch",
    "Hungarian",
    "Italian",
    "French",
    "Spanish_Latin America",
    "Spanish_Spain",
    "German",
    "Danish",
    "English",
]

audio_folders =  [
    'Amazon_temp',
    "German",
    "English",
    "Spanish (Latin America)",
    "Spanish (Spain)",
    "French",
    "Italian",
    "Japanese",
    "Portuguese_Brazil"]


vt.create_series_working_folder(
    series_name = "The Mentalist"
    , create_structure_at = r"C:\C_Video_Python"
    , audio_folders = audio_folders
    , subtitle_folders = subtitle_folders
    , end_seasons = 7)


#%%
# clean up file name
ost.auto_rename_series(
    folder_path = r"D:\D_Videos\Series\The Mentalist\S01", 
    prefix = "The Mentalist_")
#%%
input_video_folders: Dict[int, Union[str,Path]] = {}
output_sub_folders: Dict[int, Union[str,Path]] = {}

selected_seasons = [1,6,7]

# create Amazon_temp folder for all season
for season in range(1,8):
    season_str = str(season).zfill(2)
    output_sub_folders[season] = fr"C:\C_Video_Python\The Mentalist\The Mentalist Season {season_str}\Season {season_str} Subtitle\Amazon_temp"
    # new_folder = Path(output_sub_folders[season])
    # new_folder.mkdir(parents=True, exist_ok=True)
    
input_video_folder = fr"D:\D_Videos\Series\The Mentalist"

folder_names_str = ost.get_folders_name(input_video_folder)
avaliable_seasons = pst.get_num(folder_names_str)
# avaliable_seasons = [6,7]

# folder_path should be dict to
folder_paths = ost.get_folders_path(input_video_folder)


for i, season in enumerate(avaliable_seasons):
    print(f'Done season {season} ')
    
    
    
# took about 40 sec per video
#  so about 20 min per season
for i, season in enumerate(avaliable_seasons):
    # season_str = str(season).zfill(2)
    input_video_folders[season] = folder_paths[i]


for season in [6,7]:
    try:
        vt.extract_subtitle(filepaths = input_video_folders[season], output_folder = output_sub_folders[season])
        print(f'Done season {season} ✅')
    except:
        print(f"There's an error in season {season} ❌")
    
    
