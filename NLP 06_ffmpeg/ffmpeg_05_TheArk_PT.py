# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 10:22:59 2024

@author: Heng2020
"""
import video_toolkit as vt

from typing import List, Tuple, Literal, Union
from pathlib import Path
import inspect_py as inp
# Sub
import python_wizard as pw
import stable_whisper
import os

def extract_the_Ark():
    import video_toolkit as vt
    folder_the_Ark = Path(r"H:\D_Video\The Ark Season 01 Portuguese")
    output_folder_PT = r"H:\D_Video\The Ark Season 01 Portuguese\Audio Extracted\Portuguese"
    output_folder_EN = r"H:\D_Video\The Ark Season 01 Portuguese\Audio Extracted\English"
    vt.extract_audio(folder_the_Ark, output_folder_PT,languages="portuguese")
    vt.extract_audio(folder_the_Ark, output_folder_EN,languages="english")
    print("extract_the_Ark")

def whisper_extract_the_Ark_s1():
    import video_toolkit as vt
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
    faster_model_base = stable_whisper.load_faster_whisper('base')

    input_audio_folder = Path(r"H:\D_Video\The Ark Season 01 Portuguese\Audio Extracted\Portuguese 1")

    output_sub_folder = r"H:\D_Video\The Ark Season 01 Portuguese\Whisper base Subtitle PT"
    vt.audio_to_sub(faster_model_base, audio_path = input_audio_folder,output_folder=output_sub_folder)

def split_audio_the_Ark_s1():
    input_audio_path = Path(r"H:\D_Video\The Ark Season 01 Portuguese\Audio Extracted\Portuguese 1\The Ark S01E02 PT_PT.mp3")
    input_sub_path = "H:\D_Video\The Ark Season 01 Portuguese\Subtitles\srt\The Ark S01E02 PT.srt"

    output_sub_folder = r"H:\D_Video\The Ark Season 01 Portuguese\Subtitles\splited_audio\The Ark S01E02 PT"
    vt.split_1audio_by_subtitle(
        video_path = input_audio_path, 
        subtitle_path = input_sub_path, 
        output_folder = output_sub_folder,
        include_sentence=False
        )

# extract_the_Ark()
whisper_extract_the_Ark_s1()
split_audio_the_Ark_s1()
