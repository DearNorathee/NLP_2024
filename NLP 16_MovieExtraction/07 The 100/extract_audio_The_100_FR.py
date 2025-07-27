# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 10:24:21 2025

@author: Norat
"""

import video_toolkit as vt
import os
import stable_whisper
import whisper
import torch
from playsound import playsound
import modeling_tool as mlt


input_folder01 = r"G:\My Drive\G_Videos\Portuguese\The 100 PT\The 100 Season 02 Portuguese"

output_folder01 = r"G:\My Drive\G_Video_Python\02 The 100_FR"

vt.extract_audio(video_folder =input_folder01 , output_folder = output_folder01)
