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
output_audio_folders: dict[int, Union[str,Path]] = {}
output_sub_folders: dict[int, Union[str,Path]] = {}

sub_adj_folder:dict[int,Union[str,Path]] = {}
audio_adj_folder:dict[int,Union[str,Path]] = {}

LANGUAGE:str = "Italian"

# for subtitles
LANG_CODE:str = "ita"
skip_season = []
# assuming all season have the same folder structure:
    
# C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 01\Season 01 Audio\German
############################################### create Italian folder #####################################

base_path = Path(r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Audio")
new_folder = base_path / "Italian"
new_folder.mkdir(parents=True, exist_ok=True)


########################################## Extract audio
input_video_folder = fr"C:\DVDFab\StreamFab\Output\Netflix\The Big Bang Theory_IT"
folder_names_str = ost.get_folders_name(input_video_folder)
avaliable_seasons = pst.get_num(folder_names_str)
folder_paths = ost.get_folders_path(input_video_folder)


for season in avaliable_seasons:
    season_str = str(season).zfill(2)
    audio_url = Path(fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Audio")
    audio_split_url = Path(fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Splitted Audio")
    sub_url = Path(fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Subtitle")
    
    audio_new_folder = audio_url / "Italian" / 'original'
    audio_split_folder = audio_split_url / "Italian"
    sub_folder = sub_url / "Italian Netflix"
    
    audio_new_folder.mkdir(parents=True, exist_ok=True)
    audio_split_folder.mkdir(parents=True, exist_ok=True)
    sub_folder.mkdir(parents=True, exist_ok=True)

#################################
# set up all paths

# avaliable_seasons = [3,4,5,6,7,8,9,10,11,12]

for i, season in enumerate(avaliable_seasons):
    season_str = str(season).zfill(2)
    input_video_folders[season] = folder_paths[i]
    output_audio_folders[season] = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Audio\{LANGUAGE}\original"
    output_sub_folders[season] = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Subtitle\Italian Netflix\original"
    sub_adj_folder[season] = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Subtitle\Italian Netflix\cut_front_1_sec"
    audio_adj_folder[season] = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Audio\{LANGUAGE}\cut_front_1_sec"

#  exclude season 1& 2
del output_audio_folders[1]
del output_audio_folders[2]

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

# # vt.extract_audio(video_folder=input_video_folders[1], output_folder = output_audio_folders[1],languages="German")

# # English and German subtitles are extracted manually by changing LANG_CODE & output_sub_folders[season]
# # extract subtitle
# for season, audio_output_folder in output_audio_folders.items():
#     if season not in skip_season:
#         if os.path.exists(audio_output_folder):
#             if not os.path.exists(output_audio_folders[season]):
#                 os.makedirs(output_audio_folders[season], exist_ok=True)
            
#             ost.delete_files_in_folder(output_sub_folders[season],verbose=0)
#             vt.extract_subtitle(
#                 video_folder = input_video_folders[season],
#                 output_folder = output_sub_folders[season],
#                 languages= LANG_CODE
#                 )
                
#             print(f"Done season: {season}✅")
#         else:
#             print(f"{audio_output_folder} does not exist. ❌")

# # clean up subtitles filenames(only for German)
# for season, audio_output_folder in output_audio_folders.items():
#     if season not in skip_season:
#         ost.auto_rename_series(folder_path = output_sub_folders[season], prefix = "BigBang DE")
        
        
# cut front 1 sec for subtitles
for season in sub_adj_folder.keys():
    vt.change_subtitle_speed(
        sub_paths = output_sub_folders[season]
        , speedx = 1
        , output_folder = sub_adj_folder[season]
        ,shift_forward_sec=-1
        )


# cut front 1 sec for audio
for season in sub_adj_folder.keys():
    vt.cut_front_audio(filepaths = output_audio_folders[season], sec = 1,output_folder = audio_adj_folder[season])
    


