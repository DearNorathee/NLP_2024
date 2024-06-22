# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 09:05:06 2024

@author: Heng2020
"""
import simpleaudio as sa
from typing import Literal,Union

alarm_path = "H:\D_Music\Sound Effect positive-logo-opener.mp3"
wave_obj = sa.WaveObject.from_wave_file(r"H:\D_Music\_Learn Languages\French\Local TTS generated\Duolingo\04_Food\14_la soupe_soup.mp3")
play_obj = wave_obj.play()
import modeling_tool as ml
ml.check_gpu()

def play_audio(audio_path:Union[Path,str],
               engine:Literal["auto","simpleaudio","pydub","playsound"] = "auto") -> None:
    """
    

    Parameters
    ----------
    audio_path : Union[Path,str]
        DESCRIPTION.
    engine : Literal["auto","simpleaudio","pydub","playsound"], optional
        DESCRIPTION. The default is "auto".

    Returns
    -------
    None.

    """
    
    from playsound import playsound
    
    from pydub import AudioSegment
    from pydub.playback import play
    audio = AudioSegment.from_mp3(str(audio_path))
    
    try:
        wave_obj = sa.WaveObject.from_wave_file(str(audio_path))
    except:
        pass
    
    
    if engine in ["auto"]:
        try:
            # playsound
            playsound(str(audio_path))
        except:
            try:
                # simpleaudio
                play_obj = wave_obj.play()
            except:
                # pydub
                play(audio)
                
    elif engine in ["simpleaudio"]:
        play_obj = wave_obj.play()
    elif engine in ["pydub"]:
        play(audio)
    elif engine in ["playsound"]:
        playsound(str(audio_path))
        
        
    

    
import torch
print(torch.cuda.is_available())
print(torch.version.cuda)
print(torch.cuda.device_count())

import tensorflow as tf
print(tf.test.is_built_with_cuda())
print(tf.test.is_gpu_available())
