# -*- coding: utf-8 -*-
"""
Created on Mon May  1 14:29:13 2023

@author: Heng2020
"""
# I workssss finally
import whisper 
import stable_whisper

import ffmpeg
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play

# no_speech_threshold: default 0.6
# increase it might help the audio to be categorize as slient

# vad_threshold: deault False
# set to True could generate a more accurate timestamp

# ,word_level =False => normal subtitles
def play_audio_slower(audio_path, speed_factor):
    # still not working
    # TODO: Find way to play audio with slower speed without changing the file
    audio = AudioSegment.from_file(audio_path)
    
    # slowed_audio = audio.speedup(playback_speed=1/speed_factor)
    slow_audio = audio._spawn(audio.raw_data, overrides={"frame_rate": int(audio.frame_rate * speed_factor)})
    play(slow_audio)

model = whisper.load_model('base')
audio_path = r"C:\Users\Heng2020\OneDrive\Icon File Image\whisper_test_01.wav"

WW_S04E01_008 = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 01\OutputData\Westworld S04E01\Westworld_S04E01_008.wav"
WW_S04E01_010 = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 01\OutputData\Westworld S04E01\Westworld_S04E01_010.wav"

path01 = r"H:\D_Music\2022 01 单依纯  永不失联的爱.mp3"

result = model.transcribe(audio_path)
text = result['text']

BigBang_S03E01 = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 01\InputData\BigBang PT S03E01.mkv"

S04E01_008_text = model.transcribe(WW_S04E01_008)['text']

S04E01_010_text = model.transcribe(WW_S04E01_010,fp16=False)['text']
text01 = model.transcribe(path01,fp16=False)['text']

play_audio_slower(WW_S04E01_010,1)


model = stable_whisper.load_model('base')
faster_model = stable_whisper.load_faster_whisper('base')
result = model.transcribe(WW_S04E01_008)
result_02 = model.transcribe(BigBang_S03E01)

result_02.to_srt_vtt('BigBang_EN_S03E01.srt')
result_02.to_srt_vtt('BigBang_EN_S03E01_no_wordlevel.srt',word_level =False)
result_02.to_srt_vtt('BigBang_EN_S03E01_no_segment.srt',segment_level=False)
result.to_srt_vtt('Westworld_S04E01_008.srt') 
