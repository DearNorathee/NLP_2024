# -*- coding: utf-8 -*-
"""
Created on Mon May  5 09:54:35 2025

@author: Norat
"""



import playsound
# speed performance, it took about 10 min to extract German audio for bigbang 1 season(.mp3)
import video_toolkit as vt
import os_toolkit as ost
from typing import Dict, Literal, Union, List
from pathlib import Path
import os
import shutil
import py_string_tool as pst
from beartype import beartype

from play_audio_file import play_alarm_done, play_alarm_error

# play_alarm_done()
input_video_folders: dict[int, Union[str,Path]] = {}
output_audio_folders: dict[int, Union[str,Path]] = {}
output_sub_folders: dict[int, Union[str,Path]] = {}

skip_season = [1,7]

LANGUAGE:str = "French"
# the_100_fr_s1 = r"C:\C_Video\French\The 100 FR\The 100 Season 01 French"

the_100_fr_video_paths = [None for _ in range(100)]


input_video_folder = fr"C:\C_Video\French\The 100 FR"

folder_names_str = ost.get_folders_name(input_video_folder)
# doesn't work when there's number in series's name
# avaliable_seasons = pst.get_num(folder_names_str)
avaliable_seasons = [1,2,3,4,5,6,7]

folder_paths = ost.get_folders_path(input_video_folder)

# for i in range(1,8):
#     season_str = str(i).zfill(2)
#     the_100_fr_video_paths[i] = fr"C:\C_Video\French\The 100 FR\The 100 Season {season_str} French"


# set up all paths
for i, season in enumerate(avaliable_seasons):
    season_str = str(season).zfill(2)
    input_video_folders[season] = folder_paths[i]
    
    output_audio_folders[season] = fr"C:\C_Video_Python\The 100\The 100 Season {season_str}\Season {season_str} Audio\{LANGUAGE}\original"
    output_sub_folders[season] = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Subtitle\German Netflix\original"
    # sub_adj_folder[season] = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Subtitle\German Netflix\cut_front_1_sec"
    # audio_adj_folder[season] = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Audio\{LANGUAGE}\cut_front_1_sec"
    

# rename files using prefix
# for i in range(1,8):
#     ost.auto_rename_series(folder_path = the_100_fr_video_paths[i], prefix = "The 100 FR_")
    
    
# the_100_FR_mem = ost.filesize_in_folder("C:\C_Video\French\The 100 FR")
# the_100_PT_mem = ost.filesize_in_folder("G:\My Drive\G_Videos\Portuguese\The 100 PT")


# vt.create_series_working_folder(
#     series_name = "The 100"
#     ,create_structure_at = r"C:\C_Video_Python"
#     ,audio_folders = ["French","Portuguese","English","Spanish","German"]
#     ,subtitle_folders = ["English_ori",  "Portuguese_ori",  "Portuguese_whisper_base","French_whisper_base",]
#     ,end_seasons = 7)


# extract audio for all seasons
for season, audio_output_folder in output_audio_folders.items():

    if season not in skip_season:
        if os.path.exists(audio_output_folder):
            if not os.path.exists(output_audio_folders[season]):
                os.makedirs(output_audio_folders[season], exist_ok=True)
                
            vt.extract_audio(
                video_folder=input_video_folders[season],
                output_folder=output_audio_folders[season],
                # languages= LANGUAGE
                )
                
            print(f"Done season: {season}✅")
        else:
            print(f"{audio_output_folder} does not exist. ❌")


# extract audio for 1 season(for debugging)
# took about 10 min for per season
vt.extract_audio(video_folder=input_video_folders[1], output_folder = output_audio_folders[1])


vt.extract_audio_1file(video_path = r"C:\C_Video\French\The 100 FR\The 100 Season 01 French\The 100 FR_S01E01.avi"
                       , output_folder = output_audio_folders[1])

