# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 11:01:40 2024

@author: Heng2020
"""

import stable_whisper
import video_toolkit as vt
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
faster_model_base = stable_whisper.load_faster_whisper('base')


def transcripe_fr_youtube_01():
    output_folder = r"H:\D_Video\Learn French"
    audio_paths = r"H:\D_Video\Learn French\100 questions et réponses en français A1 à C1.mp4"
    vt.audio_to_sub(
        model = faster_model_base, 
        audio_paths = audio_paths,
        output_folder=output_folder,
        )

def split_fr_youtube_01():
    output_folder = r"H:\D_Video\Learn French\100 questions et réponses en français A1 à C1"
    audio_paths = r"H:\D_Video\Learn French\100 questions et réponses en français A1 à C1.mp4"
    sub_path = r"H:\D_Video\Learn French\100 questions et réponses en français A1 à C1.srt"
    prefix_name = "fr_youtube01"
    vt.split_1audio_by_subtitle(
        video_path = audio_paths
        ,subtitle_path = sub_path
        ,output_folder = output_folder
        ,modify_sub=True
        ,prefix_name = prefix_name
        )

def get_translation_fr_youtube_01():
    # https://views4you.com/tools/youtube-subtitles-downloader/
    # this subtitle is directly from Youtube
    # the subtitle time is almost the same for start
    # but since it's not exact, I can't merge using the time directly
    sub_EN_path = r"H:\D_Video\Learn French\100 questions et réponses en français A1 à C1\100 questions et réponses en français (A1 à C1)_EN.srt"
    sub_FR_path = r"H:\D_Video\Learn French\100 questions et réponses en français A1 à C1\100 questions et réponses en français (A1 à C1)_FR.srt"
    sub_EN_df = vt.sub_to_df(sub_EN_path)
    sub_FR_df = vt.sub_to_df(sub_FR_path)
    print()

get_translation_fr_youtube_01()
# transcripe_fr_youtube_v01()
# split_fr_youtube_v01()
