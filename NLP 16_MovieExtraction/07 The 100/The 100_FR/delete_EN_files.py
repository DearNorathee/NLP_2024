# -*- coding: utf-8 -*-
"""
Created on Sun Nov  9 09:54:39 2025

@author: Norat
"""

import os_toolkit as ost
from send2trash import send2trash
from pathlib import Path
from typing import Callable


root_folder_02 = r'C:\C_Video_Python\The 100\The 100 Season 01\Season 01 Audio'
path_lists_02 = ost.get_full_filename(root_folder_02)



root_folder = r"C:\C_Video_Python\The 100\The 100 Season 01\Season 01 Audio\French"
path_lists = ost.get_full_filename(root_folder,)



def validate_files(path: Path) -> bool:
    suffix = path.stem[-2:]
    return suffix in ['EN']

ost.apply_func_to_files(
    root_folder=r"C:\\C_Video_Python\\The 100\\The 100 Season 01\\Season 01 Audio\\French",
    validate_files=validate_files,
    apply_func=send2trash)

for i in range(1,8):
    season_str = str(i).zfill(2)
    ost.apply_func_to_files(
        root_folder=f"C:\\C_Video_Python\\The 100\\The 100 Season {season_str}\\Season {season_str} Audio\\French",
        validate_files=validate_files,
        apply_func=send2trash)
print("Done✅")
    

