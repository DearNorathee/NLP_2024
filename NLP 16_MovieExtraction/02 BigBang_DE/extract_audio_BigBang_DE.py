# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 09:51:16 2024

@author: Heng2020
"""
# objective of this script is to extract audio from video in BigBang for all seasons

#  change the structure of this script so that it would be very easy to run and change when there's a new langauge, or new series
#  should take less than 10 min to change, currently it's still confusing and took more than 30 min


# what if audio has multiple langauges?

# speed performance, it took about 10 min to extract German audio for bigbang 1 season(.mp3)
import video_toolkit as vt
import os_toolkit as ost
from typing import Dict, Literal, Union, List
from pathlib import Path
import os
import shutil
import py_string_tool as pst

from play_audio_file import play_alarm_done, play_alarm_error

# play_alarm_done()
input_video_folders: Dict[int, Union[str,Path]] = {}
output_audio_folders: Dict[int, Union[str,Path]] = {}

output_audio_folders: dict[int, Union[str,Path]] = {}

LANGUAGE:str = "German"
skip_season = []
# assuming all season have the same folder structure:
    
# C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 01\Season 01 Audio\German

input_video_folder = fr"C:\DVDFab\StreamFab\Output\Netflix\The Big Bang Theory"

folder_names_str = ost.get_folders_name(input_video_folder)
avaliable_seasons = pst.get_num(folder_names_str)

fodder_paths = ost.get_folders_path(input_video_folder)

for i, season in enumerate(avaliable_seasons):
    season_str = str(season).zfill(2)
    input_video_folders[season] = fodder_paths[i]
    output_audio_folders[season] = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Audio\{LANGUAGE}"



for season, audio_output_folder in output_audio_folders.items():
    # french_folder = Path(audio_output_folder) / "French"
    # english_folder = Path(audio_output_folder) / "English"
    # language_folder = Path(audio_output_folder) / LANGUAGE
    # if season not in skip_season:
    #     if os.path.exists(audio_output_folder):
    #         vt.extract_audio(input_video_folders[season], audio_output_folder, languages=LANGUAGE)
    #         print(f"Done season: {season}✅")

    #     else:
    #         print(f"{audio_output_folder} does not exist.❌")
    
    if season not in skip_season:
        if os.path.exists(audio_output_folder):
            if not os.path.exists(output_audio_folders[season]):
                os.makedirs(output_audio_folders[season], exist_ok=True)
                
            vt.extract_audio(
                video_folder=input_video_folders[season],
                output_folder=output_audio_folders[season],
                languages= LANGUAGE
                )
                
            print(f"Done season: {season}✅")
        else:
            print(f"{audio_output_folder} does not exist. ❌")

# vt.extract_audio(video_folder=input_video_folders[1], output_folder = output_audio_folders[1],languages="German")

