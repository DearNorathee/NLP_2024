# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 10:54:06 2024

@author: Heng2020
"""
# objective of this script is to explore how to manually modify sub_df that would be used in split_1audio_by_subtitle 
# to have the better result
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


def split_BigBangFR_S02E01_srt():
    import video_toolkit as vt
    # the result is not great 
    # I might need to develop a way to merge the sub(with correct time) and audio together
    
    alarm_done_path = r"H:\D_Music\Sound Effect positive-logo-opener.mp3"
    video_path =    Path( r"H:\D_Video\BigBang French\BigBang FR Season 02\BigBang FR S02E01.mkv")
    srt_path =      Path( r"H:\D_Video\BigBang French\BigBang FR Season 02\BigBang FR S02E01_FR.srt")
    folder_path =   Path( r"H:\D_Music\_Learn Languages\French\BigBang FR\Season 02\S02E01_test2")
    # shutil.rmtree(folder_path)
    prefix_name =   "BigBang FR S01E01"
    sub_df = vt.sub_to_df(srt_path)
    sub_modified = modify_sub_df_time(sub_df)
    vt.split_1audio_by_sub_df(video_path, sub_modified, output_folder= folder_path,prefix_name=prefix_name,include_sentence=False)
    # vt.split_1audio_by_subtitle(video_path,srt_path,output_folder = folder_path,prefix_name=prefix_name)
    print()

def modify_sub_df_time(sub_df:pd.DataFrame) -> pd.DataFrame:
    # the result from this is promising
    # just simply use the next 'start' as 'end' time
    
    # it works well already but the next step is the have the cut_off where we will stop if next 'start' and current 'end'
    # is too long
    # see S01E01_009 for example
    
    from datetime import timedelta
    sub_df_copy = sub_df.copy()
    sub_df_copy['start_ori'] = sub_df_copy['start'].copy()
    sub_df_copy['end_ori'] = sub_df_copy['end'].copy()
    
    sub_df_copy['end'] = sub_df_copy['start'].shift(-1)
    
    # replace last row with the same value
    sub_df_copy.loc[sub_df_copy.index[-1], 'end'] = sub_df_copy.loc[sub_df_copy.index[-1], 'end_ori']
    return sub_df_copy


split_BigBangFR_S02E01_srt()
