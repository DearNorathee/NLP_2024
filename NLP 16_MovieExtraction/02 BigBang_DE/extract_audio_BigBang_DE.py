# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 09:51:16 2024

@author: Heng2020
"""


# Next:
    # Already extracted German audio & subtitles, I'll need to go to set-up files to setup all paths ready for merge
    # Try season 2-11 first
    
# objective of this script is to extract audio from video in BigBang for all seasons

#  change the structure of this script so that it would be very easy to run and change when there's a new langauge, or new series
#  should take less than 10 min to change, currently it's still confusing and took more than 30 min



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
output_audio_folders: Dict[int, Union[str,Path]] = {}

output_audio_folders: dict[int, Union[str,Path]] = {}
output_sub_folders: dict[int, Union[str,Path]] = {}


LANGUAGE:str = "German"

# for subtitles
LANG_CODE:str = "deu"
skip_season = []
# assuming all season have the same folder structure:
    
# C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 01\Season 01 Audio\German

input_video_folder = fr"C:\DVDFab\StreamFab\Output\Netflix\The Big Bang Theory"

folder_names_str = ost.get_folders_name(input_video_folder)
avaliable_seasons = pst.get_num(folder_names_str)

fodder_paths = ost.get_folders_path(input_video_folder)

for i, season in enumerate(avaliable_seasons):
    season_str = str(season).zfill(2)
    input_video_folders[season] = fodder_paths[i]
    output_audio_folders[season] = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Audio\{LANGUAGE}"
    output_sub_folders[season] = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Subtitle\German Netflix"

# extract audio
for season, audio_output_folder in output_audio_folders.items():

    if season not in skip_season:
        if os.path.exists(audio_output_folder):
            if not os.path.exists(output_audio_folders[season]):
                os.makedirs(output_audio_folders[season], exist_ok=True)
                
            vt.extract_audio(
                video_folder=input_video_folders[season],
                output_folder=output_audio_folders[season],
                languages= LANGUAGE
                )
                
            print(f"Done season: {season}✅")
        else:
            print(f"{audio_output_folder} does not exist. ❌")

# vt.extract_audio(video_folder=input_video_folders[1], output_folder = output_audio_folders[1],languages="German")

# English and German subtitles are extracted manually by changing LANG_CODE & output_sub_folders[season]
# extract subtitle
for season, audio_output_folder in output_audio_folders.items():
    if season not in skip_season:
        if os.path.exists(audio_output_folder):
            if not os.path.exists(output_audio_folders[season]):
                os.makedirs(output_audio_folders[season], exist_ok=True)
            
            ost.delete_files_in_folder(output_sub_folders[season],verbose=0)
            vt.extract_subtitle(
                video_folder = input_video_folders[season],
                output_folder = output_sub_folders[season],
                languages= LANG_CODE
                )
                
            print(f"Done season: {season}✅")
        else:
            print(f"{audio_output_folder} does not exist. ❌")

# clean up subtitles filenames(only for German)
for season, audio_output_folder in output_audio_folders.items():
    if season not in skip_season:
        ost.auto_rename_series(folder_path = output_sub_folders[season], prefix = "BigBang DE")
        
        

# vt.extract_subtitle(video_folder=input_video_folders[1], output_folder = output_sub_folders[1],languages= LANG_CODE)

# ost.auto_rename_series(folder_path = output_sub_folders[1], prefix = "BigBang DE")
#     )
# vt.extract_sub_1_video(
#     video_path = r"C:\DVDFab\StreamFab\Output\Netflix\The Big Bang Theory\S01\BigBang DE S01E01.mp4"
#     , output_folder = output_sub_folders[1])

def test_reset_start_timestamp_1audio():
    input_path01 = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Audio\German\BigBang DE S02E01_DE.mp3"
    vt.reset_start_timestamp_1audio(input_path01,outfilename="fixed_BigBang DE S02E01_DE_v03.mp3"
                                    ,output_folder=r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Audio\German")

def test_reset_start_timestamp():
    input_path01 = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Audio\German"
    vt.reset_start_timestamp_1audio(input_path01
                                    ,output_folder=r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Audio\German")
    
test_reset_start_timestamp()
test_reset_start_timestamp_1audio()

