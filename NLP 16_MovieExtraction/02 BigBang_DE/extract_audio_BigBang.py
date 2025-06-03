# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 09:51:16 2024

@author: Heng2020
"""
# objective of this script is to extract audio from video in BigBang for all seasons

#  change the structure of this script so that it would be very easy to run and change when there's a new langauge, or new series
#  should take less than 10 min to change, currently it's still confusing and took more than 30 min


# what if audio has multiple langauges?

import video_toolkit as vt
import os_toolkit as ost
from typing import Dict, Literal, Union, List
from pathlib import Path
import os
import shutil

input_video_folders: Dict[int, Union[str,Path]] = {}
output_audio_folders: Dict[int, Union[str,Path]] = {}

output_audio_folders: dict[int, Union[str,Path]] = {}

LANGUAGE:str = "German"
skip_season = [7,8,9,10,11]
# assuming all season have the same folder structure:
    
# C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 01\Season 01 Audio\German


for season in range(1,12):
    season_str = str(season).zfill(2)
    input_video_folders[season] = fr"C:\DVDFab\StreamFab\Output\Netflix\The Big Bang Theory\S{season_str}"
    output_audio_folders[season] = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Audio\{LANGUAGE}"



for season, audio_output_folder in output_audio_folders.items():
    # french_folder = Path(audio_output_folder) / "French"
    # english_folder = Path(audio_output_folder) / "English"
    language_folder = Path(audio_output_folder) / LANGUAGE
    if season not in skip_season:
        if os.path.exists(audio_output_folder):
            vt.extract_audio(input_video_folders[season], audio_output_folder, languages=LANGUAGE)
            print(f"Done season: {season}✅")

        else:
            print(f"{audio_output_folder} does not exist.❌")
    
    if season not in skip_season:
        if os.path.exists(audio_output_folder):
            if not os.path.exists(language_folder):
                os.makedirs(language_folder, exist_ok=True)
                vt.extract_audio(
                    video_folder=input_video_folders[season],
                    output_folder=language_folder,
                    languages= ["French"]
                    )
                print(f"Done season: {season}✅")
        else:
            print(f"{audio_output_folder} does not exist. ❌")

