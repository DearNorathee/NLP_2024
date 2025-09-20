# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 09:39:38 2025

@author: Norat
"""

import os_toolkit as ost
import py_string_tool as pst
from typing import Dict, Literal, Union, List
from pathlib import Path



input_video_folder = fr"C:\DVDFab\StreamFab\Output\Netflix\The Big Bang Theory"
folder_names_str = ost.get_folders_name(input_video_folder)
avaliable_seasons = pst.get_num(folder_names_str)
folder_paths = ost.get_folders_path(input_video_folder)

input_video_folders: Dict[int, Union[str,Path]] = {}

test_path01 = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 01\Season 01 Audio\Italian\original"

for i, season in enumerate(avaliable_seasons):
    season_str = str(season).zfill(2)
    input_video_folders[season] = folder_paths[i]

    ost.auto_rename_series(folder_path = folder_paths[i] ,prefix = "BigBang IT")
    

test_path01 = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Audio\Italian\original"
ost.auto_rename_series(folder_path = test_path01 ,prefix = "BigBang IT")
