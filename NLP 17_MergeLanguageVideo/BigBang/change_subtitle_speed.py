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
from beartype import beartype

# NEXT: write change_subtitle_speed_1file using ost.new_filepath
# then generalize it using inp.handle_multi_input and name it change_subtitle_speed
# then generalize vt.change_audio_speed_1file and name it change_audio_speed

# then calculate speedx factor for season 2
# then test on BigBang thoery season 2



def test_adjust_speed():
    time01 = datetime.time(0,2,0)
    time02 = datetime.time(0,1,30)
    
    expect01_01 = datetime.time(0,1,0)
    expect01_02 = datetime.time(0,1,10)
    expect02_01 = datetime.time(0,0,45)
    
    actual01_01 = vt.adjust_speed(time_obj = time01, speedx = 2)
    actual01_02 = vt.adjust_speed(time_obj = time01, speedx = 2, shift_forward_sec=10)
    actual02_01 = vt.adjust_speed(time_obj = time02, speedx = 2)


    
    #write assert
    assert expect01_01 == actual01_01
    assert expect01_02 == actual01_02
    assert expect02_01 == actual02_01
    
                                                  

def test_change_subtitle_speed_df_1file():
    sub_path01 = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Subtitle\French_whisper_base\BigBang FR S02E01_FR.srt"
    df_sub_modified = vt.change_subtitle_speed_df_1file(sub_path01,2)

def test_change_subtitle_speed_1file():
    sub_path01 = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Subtitle\French_whisper_base\BigBang FR S02E01_FR.srt"
    output_folder01 = r"C:\Users\Norat\OneDrive\Python MyLib\Python MyLib 01_test\test_folder\test_change_subtitle_speed_1file"
    vt.change_subtitle_speed_1file(sub_path01,2, output_folder01, suffix="speedx_2")
    vt.change_subtitle_speed_1file(sub_path01,0.96, output_folder01, suffix="speedx_0.96")
    vt.change_subtitle_speed_1file(sub_path01,0.959, output_folder01, suffix="speedx_0.959")



test_change_subtitle_speed_1file()
test_adjust_speed()