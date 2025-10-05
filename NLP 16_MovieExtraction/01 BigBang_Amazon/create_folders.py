# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 10:20:38 2025

@author: Norat
"""
from pathlib import Path
import os

to_create_folders = [
    "English Amazon"
    ,"Spanish (Latin America) Amazon"
    ,"Spanish (Spain) Amazon"
    ,"French Amazon"
    ,"Italian Amazon"
    ,"Turkish Amazon"
    ]


for season in range(1,13):
    season_str = str(season).zfill(2)
    season_folder = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Audio"
    if os.path.exists(season_folder):
        # for new_folder  
        for new_folder in to_create_folders:
            new_folder_path = Path(season_folder, new_folder)
            new_folder_path.mkdir(parents=True,exist_ok=True)
    else:
        raise OSError(f"Path not found. Please double check the path.")

