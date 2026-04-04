# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 10:57:56 2025

@author: Norat
"""
import video_toolkit as vt
from pathlib import Path
from pydub import AudioSegment
import subprocess
import os_toolkit as ost
from tqdm.auto import tqdm
import os


df_path_01 = r"C:\C_Video_Python\The 100\The 100 Season 05\Season 05 Subtitle\French_whisper_base\The 100_S05E01_FR_whisper.srt"
df_path_02 = r"C:\C_Video_Python\The 100\The 100 Season 05\Season 05 Subtitle\French_HBO\The 100_S05E01_2_fra.srt"

df_01 = vt.sub_to_df(df_path_01)

df_02 = vt.sub_to_df(df_path_02)



