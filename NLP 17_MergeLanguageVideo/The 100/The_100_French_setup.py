# -*- coding: utf-8 -*-
"""
Created on Mon May  5 09:54:35 2025

@author: Norat
"""

import os_toolkit as ost
import video_toolkit as vt
import py_string_tool as pst

# setup file is intended to run once


# the_100_fr_s1 = r"C:\C_Video\French\The 100 FR\The 100 Season 01 French"

the_100_fr_video_paths = [None for _ in range(100)]

for i in range(1,8):
    season_str = str(i).zfill(2)
    the_100_fr_video_paths[i] = fr"C:\C_Video\French\The 100 FR\The 100 Season {season_str} French"

# rename files using prefix

for i in range(1,8):
    ost.auto_rename_series(folder_path = the_100_fr_video_paths[i], prefix = "The 100 FR_")
    
    
def create_bigbang_working_folder() -> None:
    """
    create bigbang working folders to store audio and subtitle(but not video)

    Returns
    -------
    None
        DESCRIPTION.

    """
    create_structure_at = r"C:\C_Video_Python"
    lang_folder = ["French","Portuguese","English","Spanish","German"]
    sub_lang_folder = ["English_ori .ass",  "English_ori .srt",  "French_ori .ass",
                       "French_ori .srt",  "French_whisper_base",  "Portuguese_ori",  "Portuguese_whisper_base"]
    
    # what folder_structure example looks like for 1 season
    
    # folder_structure = {
    #     "The Big Bang Theory":{
    #         "BigBang Theory Season 07": {
    #             "Season 07 Audio": lang_folder,
    #             "Season 07 Splitted Audio": lang_folder,
    #             "Season 07 Subtitle": sub_lang_folder,
    #             }
    #         }
    #     }
    
    folder_structure = {
        "The Big Bang Theory":{}
        }
    
    
    for season in range(1,13):
        season_str = str(season).zfill(2)
        curr_season_structure = {
                    f"Season {season_str} Audio": lang_folder,
                    f"Season {season_str} Splitted Audio": lang_folder,
                    f"Season {season_str} Subtitle": sub_lang_folder,
                    }
                
        folder_structure["The Big Bang Theory"][f"BigBang Theory Season {season_str}"] = curr_season_structure
        # pprint(curr_season_structure)
    # pprint(folder_structure)
    ost.create_folder_structure(root_folder = create_structure_at , structure = folder_structure)

