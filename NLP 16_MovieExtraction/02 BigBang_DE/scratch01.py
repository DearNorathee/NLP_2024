# -*- coding: utf-8 -*-
"""
Created on Tue Jun  3 10:15:36 2025

@author: Norat
"""

from pathlib import Path
from typing import Type

def get_folders_name(parent_path: str| Path) -> list[str]:
    
    """
    Return a list of folder names contained directly within the given parent directory.

    Parameters:
    -----------
    parent_path : str or Path
        The path to the parent directory in which to look for subfolders.

    Returns:
    --------
    List[str]
        A list of folder names (not full paths) for every directory found inside parent_path.
    """
    
    # medium tested
    parent = Path(parent_path)
    if not parent.is_dir():
        raise ValueError(f"Provided path does not exist or is not a directory: {parent}")

    folder_names: list[str] = []
    for child in parent.iterdir():
        if child.is_dir():
            folder_names.append(child.name)

    return folder_names

def test_get_folders_name():
    input_path01 = r"C:\DVDFab\StreamFab\Output\Netflix\The Big Bang Theory"
    actual01 = get_folders_name(input_path01)
    expect01 = ['S01', 'S02', 'S03', 'S04', 'S05', 'S06', 'S07', 'S08', 'S09', 'S10', 'S11', 'S12']
    assert actual01 == expect01


def get_folders_path(parent_path: str| Path,return_type:Type = str) -> list[Path]:
    """
    Return a list of full folder paths for all directories directly within the given parent directory.

    Parameters:
    -----------
    parent_path : str or Path
        The path to the parent directory in which to look for subfolders.

    Returns:
    --------
    List[Path]
        A list of Path objects pointing to each directory found inside parent_path.
    """
    
    # medium tested
    parent = Path(parent_path)
    if not parent.is_dir():
        raise ValueError(f"Provided path does not exist or is not a directory: {parent}")

    folder_paths: list[Path] = []
    for child in parent.iterdir():
        if child.is_dir():
            if return_type in [Path]:
                folder_paths.append(child)
            elif return_type in [str]: 
                folder_paths.append(str(child))

    return folder_paths

def test_get_folders_path():
    input_path01 = r"C:\DVDFab\StreamFab\Output\Netflix\The Big Bang Theory"
    actual01 = get_folders_path(input_path01)
    expect01 = ['C:\\DVDFab\\StreamFab\\Output\\Netflix\\The Big Bang Theory\\S01'
                , 'C:\\DVDFab\\StreamFab\\Output\\Netflix\\The Big Bang Theory\\S02'
                , 'C:\\DVDFab\\StreamFab\\Output\\Netflix\\The Big Bang Theory\\S03'
                , 'C:\\DVDFab\\StreamFab\\Output\\Netflix\\The Big Bang Theory\\S04'
                , 'C:\\DVDFab\\StreamFab\\Output\\Netflix\\The Big Bang Theory\\S05'
                , 'C:\\DVDFab\\StreamFab\\Output\\Netflix\\The Big Bang Theory\\S06'
                , 'C:\\DVDFab\\StreamFab\\Output\\Netflix\\The Big Bang Theory\\S07'
                , 'C:\\DVDFab\\StreamFab\\Output\\Netflix\\The Big Bang Theory\\S08'
                , 'C:\\DVDFab\\StreamFab\\Output\\Netflix\\The Big Bang Theory\\S09'
                , 'C:\\DVDFab\\StreamFab\\Output\\Netflix\\The Big Bang Theory\\S10'
                , 'C:\\DVDFab\\StreamFab\\Output\\Netflix\\The Big Bang Theory\\S11'
                , 'C:\\DVDFab\\StreamFab\\Output\\Netflix\\The Big Bang Theory\\S12']
    # assert actual01 == expect01

test_get_folders_path()
test_get_folders_name()