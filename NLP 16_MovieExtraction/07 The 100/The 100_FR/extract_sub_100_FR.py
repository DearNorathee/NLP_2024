# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 14:13:04 2025

@author: Norat
"""

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

input_video_folders: Dict[int, Union[str,Path]] = {}
output_sub_folders: Dict[int, Union[str,Path]] = {}
input_video_folder = fr"D:\D_Videos\Series\The 100\The 100_FR"

# create Amazon_temp folder for all season
for season in range(1,8):
    season_str = str(season).zfill(2)
    output_sub_folders[season] = fr"C:\C_Video_Python\The 100\The 100 Season {season_str}\Season {season_str} Subtitle\French_HBO"
    new_folder = Path(output_sub_folders[season])
    new_folder.mkdir(parents=True, exist_ok=True)
    
    
folder_names_str = ost.get_folders_name(input_video_folder)
avaliable_seasons = pst.get_num(folder_names_str)

folder_paths = ost.get_folders_path(input_video_folder)

# took about 7 min to extract all of seasons
for i, season in enumerate(avaliable_seasons):
    season_str = str(season).zfill(2)
    input_video_folders[season] = folder_paths[i]


for season in range(1,8):
    try:
        vt.extract_subtitle(filepaths = input_video_folders[season], output_folder = output_sub_folders[season])
        print(f'Done season {season} ✅')
    except:
        print(f"There's an error in season {season} ❌")
    
    
