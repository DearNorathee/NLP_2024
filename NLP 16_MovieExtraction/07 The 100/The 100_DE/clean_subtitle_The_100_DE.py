# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 10:51:57 2025

@author: Norat
"""

import video_toolkit as vt
import os
import stable_whisper
import whisper
import torch
from playsound import playsound
import modeling_tool as mlt
import os_toolkit as ost
from pathlib import Path
import shutil

sub_path01 = r"C:\C_Video_Python\The 100\The 100 Season 01\Season 01 Subtitle\German Amazon Auto\The 100 S01E01_DE_1_deu.srt"

sub_df01 = vt.sub_to_df(sub_path01)

# vt.create_series_working_folder(series_name, create_structure_at, audio_folders, subtitle_folders, end_seasons)