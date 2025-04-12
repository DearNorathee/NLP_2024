# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 10:10:57 2025

@author: Norat
"""

# not successfull with stable_whisper yet
import video_toolkit as vt
import os
import stable_whisper
import whisper
import torch
from playsound import playsound

vt.play_audio(r"C:\C_Music\Sound Effect positive-massive-logo.wav")

# playsound(r"C:\C_Music\Sound Effect positive-massive-logo.wav")

# whisper.available_models()
model = whisper.load_model('base')

input_video_path = r"G:\My Drive\G_Videos\Portuguese\The 100 PT\The 100 Season 01 Portuguese"



audio_PT_path = r"C:\C_Video_Python\Portuguese\The 100\Audio Extracted\The 100 season 1\Portuguese mp3"
audio_EN_path = r"C:\C_Video_Python\Portuguese\The 100\Audio Extracted\The 100 season 1\English mp3"

whisper_PT_sub_folder = r"C:\C_Video_Python\Portuguese\The 100\Whisper base Subtitle PT\The 100 season 1"

audio_test01 = r"C:\C_Video_Python\Portuguese\The 100\Audio Extracted\The 100 season 1\Portuguese mp3\The 100 PT_S01E01_PT.wav"


os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
faster_model_base = stable_whisper.load_faster_whisper('base')

vt.extract_audio(video_folder = input_video_path, output_folder = audio_PT_path, languages="Portuguese",output_extension=".mp3")

vt.audio_to_sub(model = faster_model_base, audio_paths = audio_test01, output_folder=whisper_PT_sub_folder,language="pt", )
