# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 11:32:38 2025

@author: Norat
"""

import video_toolkit as vt


sub_path01 = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Subtitle\German Netflix\original\BigBang DE S06E01.srt"
df_sub_01 = vt.sub_to_df(sub_path01)

PATTERN = r'^((?:\([A-Z\' ]+\)|[A-Z\']+):\s)'

df_sub_01['sentence_ori'] = df_sub_01['sentence'].copy()
# extract into a new column; missing ones become NaN
df_sub_01['speaker_prefix'] = df_sub_01['sentence'].str.extract(PATTERN)
df_sub_01['sentence'] = df_sub_01['sentence_ori'].str.replace(PATTERN, '', regex=True)

def clean_netflix_srt_1file(
    sub_path
    ,output_folder):
    pass



