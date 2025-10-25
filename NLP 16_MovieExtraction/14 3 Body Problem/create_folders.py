# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 14:11:20 2025

@author: Norat
"""

import os_toolkit as ost
import video_toolkit as vt





to_create_audio_folders =  [
    "Czech",
    "German",
    "English",
    "Spanish_Latin America",
    "Spanish_Spain",
    "French",
    "Hindi",
    "Hungarian",
    "Indonesian",
    "Italian",
    "Japanese",
    "Polish",
    "Portuguese_Brazil",
    "Thai",
    "Turkish",
    "Ukrainian",
    "Vietnamese",
    "Chinese"
]

to_create_sub_folders = [
    "All_temp",
    "English_ForcedNarrative",
    "English",
    "Arabic",
    "Basque",
    "Catalan",
    "Chinese_Simplified",
    "Chinese_Traditional",
    "Chinese_ForcedNarrative",
    "Croatian",
    "Czech",
    "Czech_ForcedNarrative",
    "Danish",
    "Dutch",
    "Filipino",
    "Finnish",
    "French",
    "French_CC",
    "French_ForcedNarrative",
    "Galician",
    "German",
    "German_CC",
    "German_ForcedNarrative",
    "Greek_Modern",
    "Hebrew",
    "Hindi_ForcedNarrative",
    "Hungarian",
    "Hungarian_ForcedNarrative",
    "Indonesian"
]

vt.create_series_working_folder(
    series_name = r"3 Body Problem"
    , create_structure_at = r"C:\C_Video_Python"
    , audio_folders = to_create_audio_folders, subtitle_folders=to_create_sub_folders, end_seasons = 3)

ost.auto_rename_series(folder_path = r"D:\D_Videos\Netflix Series\3 Body Problem\S01"
                       , prefix = "3 Body Problem_")