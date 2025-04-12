# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 11:27:07 2025

@author: Heng2020
"""

import video_toolkit as vt
import os
import stable_whisper
import whisper
import torch

input_video_path = r"H:\H_Download\Video 01\2024\The 100 - 7"
audio_PT_path = r"C:\C_Video_Python\Portuguese\The 100\Audio Extracted\The 100 season 7\Portuguese mp3"
audio_EN_path = r"C:\C_Video_Python\Portuguese\The 100\Audio Extracted\The 100 season 7\English mp3"


whisper_PT_sub_folder = r"C:\C_Video_Python\Portuguese\The 100\Whisper base Subtitle PT\The 100 season 7"

season_07_manual_audio_PT = [
    # r"C:\C_Video_Python\Portuguese\The 100\Audio Extracted\The 100 season 7\Portuguese mp3\The 100 PT_S07E04_PT.mp3"
    r"C:\C_Video_Python\Portuguese\The 100\Audio Extracted\The 100 season 7\Portuguese mp3\The 100 PT_S07E08_PT.mp3"
    # ,r"C:\C_Video_Python\Portuguese\The 100\Audio Extracted\The 100 season 7\Portuguese mp3\The 100 PT_S07E16_PT.mp3"
    ]
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
# vt.extract_audio(video_folder = input_video_path, output_folder = audio_PT_path, languages="Portuguese",output_extension=".wav")

# took about 10 min to extract the audio for whole season for .mp3
# 45 sec per video

#%%
# vt.extract_audio(video_folder = input_video_path, output_folder = audio_PT_path, languages="Portuguese")

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
faster_model_base = stable_whisper.load_faster_whisper('base')
#%%
# vt.audio_to_sub(model, audio_paths)


# vt.audio_to_sub
# you need to use env: stable_whisper
# env: stable_whisper_2 still have some error, this might be because I haven't downloaded the model in this env
#%%
# vt.audio_to_sub(model = faster_model_base, audio_paths = audio_PT_path, language="pt", )


#%%
# S07E16 & S07E04, S07E08
# output subtitle is in English
#  the reason is because it takes a sample of audio (maybe the first 30 sec of audio)
# All of them has only sound effect, and whisper is tricked to think that it has no speech and hence choose English as default
# I checked and the audio is in Portuguese for both episodes

# from the premary result, it looks like if audio is in Portuguese, but I specify as English, the translation quality
# directly from stable_whisper is relatively good as well :>

# language for not has to be 2chr
vt.audio_to_sub(model = faster_model_base, audio_paths = season_07_manual_audio_PT, output_folder=whisper_PT_sub_folder,language="pt", )


