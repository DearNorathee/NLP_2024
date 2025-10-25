# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 14:13:04 2025

@author: Norat
"""
# worked now
import video_toolkit as vt
import os_toolkit as ost
from typing import Dict, Literal, Union, List
from pathlib import Path
import os

import py_string_tool as pst

#%%
input_video_folder = fr"D:\D_Videos\Netflix Series\3 Body Problem"
output_audio_folder_path = pst.TString(r"C:\C_Video_Python\3 Body Problem\3 Body Problem Season {}\Season {} Subtitle\All_temp")
processing_seasons = [1]

input_video_folders: Dict[int, Union[str,Path]] = {}
output_sub_folders: Dict[int, Union[str,Path]] = {}

    
#%%
folder_names_str = ost.get_folders_name(input_video_folder)
folder_names_str.pop(-1) # exclude S01_Experiment(keep)
avaliable_seasons = pst.get_num(folder_names_str)

folder_paths = ost.get_folders_path(input_video_folder)
folder_paths.pop(-1) # exclude S01_Experiment(keep)
# avaliable_seasons = [7]
# took about 7 min to extract all of seasons

for i, season in enumerate(avaliable_seasons):
    season_str = str(season).zfill(2)
    input_video_folders[season] = folder_paths[i]

for season in range(1,3):
    season_str = str(season).zfill(2)
    output_sub_folders[season] = output_audio_folder_path.fill_values(season_str)
    # new_folder = Path(output_sub_folders[season])
    # new_folder.mkdir(parents=True, exist_ok=True)
    
#%%
for season in processing_seasons:
    try:
        vt.extract_subtitle(filepaths = input_video_folders[season], output_folder = output_sub_folders[season])
        print(f'Done season {season} ✅')
    except:
        print(f"There's an error in season {season} ❌")


    
