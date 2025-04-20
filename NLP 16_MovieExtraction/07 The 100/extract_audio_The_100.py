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
import modeling_tool as mlt

# env: stable_whisper_2.19.0

# openai-whisper=20240930
# stable-ts=2.19.0
# faster-whisper=1.1.1

mlt.check_gpu()

vt.play_audio(r"C:\C_Music\Sound Effect positive-massive-logo.wav")

# playsound(r"C:\C_Music\Sound Effect positive-massive-logo.wav")

# whisper.available_models()
model = whisper.load_model('base')

input_video_path = r"G:\My Drive\G_Videos\Portuguese\The 100 PT\The 100 Season 01 Portuguese"



audio_PT_path = r"C:\C_Video_Python\Portuguese\The 100\Audio Extracted\The 100 season 1\Portuguese mp3"
audio_EN_path = r"C:\C_Video_Python\Portuguese\The 100\Audio Extracted\The 100 season 1\English mp3"

whisper_PT_sub_folder = r"C:\C_Video_Python\Portuguese\The 100\Whisper base Subtitle PT\The 100 season 1"

audio_test01 = r"C:\C_Video_Python\Portuguese\The 100\Audio Extracted\The 100 season 1\Portuguese wav\The 100 PT_S01E01_PT.wav"


# os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE" # no longer needed
faster_model_base = stable_whisper.load_faster_whisper('base')

# faster_model_large = stable_whisper.load_faster_whisper('large-v2')
# transcribe_stable will be depreciated
# I tested transcribe_stable vs transcribe took the same amount of time

result_fast = faster_model_base.transcribe_stable(audio_test01)
faster_model_base.transcribe(audio_test01)

# took about 2 min per episode
vt.extract_audio(video_folder = input_video_path, output_folder = audio_PT_path, languages="Portuguese",output_extension=".mp3")

vt.audio_to_sub(model = faster_model_base, audio_paths = audio_test01, output_folder=whisper_PT_sub_folder,language="pt", )

vt.play_audio(r"C:\C_Music\Sound Effect positive-massive-logo.wav")


