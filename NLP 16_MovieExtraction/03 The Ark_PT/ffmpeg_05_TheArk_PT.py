# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 10:22:59 2024

@author: Heng2020
"""
import video_toolkit as vt

from typing import List, Tuple, Literal, Union
from pathlib import Path
import inspect_py as inp
import modeling_tool as ml
# Sub
import python_wizard as pw
import stable_whisper
import os
import os_toolkit as ost
# ml.check_gpu()

def extract_the_Ark_debug_01():
    import video_toolkit as vt
    folder_the_Ark = Path(r"H:\D_Video\The Ark Season 01 Portuguese")
    video_path1 = r"H:\D_Video\The Ark Season 01 Portuguese\The Ark S01E10 PT.mkv"
    output_folder = r"H:\D_Video\The Ark Season 01 Portuguese\Audio Extracted\Debug"
    output_name = "The Ark S01E10 PT"
    vt.extract_audio_1file(video_path1, output_folder, output_name,encoding="utf-8")
    print(f"From extract_the_Ark_debug_01")

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
    vt.audio_to_sub(faster_model_base, audio_paths = input_audio_folder,output_folder=output_sub_folder)

def whisper_extract_the_Ark_s1_left():
    # extract the left videos which is episode 10, 11,12
    import video_toolkit as vt
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
    faster_model_base = stable_whisper.load_faster_whisper('base')

    input_audio_folder = [
        # r"H:\D_Video_Python\Portuguese\The Ark_PT\Audio Extracted\Portuguese\The Ark S01E10 PT_PT.mp3",
        # r"H:\D_Video_Python\Portuguese\The Ark_PT\Audio Extracted\Portuguese\The Ark S01E11 PT_PT.mp3",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Audio Extracted\Portuguese\The Ark S01E12 PT_Final_PT.mp3",
        
        ]

    output_sub_folder = r"H:\D_Video_Python\Portuguese\The Ark_PT\Whisper base Subtitle PT"
    vt.audio_to_sub(faster_model_base, audio_paths = input_audio_folder,output_folder=output_sub_folder)

def split_audio_the_Ark_s1():
    # use sub from video 
    # split as mp3 is much slow than wav
    input_audio_path = Path(r"H:\D_Video\The Ark Season 01 Portuguese\Audio Extracted\Portuguese 1\The Ark S01E02 PT_PT.mp3")
    input_sub_path = r"H:\D_Video\The Ark Season 01 Portuguese\Subtitles\srt\The Ark S01E02 PT.srt"

    output_sub_folder = r"H:\D_Video\The Ark Season 01 Portuguese\Subtitles\splited_audio\The Ark S01E02 PT"
    vt.split_1audio_by_subtitle(
        video_path = input_audio_path, 
        subtitle_path = input_sub_path, 
        output_folder = output_sub_folder,
        include_sentence=True,
        out_audio_ext="mp3"
        
        )

def split_audio_the_Ark_s1_whisper_sub():
    # whisper sub with modified sub seems to work better than original sub(timestamp)
    
    # use sub from video 
    # split as mp3 is much slow than wav
    input_audio_path = Path(r"H:\D_Video\The Ark Season 01 Portuguese\Audio Extracted\Portuguese 1\The Ark S01E02 PT_PT.mp3")
    input_sub_path = r"H:\D_Video\The Ark Season 01 Portuguese\Whisper base Subtitle PT\The Ark S01E02 PT_PT.srt"

    output_sub_folder = r"H:\D_Video\The Ark Season 01 Portuguese\Subtitles\splited_audio\The Ark S01E02 PT_2"
    
    sub_df = vt.sub_to_df(input_sub_path)
    modified_sub = vt.modify_sub_df_time(sub_df)
    
    vt.split_1audio_by_sub_df(
        video_path = input_audio_path, 
        subs_df = modified_sub, 
        output_folder = output_sub_folder)

def srt_to_excel_Ark_s1():

    input_sub_folder = r"H:\D_Video\The Ark Season 01 Portuguese\Whisper base Subtitle PT"
    output_folder = r"H:\D_Video\The Ark Season 01 Portuguese\Whisper base Subtitle PT\Excel Generated"
    vt.srt_to_Excel(srt_path = input_sub_folder, output_path = output_folder)

def test_nested_progress_bar():
    # this works with .py but not in IPython
    from tqdm.auto import tqdm
    # from tqdm.notebook import tqdm
    # from tqdm import tqdm
    import time
    for i in tqdm(range(5), desc="Outer Loop", position=0, dynamic_ncols=True):
        # Inner loop (20 iterations), with a new progress bar for each outer iteration
        for j in tqdm(range(10), desc="Inner Loop", position=1, leave=False, dynamic_ncols=True):
            time.sleep(0.1)  # Simulate some work

def create_BigBang_folder_structure():
    input_path = r"H:\D_Video\BigBang French"
    structure = ost.extract_folder_structure(input_path)
    output_folder = r"H:\D_Video_Python\French\BigBang French"
    ost.create_folder_structure(output_folder, structure)

def test_split_audio_by_sub():
    media_paths: list[str] = [
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Audio Extracted\Portuguese\The Ark S01E03 PT_PT.mp3",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Audio Extracted\Portuguese\The Ark S01E04 PT_PT.mp3",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Audio Extracted\Portuguese\The Ark S01E05 PT_PT.mp3",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Audio Extracted\Portuguese\The Ark S01E06 PT_PT.mp3",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Audio Extracted\Portuguese\The Ark S01E07 PT_PT.mp3",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Audio Extracted\Portuguese\The Ark S01E08 PT_PT.mp3",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Audio Extracted\Portuguese\The Ark S01E09 PT_PT.mp3",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Audio Extracted\Portuguese\The Ark S01E10 PT_PT.mp3",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Audio Extracted\Portuguese\The Ark S01E11 PT_PT.mp3",

    ]
    sub_paths: list[str] = [
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Whisper base Subtitle PT\The Ark S01E03 PT_PT.srt",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Whisper base Subtitle PT\The Ark S01E04 PT_PT.srt",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Whisper base Subtitle PT\The Ark S01E05 PT_PT.srt",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Whisper base Subtitle PT\The Ark S01E06 PT_PT.srt",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Whisper base Subtitle PT\The Ark S01E07 PT_PT.srt",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Whisper base Subtitle PT\The Ark S01E08 PT_PT.srt",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Whisper base Subtitle PT\The Ark S01E09 PT_PT.srt",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Whisper base Subtitle PT\The Ark S01E10 PT_PT.srt",
        r"H:\D_Video_Python\Portuguese\The Ark_PT\Whisper base Subtitle PT\The Ark S01E11 PT_PT.srt",
    ]
    main_output_folder = r"H:\D_Video_Python\Portuguese\The Ark_PT\Splited Audio PT_test"
    vt.split_audio_by_sub(media_paths=media_paths,sub_paths=sub_paths,output_folder=main_output_folder,modify_sub=True)

split_audio_the_Ark_s1()
# create_BigBang_folder_structure()

# whisper_extract_the_Ark_s1_left()    
# vt.split_audio_by_sub(video_paths, subs_paths, output_folders)

# test_nested_progress_bar()

# extract_the_Ark_debug_01()
# srt_to_excel_Ark_s1()

# split_audio_the_Ark_s1_whisper_sub()
# # extract_the_Ark()
# # whisper_extract_the_Ark_s1()
# split_audio_the_Ark_s1()
