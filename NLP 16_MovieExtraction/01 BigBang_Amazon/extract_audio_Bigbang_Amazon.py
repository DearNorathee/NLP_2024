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
input_video_folders: Dict[int, Union[str,Path]] = {}
output_audio_folders: Dict[int, Union[str,Path]] = {}

# create Amazon_temp folder for all season
for season in range(1,13):
    season_str = str(season).zfill(2)
    output_audio_folders[season] = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Audio\Amazon_temp"
    new_folder = Path(output_audio_folders[season])
    new_folder.mkdir(parents=True, exist_ok=True)
    
#%%
input_video_folder = fr"C:\C_Video\The Big Bang Theory"

folder_names_str = ost.get_folders_name(input_video_folder)
avaliable_seasons = pst.get_num(folder_names_str)

folder_paths = ost.get_folders_path(input_video_folder)

# took about 3 min per video
# about 1 hr per season
for i, season in enumerate(avaliable_seasons):
    season_str = str(season).zfill(2)
    input_video_folders[season] = folder_paths[i]

#%%
for season in range(10,13):
    try:
        vt.extract_audio(filepaths = input_video_folders[season], output_folder = output_audio_folders[season])
        print(f'\nDone season {season} ✅')
        play_alarm_done()
    except:
        print(f"\nThere's an error in season {season} ❌")
        play_alarm_error()
    
    
