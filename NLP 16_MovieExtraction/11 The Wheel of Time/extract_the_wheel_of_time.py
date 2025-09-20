# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 11:27:07 2025

@author: Heng2020
"""

# I tried to test if extract using python in .wav, then convert .wav to .mp3 using Format factory
# The method above doesn't help saving time, because it's slow converting .wav to .mp3 anyway.(about 1.5 min)(the same spent in python)

import video_toolkit as vt
import os
import stable_whisper
import os_toolkit as ost


input_video_path = r"C:\DVDFab\StreamFab\Output\Amazon\The Wheel of Time\S01_high_res\The Wheel of Time_S01E01_Leavetaking.mkv"

sub_path = r'C:\C_Video_Python\Amazon Prime Series\The Wheel of Time\test_01\subtitles'
audio_path = r'C:\C_Video_Python\Amazon Prime Series\The Wheel of Time\test_02\audio'
meta_data = vt.get_all_metadata(input_video_path)

vt.is_ffmpeg_installed()

# test = vt.get_all_metadata(input_video_path)

vt.extract_sub_1_video(
    video_path = input_video_path
    , output_folder = sub_path)


# vt.extract_subtitle doesn't work on 1 video !!!!
vt.extract_subtitle(
    video_folder = input_video_path
    ,output_folder = sub_path
    # ,one_output_per_lang=False
    )

# took about 1.5 min for each language, about 30 min in total
vt.extract_audio_1file(
    video_path = input_video_path
    , output_folder = audio_path
    ,one_output_per_lang=False
    
    )

vt.extract_audio(
    video_folder = input_video_path
    ,output_folder = audio_path
    # ,output_extension=".wav"
    ,one_output_per_lang=False
    )


os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
faster_model_base = stable_whisper.load_faster_whisper('base')
# vt.audio_to_sub(model, audio_paths)




