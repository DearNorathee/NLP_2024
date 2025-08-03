# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 10:36:40 2025

@author: Norat
"""
import video_toolkit as vt
import shutil
import os_toolkit as ost
from typing import Literal

input_sub_folder = r"C:\C_Video\Learn French\Elisa"

sub_paths = ost.get_full_filename(input_sub_folder,extension=[".srt",".ass"])



fr_sub_paths = []
en_sub_paths = []

# sub must ended with language code for this script to auto detect it
for curr_path in sub_paths:
    temp_path = str(curr_path).split(".")[0]
    if temp_path.endswith("_EN"):
        en_sub_paths.append(curr_path)
    elif temp_path.endswith("_FR"):
        fr_sub_paths.append(curr_path)



df_sub_fr = vt.srt_to_df(fr_sub_paths[0])
df_sub_en = vt.srt_to_df(en_sub_paths[0])

df_sub_left = df_sub_en.copy()
df_sub_right = df_sub_fr.copy()

df_sub_left['left_start_time'] = df_sub_left['start'].dt.minute
