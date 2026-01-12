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
input_video_folders: Dict[int, Union[str,Path]] = {}
output_audio_folders: Dict[int, Union[str,Path]] = {}
input_video_folder = fr"D:\D_Videos\Series\The 100\The 100_FR"

# create Amazon_temp folder for all season
for season in range(1,8):
    season_str = str(season).zfill(2)
    output_audio_folders[season] = fr"C:\C_Video_Python\The 100\The 100 Season {season_str}\Season {season_str} Audio\French"
    # output_audio_folders[season] = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Audio\Amazon_temp"
    # new_folder = Path(output_audio_folders[season])
    # new_folder.mkdir(parents=True, exist_ok=True)
    
#%%


folder_names_str = ost.get_folders_name(input_video_folder)
avaliable_seasons = pst.get_num(folder_names_str)

folder_paths = ost.get_folders_path(input_video_folder)

# took about 20 min to extract season 1(13 episodes)(both FR and EN)
for i, season in enumerate(avaliable_seasons):
    season_str = str(season).zfill(2)
    input_video_folders[season] = folder_paths[i]

#%%
for season in range(2,8):
    try:
        vt.extract_audio(filepaths = input_video_folders[season], output_folder = output_audio_folders[season])
        print(f'\nDone season {season} ✅')
        play_alarm_done()
    except:
        print(f"\nThere's an error in season {season} ❌")
        play_alarm_error()


#%%
# S01 | 13 videos | 18:15 min
# S02 | 16 videos | 22:42 min
# S03 | 16 videos | 22:06 min
# S04 | 13 videos | 18:04 min
# S05 | 13 videos | 17:48 min
# S06 | 13 videos | 17:17 min
# S07 | 16 videos | 21:18 min | 1.33 min / video

    
    
    

