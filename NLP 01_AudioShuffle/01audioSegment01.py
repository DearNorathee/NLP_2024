
########################## start run 1 ################################
import pysrt
import pandas as pd
import os
from pydub import AudioSegment
from datetime import datetime, timedelta
import time
from playsound import playsound
from typing import Literal, Union
from pathlib import Path
import shutil
import video_toolkit as vt
# Parse the SRT subtitle file

def test_split_1audio_by_subtitle():
    import video_toolkit as vt
    alarm_done_path = r"H:\D_Music\Sound Effect positive-logo-opener.mp3"
    video_path =    Path( r"H:\D_Video\The Ark Season 01 Portuguese\The Ark S01E01 PT.mkv")
    srt_path =      Path( r"H:\D_Video\The Ark Season 01 Portuguese\Subtitles\srt\The Ark S01E01 PT.srt")
    folder_path =   Path( r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 01\OutputData\split_audio_by_subtitle\test_01_Ark_S01E01")
    prefix_name =   "The Ark S01E01"
    vt.split_1audio_by_subtitle(video_path,srt_path,output_folder = folder_path,alarm_done_path = alarm_done_path)

def split_BigBangFR_S02E01():
    import video_toolkit as vt
    # the result is not great 
    # I might need to develop a way to merge the sub(with correct time) and audio together
    
    alarm_done_path = r"H:\D_Music\Sound Effect positive-logo-opener.mp3"
    video_path =    Path( r"H:\D_Video\BigBang French\BigBang FR Season 02\BigBang FR S02E01.mkv")
    srt_path =      Path( r"H:\D_Video\BigBang French\BigBang FR Season 02\BigBang FR S02E01_FR.srt")
    folder_path =   Path( r"H:\D_Music\_Learn Languages\French\BigBang FR\Season 02\S02E01")
    # shutil.rmtree(folder_path)
    prefix_name =   "BigBang FR S01E01"
    vt.split_1audio_by_subtitle(video_path,srt_path,output_folder = folder_path,prefix_name=prefix_name)
    print()


def extract_ori_sub_BigBangFR():
    video_folder = fr"H:\D_Video\BigBang French\BigBang FR Season 02"
    output_folder = r"H:\D_Video\BigBang French\BigBang FR Season 02\Season 02 Audio\French Subtitle ori Extracted"
    vt.extract_subtitle(video_folder = video_folder, output_folder = output_folder)

def extract_ori_sub_BigBangFR_1_file():
    video_path = fr"H:\D_Video\BigBang French\BigBang FR Season 02\BigBang FR S02E01.mkv"
    output_folder = r"H:\D_Video\BigBang French\BigBang FR Season 02\Season 02 Audio\French Subtitle ori Extracted"
    vt.extract_sub_1_video(video_path, output_folder)


extract_ori_sub_BigBangFR_1_file()
extract_ori_sub_BigBangFR()

# split_BigBangFR_S02E01()
# test_split_1audio_by_subtitle()
