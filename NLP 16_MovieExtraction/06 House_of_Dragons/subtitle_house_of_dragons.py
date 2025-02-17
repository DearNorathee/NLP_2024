# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 11:27:07 2025

@author: Heng2020
"""

import video_toolkit as vt
import os
import stable_whisper

input_video_path = r"C:\C_Video\Portuguese\House of Dragon\House of Dragon_PT Season 2"
audio_PT_path = r"C:\C_Video_Python\Portuguese\House of Dragons\Portuguese"
audio_EN_path = r"C:\C_Video_Python\Portuguese\House of Dragons\English"

# vt.extract_1_audio(
#     video_path = "C:\C_Video\Portuguese\House of Dragon\House of Dragon_PT Season 2\House of Dragon_PT S02E01.mkv"
#     ,output_folder = "audio_PT_path"
#     , output_name
    
#     )

# vt.extract_audio_1file(
#     video_path = r"C:\C_Video\Portuguese\House of Dragon\House of Dragon_PT Season 2\House of Dragon_PT S02E01.mkv"
#     , output_folder = audio_PT_path
#     ,languages="Portuguese"
#     )

# .wav generally is a bit faster than .mp3
vt.extract_audio(video_folder = input_video_path, output_folder = audio_PT_path, languages="Portuguese",output_extension=".wav")
vt.extract_audio(video_folder = input_video_path, output_folder = audio_EN_path, languages="English")

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
faster_model_base = stable_whisper.load_faster_whisper('base')
# vt.audio_to_sub(model, audio_paths)