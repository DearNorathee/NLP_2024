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
from typing import Union, Literal

# 
# then generalize it using inp.handle_multi_input and name it change_subtitle_speed
# then generalize vt.change_audio_speed_1file and name it change_audio_speed

# then calculate speedx factor for season 2
# then test on BigBang thoery season 2

@beartype
def change_subtitle_speed(
    sub_paths: Union[str, Path, list[str|Path]]
    ,speedx:float|int
    ,output_folder: str|Path
    # input below would get import automatically
    ,prefix: str = ""
    ,suffix: str = ""
    ,errors:Literal["warn","raise"] = "raise"
    ,print_errors:bool = False

    # handle_multi_input parameters
    ,progress_bar: bool = True
    ,verbose: int = 1
    ,alarm_done: bool = False
    ,alarm_error: bool = False
    ,input_extension: str|None = [".ass",".srt"]
    ):
    
    import inspect_py as inp
    path_input = {
        "filepaths":sub_paths
        ,"output_folder":output_folder
    }
    handle_multi_input_params = {
        "progress_bar": progress_bar
        ,"verbose":verbose
        ,"alarm_done":alarm_done
        ,"alarm_error":alarm_error
        ,"input_extension":input_extension
    }
    func_temp = inp.handle_multi_input(**handle_multi_input_params)(vt.change_subtitle_speed_1file)
    result = func_temp(**path_input)
    return result

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
    

def test_change_subtitle_speed():
    test_input01 = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Subtitle\French_whisper_base"
    test_output = r"C:\Users\Norat\OneDrive\Python MyLib\Python MyLib 01_test\video_toolkit_test\test_change_subtitle_speed"
    test_output_paths = [None for _ in range(100)]

    for i, curr_path in enumerate(test_output_paths):
        test_output_paths[i] = Path(test_output) / f"test_{str(i).zfill(2)}"


    change_subtitle_speed(test_input01,speedx=0.96,output_folder=test_output_paths[1] )                                 

def test_change_subtitle_speed_df_1file():
    sub_path01 = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Subtitle\French_whisper_base\BigBang FR S02E01_FR.srt"
    df_sub_modified = vt.change_subtitle_speed_df_1file(sub_path01,2)

def test_change_subtitle_speed_1file():
    sub_path01 = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Subtitle\French_whisper_base\BigBang FR S02E01_FR.srt"
    output_folder01 = r"C:\Users\Norat\OneDrive\Python MyLib\Python MyLib 01_test\video_toolkit_test\test_change_subtitle_speed_1file"
    vt.change_subtitle_speed_1file(sub_path01,2, output_folder01, suffix="speedx_2")
    vt.change_subtitle_speed_1file(sub_path01,0.96, output_folder01, suffix="speedx_0.96")
    vt.change_subtitle_speed_1file(sub_path01,0.959, output_folder01, suffix="speedx_0.959")


test_change_subtitle_speed()
# test_change_subtitle_speed_1file()
# test_adjust_speed()