# -*- coding: utf-8 -*-
"""
Created on Sat Aug  2 10:42:33 2025

@author: Norat
"""

import shutil
from pathlib import Path
from tqdm import tqdm


seasons = [i for i in range(1,13)]

for season in tqdm(seasons):
    season_str = str(season).zfill(2)
    # Source folder you want to copy
    src = Path(fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Audio\German\cut_front_1_sec")
    # Destination parent folder
    dst_parent = Path(fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Audio\German")

    # New folder name
    dst = dst_parent / "final_selection"
    # Copy the entire directory tree and rename it in the process
    try:
        shutil.copytree(src, dst)
    except FileExistsError:
        print(f'folder already exist, skip for season {season}⚠️')


seasons = [i for i in range(1,13)]

for season in tqdm(seasons):
    season_str = str(season).zfill(2)
    # Source folder you want to copy
    src = Path(fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Subtitle\German Netflix\cut_front_1_sec")
    # Destination parent folder
    dst_parent = Path(fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Subtitle\German Netflix")

    # New folder name
    dst = dst_parent / "final_selection"
    # Copy the entire directory tree and rename it in the process
    try:
        shutil.copytree(src, dst)
    except FileExistsError:
        print(f'folder already exist, skip for season {season}⚠️')
