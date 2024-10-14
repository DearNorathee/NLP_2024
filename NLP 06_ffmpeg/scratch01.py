# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 10:22:15 2024

@author: Heng2020
"""
import os_toolkit as ost
from pathlib import Path
path01 = ost.print_folder_structure("G:\My Drive\G_Videos\Portuguese",include_only_folder=True)
path02 = ost.print_folder_structure("G:\My Drive\G_Videos\Portuguese",include_only_folder=False)


def test_extract_folder_structure():
    root_folder = r"C:\Users\Heng2020\OneDrive\Python MyLib\Python MyLib 01\10 OS\os_toolkit\tests\test_output\test_create_folder_structure"
    actual01 = ost.extract_folder_structure(root_folder)
    expect01 =  {
    "Portuguese": {
        "Westworld Portuguese": {
            "Westworld Portugues 01": None,
            "Westworld Portugues 02": ["folder1", "folder2"],
            "Westworld Portugues 03": None,
            "Westworld Portugues 04": None,
        },
        "BigBang Portuguese": [
            "BigBang PT Season 01",
            "BigBang PT Season 02",
            "BigBang PT Season 03",
            "BigBang PT Season 04",
            "BigBang PT Season 05",
            "BigBang PT Season 06",
            "BigBang PT Season 07",
            "BigBang PT Season 08",
            "BigBang PT Season 09",
            "BigBang PT Season 10",
            "BigBang PT Season 11",
        ],
        "The 100 PT": [
            "The 100 Season 01 Portuguese",
            "The 100 Season 02 Portuguese",
            "The 100 Season 03 Portuguese",
            "The 100 Season 04 Portuguese",
            "The 100 Season 05 Portuguese",
                    ],
                }
            }
    assert actual01 == expect01

def test_filesize_in_folder():
    path01 = r"H:\D_Video\The Ark Season 01 Portuguese\Audio Extracted\English"
    actual01 = ost.filesize_in_folder(path01)
    expect01 = []

    path02 = r"H:\D_Video\The Ark Season 01 Portuguese\Audio Extracted"
    actual02 = ost.filesize_in_folder(path02)
    
    path03 = r"G:\My Drive\G_Videos\Portuguese\The 100 PT"
    actual03 = ost.filesize_in_folder(path03)
    
    path04 = r"G:\My Drive\G_Videos\Portuguese\The 100 PT\The 100 Season 01 Portuguese"
    actual04 = ost.filesize_in_folder(path04)
    print(actual01)

test_filesize_in_folder()
test_extract_folder_structure()

path03 = Path(r"H:\D_Video\The Ark Season 01 Portuguese\Audio Extracted\Debug")

ost.delete_files_in_folder(path03)
