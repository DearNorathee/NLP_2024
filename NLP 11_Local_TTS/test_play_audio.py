# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 09:05:06 2024

@author: Heng2020
"""
import simpleaudio as sa
from typing import Literal,Union
wave_obj = sa.WaveObject.from_wave_file(r"H:\D_Music\_Learn Languages\French\Local TTS generated\Duolingo\04_Food\14_la soupe_soup.mp3")
play_obj = wave_obj.play()
import modeling_tool as ml
ml.check_gpu()
def play_audio(file_path,engine = "auto"):
    from pydub import AudioSegment
    from pydub.playback import play
    audio = AudioSegment.from_mp3(file_path)
    play(audio)
    
import torch
print(torch.cuda.is_available())
print(torch.version.cuda)
print(torch.cuda.device_count())

import tensorflow as tf
print(tf.test.is_built_with_cuda())
print(tf.test.is_gpu_available())
