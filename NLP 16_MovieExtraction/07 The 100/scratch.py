# -*- coding: utf-8 -*-
"""
Created on Tue Dec 30 10:48:28 2025

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

# --- Example Usage ---



sub_01_path = fr"C:\C_Video_Python\3 Body Problem\3 Body Problem Season 01\Season 01 Subtitle\English\3 Body Problem_S01E08_eng.srt"
sub_02_path = fr""

sub_01_df = vt.sub_to_df(sub_01_path)
sub_02_df = vt.sub_to_df(sub_02_path)


