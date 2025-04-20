# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 13:33:43 2025

@author: Heng2020
"""
import video_toolkit as vt
import shutil
import os_toolkit as ost
from typing import Literal

# sub_paths = r"H:\D_Video\Learn French\100 questions et réponses en français A1 à C1\100 questions et réponses en français (A1 à C1)_FR.srt"
# media_paths = r"H:\D_Video\Learn French\100 questions et réponses en français A1 à C1\100 questions et réponses en français A1 à C1.mp4"

# output_folder = r"C:\C_Video_Python\Learn French\Elisa"

# output_folder02 = r"H:\D_Video\Learn French\100 questions et réponses en français A1 à C1\Question and Answer Part_YoutubeSub\100 questions et réponses en français A1 à C1."
# sub_paths = r"C:\C_Video\Learn French\Elisa\02_The French are rude and arrogant_FR.srt"
# media_paths = r"C:\C_Video\Learn French\Elisa\02_The French are rude and arrogant.mp4"

input_video_folder = r"C:\C_Video\Learn French\Elisa"
input_sub_folder = r"C:\C_Video\Learn French\Elisa"
output_folder = r"C:\C_Video_Python\Learn French\Elisa"

video_names = ost.get_filename(input_video_folder,extension=[".mkv",".mp4"])
video_paths = ost.get_full_filename(input_video_folder,extension=[".mkv",".mp4"])

n_videos = len(video_paths)
sub_paths = ost.get_full_filename(input_sub_folder,extension=[".srt",".ass"])

SUB_LANG: Literal["English","French"] = "English"
PREFIX_NAME:str = "fr_Elisa"

PREFIX_START_INDEX:int = 2

prefix_list = []
for i in range(PREFIX_START_INDEX,n_videos + PREFIX_START_INDEX):
    prefix_list.append(f"{PREFIX_NAME}{str(i).zfill(2)}")

sub_paths_selected = []

# sub must ended with language code for this script to auto detect it
for curr_path in sub_paths:
    temp_path = str(curr_path).split(".")[0]
    if SUB_LANG == "English":
        if temp_path.endswith("_EN"):
            sub_paths_selected.append(curr_path)
    elif SUB_LANG == "French":
        if temp_path.endswith("_FR"):
            sub_paths_selected.append(curr_path)


if len(sub_paths_selected) != n_videos:
    raise ValueError(f"Please check sub_paths_selected length isn't the same as number of videos.❌")


# output_folder02 = r"H:\D_Video\Learn French\100 questions et réponses en français A1 à C1\Question and Answer Part_YoutubeSub\100 questions et réponses en français A1 à C1."


ost.delete_files_in_folder(output_folder)
vt.split_audio_by_sub(
    media_paths = video_paths
    , sub_paths = sub_paths_selected
    , output_folder = output_folder
    ,prefix_names=prefix_list
    ,create_media_folder=True
    )
# shutil.copytree()


