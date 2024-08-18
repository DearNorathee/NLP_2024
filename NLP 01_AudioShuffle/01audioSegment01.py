
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
    alarm_done_path = r"H:\D_Music\Sound Effect positive-logo-opener.mp3"
    video_path =    Path( r"H:\D_Video\BigBang French\BigBang FR Season 02\BigBang FR S02E01.mkv")
    srt_path =      Path( r"H:\D_Video\BigBang French\BigBang FR Season 02\BigBang FR S02E01_FR.srt")
    folder_path =   Path( r"H:\D_Music\_Learn Languages\French\BigBang FR\Season 02\S02E01")
    prefix_name =   "BigBang FR S01E01"
    vt.split_1audio_by_subtitle(video_path,srt_path,output_folder = folder_path,prefix_name=prefix_name)
    print()


split_BigBangFR_S02E01()
# test_split_1audio_by_subtitle()
