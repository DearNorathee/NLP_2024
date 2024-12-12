# -*- coding: utf-8 -*-
"""
Created on Mon May  1 14:29:13 2023

@author: Heng2020
"""

# NEXT write transcribe_to_subtitle to loop through the audio files and create subtitles



# I workssss finally
# based on numba 0.58.0
# whisper 1.1.10
# stable_whisper 2.17.3
# faster-whisper 1.0.3

# https://github.com/jianfch/stable-ts

import video_toolkit as vt
# import numba
import whisper
# pip install -U stable-ts
import stable_whisper

from whisper.model import Whisper as whisper_model_Whisper

import ffmpeg
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
from typing import List, Literal, Dict, Union
import faster_whisper
from pathlib import Path
# no_speech_threshold: default 0.6
# increase it might help the audio to be categorize as slient
import os
# make sure that fast_whisper will not throw weird error
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
# vad_threshold: deault False
# set to True could generate a more accurate timestamp

# ,word_level =False => normal subtitles

# model.refine('audio.mp3', result)

# Timestamps can be further improved with refine(). This method iteratively mutes portions of the audio based on current timestamps then compute the probabilities of the tokens. Then by monitoring the fluctuation of the probabilities, it tries to find the most precise timestamps. "Most precise" in this case means the latest start and earliest end for the word such that it still meets the specified conditions.
alarm_done_path = r"H:\D_Music\Sound Effect positive-logo-opener.mp3"
def play_audio_slower(audio_path, speed_factor):
    # still not working
    # TODO: Find way to play audio with slower speed without changing the file
    audio = AudioSegment.from_file(audio_path)
    
    # slowed_audio = audio.speedup(playback_speed=1/speed_factor)
    slow_audio = audio._spawn(audio.raw_data, overrides={"frame_rate": int(audio.frame_rate * speed_factor)})
    play(slow_audio)


def transcribe_to_subtitle_1file(
        model:Union[whisper_model_Whisper, faster_whisper.WhisperModel]
        ,audio_path: Union[str,Path]
        ,output_name: Union[str,Path] = ""
        ,output_folder: Union[str,Path] = ""
        ) -> None:
    # medium tested
    # seems to work
    
    # TOADD_01: output subtitle format
    
    """
    signature function that will extract the subtitle from the audio
    """
    # if output_name is "" then default it should use the same name as the audio
    if output_name == "":
        output_name_in = Path(str(audio_path)).stem
    else:
        output_name_in = output_name

    if output_folder == "":
        output_folder_in = Path(str(audio_path)).parent
    else:
        output_folder_in = output_folder

    output_path = Path(str(output_folder_in)) / output_name_in
    
    if isinstance(model, (whisper_model_Whisper)):
        result = model.transcribe(audio_path)
    elif isinstance(model, (faster_whisper.WhisperModel)): 
        result = model.transcribe_stable(audio_path)
    result.to_srt_vtt(str(output_path),word_level =False)

# NEXT write transcribe_to_subtitle to loop through the audio files and create subtitles
def transcribe_to_subtitle(
    model:Union[whisper_model_Whisper, faster_whisper.WhisperModel]
    ,audio_path: Union[str,Path]
    ,output_name: Union[str,Path] = ""
    ,output_folder: Union[str,Path] = ""
    ,progress_bar:bool = True
    ,verbose:int = 1
    ,alarm_done:bool = True
    ,alarm_error:bool = True
    ,input_extension:Union[List[str],str] = [".mp3",".wav"]
    ) -> None:
    # list of files is not supported
    """
    audio_path could be folder_path, single_file, or list of files


    """
    import os_toolkit as ost
    from tqdm import tqdm

    alarm_done_path = r"H:\D_Music\Sound Effect positive-logo-opener.mp3"


    if ost.is_folder_path(audio_path):
        audio_full_paths = ost.get_full_filename(audio_path,extension = input_extension)
        audio_name_paths = ost.get_filename(audio_path,extension = input_extension)
        if progress_bar:
            loop_obj = tqdm( enumerate(audio_full_paths), total = len(audio_full_paths))
        else:
            loop_obj = enumerate(audio_full_paths)

        for i, path in loop_obj:
            transcribe_to_subtitle_1file(model,path,output_name = output_name,output_folder = output_folder)
            if verbose >= 1:
                print(f"{audio_name_paths[i]} done!!")
            
        if alarm_done:
            try:
                vt.play_audio(alarm_done_path)
            except:
                pass
    elif isinstance(audio_path,list):
        raise NotImplementedError(f"list of files is not supported")
    elif isinstance(audio_path,(str,Path)):
        transcribe_to_subtitle_1file(model,audio_path,output_name = output_name,output_folder = output_folder)
        if alarm_done:
            try:
                vt.play_audio(alarm_done_path)
            except:
                pass
    

def test_transcribe_to_subtitle_1file():
    # as of Aug,10,2024 cuda was still not install correctly, so I'm going to use model from 
    model = stable_whisper.load_model('base')
    BigBangFR_S02E01 = r"H:\D_Video\BigBang French\BigBang FR Season 02\BigBang FR S02E01.mkv"
    output_folder = r"H:\D_Video\BigBang French\BigBang FR Season 02\Season 02 Audio\French Subtitle"
    transcribe_to_subtitle_1file(model,BigBangFR_S02E01,output_folder = output_folder)


def test_transcribe_to_subtitle():
    import os
    # make sure that fast_whisper will not throw weird error
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
    bigBang_FR_season2 = r"H:\D_Video\BigBang French\BigBang FR Season 02\Season 02 Audio\French"
    output_folder = r"H:\D_Video\BigBang French\BigBang FR Season 02\Season 02 Audio\French Subtitle"
    faster_model_base = stable_whisper.load_faster_whisper('base')
    transcribe_to_subtitle(faster_model_base,bigBang_FR_season2,output_folder = output_folder)


def old_code():
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

    BigBangFR_S06E10 = r"C:\Users\Heng2020\Downloads\BigBang FR\Saison 6\Season 06 Audio\The Big Bang Theory_S06E10_FR.mp3"

    model = stable_whisper.load_model('base')
    faster_model_large = stable_whisper.load_faster_whisper('large-v3')
    faster_model_base = stable_whisper.load_faster_whisper('base')
    # {'tiny', 'tiny.en', 'base', 'base.en', 'small', 'small.en', 'medium', 'medium.en', 'large-v1',
    # 'large-v2', 'large-v3', or 'large'}

    result = model.transcribe(BigBangFR_S06E10)
    result.to_srt_vtt('BigBang_FR_S06E10.srt',word_level =False)

    # I wouldn't use refine from preminary result
    # the .refine doesn't improve the timestamp that much
    # upgrading to stable_whisper 2.17.3 seems to help
    # and it took 13.51 min / 20 min of videos to refine

    result_refine = model.refine(BigBangFR_S06E10,result)
    result_refine.to_srt_vtt('BigBang_FR_S06E10_refined.srt',word_level =False)

    result_02 = model.transcribe(BigBang_S03E01)
    result_02.to_srt_vtt('BigBang_EN_S03E01.srt',word_level =False)

    result_02_fast_large = faster_model_base.transcribe_stable(BigBangFR_S06E10)
    result_02_fast_base = faster_model_base.transcribe_stable(BigBang_S03E01)

    result_02.to_srt_vtt('BigBang_EN_S03E01_no_wordlevel.srt',word_level =False)
    result_02.to_srt_vtt('BigBang_EN_S03E01_no_segment.srt',segment_level=False)
    result.to_srt_vtt('Westworld_S04E01_008.srt') 

    srt_path = r"h\BigBang_FR_S06E10.srt"
    sub_output = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\BigBang_FR_S06E10.csv"
    vt.srt_to_csv(srt_path, sub_output)
    
test_transcribe_to_subtitle()
# test_transcribe_to_subtitle_1file()


