# -*- coding: utf-8 -*-
"""
Created on Sat Jan  3 11:11:46 2026

@author: Norat
"""

import video_toolkit as vt
from pathlib import Path
from pydub import AudioSegment
import subprocess
import os_toolkit as ost
from tqdm.auto import tqdm
import os



df_path_01 = r"C:\C_Video_Python\The 100\The 100 Season 01\Season 01 Subtitle\English\The 100 S01E03_EN.srt"
df_path_02 = r"C:\C_Video_Python\The 100\The 100 Season 01\Season 01 Subtitle\English\The 100 S01E03_EN.srt"

df_01 = vt.sub_to_df(df_path_01)
df_01_step_2 = df_01.loc[(df_01['sentence'].str[:1] != "[") & ~df_01['sentence'].str.contains('<') ]



