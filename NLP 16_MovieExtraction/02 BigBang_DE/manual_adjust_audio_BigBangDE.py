# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 09:53:09 2025

@author: Norat
"""


# what if audio has multiple langauges?
import playsound
# speed performance, it took about 10 min to extract German audio for bigbang 1 season(.mp3)
import video_toolkit as vt
import os_toolkit as ost
from typing import Dict, Literal, Union, List
from pathlib import Path
import os
import shutil
import py_string_tool as pst

from play_audio_file import play_alarm_done, play_alarm_error

# play_alarm_done()
input_video_folders: Dict[int, Union[str,Path]] = {}
output_audio_folders: dict[int, Union[str,Path]] = {}
output_sub_folders: dict[int, Union[str,Path]] = {}

sub_adj_folder:dict[int,Union[str,Path]] = {}
audio_adj_folder:dict[int,Union[str,Path]] = {}

LANGUAGE:str = "German"

# for subtitles
LANG_CODE:str = "deu"
skip_season = []
# assuming all season have the same folder structure:
    
# C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 01\Season 01 Audio\German

input_video_folder = fr"C:\DVDFab\StreamFab\Output\Netflix\The Big Bang Theory_German"

folder_names_str = ost.get_folders_name(input_video_folder)
avaliable_seasons = pst.get_num(folder_names_str)

folder_paths = ost.get_folders_path(input_video_folder)

# set up all paths
for i, season in enumerate(avaliable_seasons):
    season_str = str(season).zfill(2)
    input_video_folders[season] = folder_paths[i]
    output_audio_folders[season] = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Audio\{LANGUAGE}\original"
    output_sub_folders[season] = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Subtitle\German Netflix\original"
    sub_adj_folder[season] = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Subtitle\German Netflix\cut_front_1_sec"
    audio_adj_folder[season] = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Audio\{LANGUAGE}\cut_front_1_sec"


audio_adj_folder[6] = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Audio\German\add_front_1_sec"
output_audio_folders[6]

vt.add_front_audio(filepaths = output_audio_folders[6], sec = 1,output_folder=audio_adj_folder[6])

