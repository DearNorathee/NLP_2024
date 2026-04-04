# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 10:47:35 2026

@author: Norat
"""
#%%
from playsound import playsound
import os
import random
import pandas as pd
import os_toolkit as ost

from pydub import AudioSegment
from pydub.playback import play
from pathlib import Path

import whisper 

import ffmpeg
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
from play_audio_file import play_alarm_done

#%%
model_base = whisper.load_model('base')
model_large = whisper.load_model('large')

#%%
audio_folder = fr"C:\C_Video_Python\3 Body Problem\3 Body Problem Season 01\Season 01 Splitted Audio\French\3 Body Problem_S01E03_FR_FR"

audio_name_list = ost.get_filename(audio_folder)
audio_full_path_list = ost.get_full_filename(audio_folder)

#%%
audio_index = 108
search_str = f"_{str(audio_index).zfill(3)}_"

#%%
# 2. Find the first match in the list
curr_audio_name = next((s for s in audio_name_list if search_str in s), None)
curr_audio_full_path = next((s for s in audio_full_path_list if search_str in s), None)

text_from_sub = curr_audio_name.split('_')[-1]
print(text_from_sub)


#%%
text_pred_base = model_base.transcribe(curr_audio_full_path,language="fr")['text']
print(text_pred_base)

#%%
text_pred_large = model_large.transcribe(curr_audio_full_path,language="fr")['text']
print(text_pred_large)
play_alarm_done()





