# -*- coding: utf-8 -*-
"""
Created on Tue Dec 30 10:16:33 2025

@author: Norat
"""

import re
from pathlib import Path
import os_toolkit as ost
from typing import Type, Union, List
import video_toolkit as vt

def rename(old_path: str | Path, new_name: str) -> None:
    """
    Renames a file in its current directory.
    - old_path: The full path to the existing file.
    - new_name: The new filename (with or without extension).
    """
    
    # medium tested
    
    # 1. Convert to a Path object if it's a string
    file_path = Path(old_path)
    
    # 2. Safety check: does the file actually exist?
    if not file_path.exists():
        print(f"Error: The file '{file_path}' does not exist.")
        return

    # 3. Handle the extension
    # If new_name doesn't have an extension, we grab it from the old file
    if "." not in new_name:
        new_name = f"{new_name}{file_path.suffix}"

    # 4. Create the full destination path in the same directory
    new_path = file_path.with_name(new_name)

    # 5. Perform the rename
    try:
        file_path.rename(new_path)
    except FileExistsError as e:
        raise FileExistsError(f"{new_name} already exists in the folder please check the name.")
    except Exception as e:
        print(f"Error during rename: {e}")

eng_sub_folder = r"D:\D_Videos\Series\The 100\The 100_DE\The 100_EN"  

season_folders = ost.get_full_filename(eng_sub_folder)
  
for season_folder in season_folders:
    episode_paths = ost.get_full_filename(season_folder,return_type=Path)
    
    for old_file in episode_paths:
        # Search for digits before and after 'x'
        match = re.search(r'(\d+)x(\d+)', old_file.name)
        
        if match:
            season = match.group(1).zfill(2) # '1'
            episode = match.group(2).zfill(2) # '01'
            new_name = f"The 100 S{season}E{episode}_EN.srt"
            rename(old_file,new_name)
        # print(f"{new_name}")
print('Done :>')

sub_path_01 = r"D:\D_Videos\Series\The 100\The 100_DE\The 100_EN\The_100 - season 1.en\The 100 S01E01_EN.srt"
sub_df_01 = vt.sub_to_df(sub_path_01)
    

