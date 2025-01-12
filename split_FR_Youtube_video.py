# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 13:33:43 2025

@author: Heng2020
"""
import video_toolkit as vt
import shutil
import os_toolkit as ost

sub_paths = r"H:\D_Video\Learn French\100 questions et réponses en français A1 à C1\100 questions et réponses en français (A1 à C1)_FR.srt"
media_paths = r"H:\D_Video\Learn French\100 questions et réponses en français A1 à C1\100 questions et réponses en français A1 à C1.mp4"
output_folder = r"H:\D_Video\Learn French\100 questions et réponses en français A1 à C1\Question and Answer Part_YoutubeSub"

output_folder02 = r"H:\D_Video\Learn French\100 questions et réponses en français A1 à C1\Question and Answer Part_YoutubeSub\100 questions et réponses en français A1 à C1."

ost.delete_files_in_folder(output_folder)
vt.split_audio_by_sub(
    media_paths = media_paths
    , sub_paths = sub_paths
    , output_folder = output_folder
    ,prefix_names="fr_youtube01"
    ,create_media_folder=False
    )
# shutil.copytree()


