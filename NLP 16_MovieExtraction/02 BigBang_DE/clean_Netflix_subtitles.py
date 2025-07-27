# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 11:32:38 2025

@author: Norat
"""

import video_toolkit as vt
from pathlib import Path
from beartype import beartype
from typing import Union, Literal
import os
import os_toolkit as ost

def create_cleaned_sub_BigBang():
    from tqdm import tqdm
    seasons = [i for i in range(1,13)]
    error_count = 0
    for season in tqdm(seasons, desc="processing...",colour='blue'):
        try:
            season_str = str(season).zfill(2)
            sub_original_folder = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Subtitle\German Netflix\original"
            # ost.delete_files_in_folder(sub_original_folder)
            ori_no_speakers_folder = Path(sub_original_folder).parent / "original_no_speakers"
            # Create the folder (and any missing parents) if it doesn’t exist
            ori_no_speakers_folder.mkdir(parents=True, exist_ok=True)
            vt.clean_Netflix_srt(sub_original_folder,ori_no_speakers_folder)
        except:
            print(f"There's an error in season: {season}. ❌")
            error_count += 1
    if error_count == 0:
        print("All seasons are processed correctly. 😊✅")

create_cleaned_sub_BigBang()


vt.srt_to_Excel(srt_path = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Subtitle\German Netflix\original_no_speakers"
    , output_path = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Subtitle\German Netflix\original_no_speakers"
    )




