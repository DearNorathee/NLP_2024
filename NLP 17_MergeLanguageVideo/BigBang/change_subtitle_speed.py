# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 10:50:32 2025

@author: Norat
"""

import os_toolkit as ost
from pprint import pprint
import shutil
from tqdm import tqdm
import video_toolkit as vt
from pathlib import Path
import pandas as pd
import datetime

# NEXT: write change_subtitle_speed_1file using ost.new_filepath
# then generalize it using inp.handle_multi_input and name it change_subtitle_speed
# then generalize vt.change_audio_speed_1file and name it change_audio_speed

# then calculate speedx factor for season 2
# then test on BigBang thoery season 2
# 




def adjust_speed(
    time_obj: datetime.time,
    speedx: float
    ,shift_forward_sec: float|int = 0
) -> datetime.time:
    """
    Adjust a datetime.time by a speed factor, using the datetime module alias directly.

    Parameters
    ----------
    time_obj : datetime.time
        The original time to adjust.
    speedx : float
        Speed factor: >1.0 makes time shorter (faster), <1.0 makes time longer (slower).

    Returns
    -------
    datetime.time
        The adjusted time.
    """
    # total seconds in the original time
    #  Apr, 26, 2025
    # 4o can't do it at one shot, this is from o4-mini

    total_seconds = (
        time_obj.hour * 3600
        + time_obj.minute * 60
        + time_obj.second
        + time_obj.microsecond / 1_000_000
    )

    # adjust by speed factor
    adjusted_seconds = total_seconds / speedx + shift_forward_sec

    # reconstruct hours, minutes, seconds, microseconds
    hours = int(adjusted_seconds // 3600)
    rem = adjusted_seconds - hours * 3600
    minutes = int(rem // 60)
    rem -= minutes * 60
    secs = int(rem)
    micros = int((rem - secs) * 1_000_000)

    return datetime.time(hour=hours, minute=minutes, second=secs, microsecond=micros)


def test_adjust_speed():
    time01 = datetime.time(0,2,0)
    time02 = datetime.time(0,1,30)
    
    expect01_01 = datetime.time(0,1,0)
    expect01_02 = datetime.time(0,1,10)
    expect02_01 = datetime.time(0,0,45)
    
    actual01_01 = adjust_speed(time_obj = time01, speedx = 2)
    actual01_02 = adjust_speed(time_obj = time01, speedx = 2, shift_forward_sec=10)
    actual02_01 = adjust_speed(time_obj = time02, speedx = 2)


    
    #write assert
    assert expect01_01 == actual01_01
    assert expect01_02 == actual01_02
    assert expect02_01 == actual02_01
    
    
    

def change_subtitle_speed_df_1file(
        sub_file:str|Path
        , speedx: int|float) -> pd.DataFrame:
    """
    support both str and Path, and df
    """
    if isinstance(sub_file, (str,Path)):
        df_sub = vt.sub_to_df(sub_file)
    elif isinstance(sub_file, pd.DataFrame):
        df_sub = sub_file.copy()
        
    df_sub_adj = df_sub.iloc[:,[0]]
    
    df_sub_adj['start'] = df_sub['start'].apply(lambda x: adjust_speed(x,speedx))
    df_sub_adj['end'] = df_sub['end'].apply(lambda x: adjust_speed(x,speedx))
    
    return df_sub_adj                                                           

def test_change_subtitle_speed_1file():
    sub_path01 = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Subtitle\French_whisper_base\BigBang FR S02E01_FR.srt"
    df_sub_modified = change_subtitle_speed_df_1file(sub_path01,2)


test_adjust_speed()
test_change_subtitle_speed_1file()