# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 14:13:04 2025

@author: Norat
"""
#%%

# NEXT: 1) set up working folder
# 2) Clean up videos's name file(Don't forget to store German's episode name)
import video_toolkit as vt
import os_toolkit as ost
from typing import Dict, Literal, Union, List
from pathlib import Path
import os
from play_audio_file import play_alarm_done, play_alarm_error
import py_string_tool as pst
import pandas as pd

#%%
# create working folder
subtitle_folders = [
    'Japanese',
    "German",
    "English",
]

audio_folders =  [
    'Japanese',
    "German",
    "English"
    ]


vt.create_series_working_folder(
    series_name = "Yu-Gi-Oh_GX"
    , create_structure_at = r"C:\C_Video_Python"
    , audio_folders = audio_folders
    , subtitle_folders = subtitle_folders
    , end_seasons = 4)

#%%
 # extract episodes name before renaming
# episode_names = pd.DataFrame(ost.get_filename(r"D:\D_Videos\Japanese Anime\Yu-Gi-Oh_GX_DE\S03")) 

#%%
# clean up file name
ost.auto_rename_series(
    folder_path = r"D:\D_Videos\Japanese Anime\Yu-Gi-Oh_GX_DE\S03", 
    prefix = "Yu-Gi-Oh_GX")

#%%
input_video_folders: Dict[int, Union[str,Path]] = {}
output_audio_folders: Dict[int, Union[str,Path]] = {}
# !CHANGE
input_video_folder = fr"D:\D_Videos\Japanese Anime\Yu-Gi-Oh_GX_DE"
output_audio_template_path = r"C:\C_Video_Python\Yu-Gi-Oh_GX\Yu-Gi-Oh_GX Season {season_str}\Season {season_str} Audio\German"


# create Amazon_temp folder for all season
for season in range(1,5):
    season_str = str(season).zfill(2)
    # !CHANGE
    output_audio_folders[season] = output_audio_template_path.replace("{season_str}", season_str)
    # new_folder = Path(output_audio_folders[season])
    # new_folder.mkdir(parents=True, exist_ok=True)
    
#%%


folder_names_str = ost.get_folders_name(input_video_folder)
avaliable_seasons = pst.get_num(folder_names_str)

folder_paths = ost.get_folders_path(input_video_folder)

# took about 25 sec per video
# about 20 min for 1 season
for i, season in enumerate(avaliable_seasons):
    season_str = str(season).zfill(2)
    input_video_folders[season] = folder_paths[i]


#%%
# !CHANGE
for season in [2,3]:
    try:
        vt.extract_audio(filepaths = input_video_folders[season], output_folder = output_audio_folders[season])
        print(f'\nDone season {season} ✅')
        play_alarm_done()
    except:
        print(f"\nThere's an error in season {season} ❌")
        play_alarm_error()
    
    
