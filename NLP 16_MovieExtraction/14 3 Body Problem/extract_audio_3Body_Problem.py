# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 14:13:04 2025

@author: Norat
"""
#%%
import video_toolkit as vt
import os_toolkit as ost
from typing import Dict, Literal, Union, List
from pathlib import Path
import os
from play_audio_file import play_alarm_done, play_alarm_error
import py_string_tool as pst


#%%
# rename video files
# for season in range(1,13):
#     season_str = str(season).zfill(2)
#     video_path_01 = fr'C:\DVDFab\StreamFab\Output\Amazon\The Big Bang Theory\S{season_str}'
#     ost.auto_rename_series(folder_path = video_path_01, prefix = "The Big Bang Theory_")
#%%
input_video_folder = fr"D:\D_Videos\Netflix Series\3 Body Problem"
output_audio_folder_path = pst.TString(r"C:\C_Video_Python\3 Body Problem\3 Body Problem Season {}\Season {} Audio\All_temp")
processing_seasons = [1]

input_video_folders: Dict[int, Union[str,Path]] = {}
output_audio_folders: Dict[int, Union[str,Path]] = {}

# create Amazon_temp folder for all season

    # new_folder = Path(output_audio_folders[season])
    # new_folder.mkdir(parents=True, exist_ok=True)
    
#%%


folder_names_str = ost.get_folders_name(input_video_folder)
folder_names_str.pop(-1) # exclude S01_Experiment(keep)
avaliable_seasons = pst.get_num(folder_names_str)

folder_paths = ost.get_folders_path(input_video_folder)
folder_paths.pop(-1) # exclude S01_Experiment(keep)

# took about 15 min per episode(mp3)
for i, season in enumerate(avaliable_seasons):
    season_str = str(season).zfill(2)
    input_video_folders[season] = folder_paths[i]

for season in avaliable_seasons:
    season_str = str(season).zfill(2)
    
    output_audio_folders[season] = output_audio_folder_path.fill_values(season_str)

#%%
for season in processing_seasons:
    try:
        vt.extract_audio(filepaths = input_video_folders[season], output_folder = output_audio_folders[season])
        print(f'\nDone season {season} ✅')
        play_alarm_done()
    except:
        print(f"\nThere's an error in season {season} ❌")
        play_alarm_error()
    
    
