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

def test_change_audio_speed():
    audio_path01 = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Audio\French"
    test_output = r"C:\C_Video_Python\video_toolkit_test\test_change_audio_speed"
    test_output_paths = [None for _ in range(100)]

    for i, curr_path in enumerate(test_output_paths):
        test_output_paths[i] = Path(test_output) / f"test_{str(i).zfill(2)}"

    for i in range(1,2):
        ost.delete_files_in_folder(test_output_paths[i],verbose=0)
    
    change_audio_speed(audio_paths = audio_path01,speedx=0.96,output_folder=test_output_paths[1])

@beartype
def change_audio_speed(
    audio_paths: Union[str, Path, list[str|Path]]
    ,speedx:float|int
    ,output_folder: str|Path
    # optional
    ,prefix:str = ""
    ,suffix:str = ""
    ,shift_forward_sec: float|int = 0
    # input below would get import automatically
    ,errors:Literal["warn","raise"] = "raise"
    ,print_errors:bool = False

    # handle_multi_input parameters
    ,progress_bar: bool = True
    ,verbose: int = 0
    ,alarm_done: bool = False
    ,alarm_error: bool = False
    ,input_extension: str|None = [".mp3",".wav",".flac",".aac",".ogg",".m4a",".wma",".alac",".aiff",".opus"]
    ) -> None:

    
    """
    Change subtitle speed for a single file or a folder of files.

    Parameters
    ----------
    sub_paths : Union[str, Path, list[str|Path]]
        Filepath(s) of the subtitle file(s) to change speed for.
    speedx : float|int
        Speed multiplier to apply to the subtitle timing. e.g. 0.96 for 96% of the original speed.
    output_folder : str|Path
        Folder to save the output subtitle file(s) to.
    shift_forward_sec : float|int, optional
        Number of seconds to shift the subtitle timing forward. Defaults to 0.
    errors : Literal["warn","raise"], optional
        How to handle errors when reading the subtitle file(s). Defaults to "raise".
    print_errors : bool, optional
        Whether to print error messages when reading the subtitle file(s). Defaults to False.

    handle_multi_input parameters
    ----------------------------
    progress_bar : bool, optional
        Whether to show a progress bar when processing folders/lists. Defaults to True.
    verbose : int, optional
        Verbosity level (0=quiet, 1=normal, 2=detailed output). Defaults to 0.
    alarm_done : bool, optional
        Play success sound after completion. Defaults to False.
    alarm_error : bool, optional
        Play error sound if processing fails. Defaults to False.
    input_extension : str|None, optional
        File extensions to process when input is a folder. Defaults to [".ass",".srt"]

    Returns
    -------
    None
    """

    # medium tested
    import inspect_py as inp
    unique_input = {
        "filepaths":audio_paths
        ,"output_folder":output_folder

        # unique inputs for variety of functions
        ,"speedx":speedx
        # ,"shift_forward_sec": shift_forward_sec
        ,"prefix":prefix
        ,"suffix":suffix
    }
    handle_multi_input_params = {
        "progress_bar": progress_bar
        ,"verbose":verbose
        ,"alarm_done":alarm_done
        ,"alarm_error":alarm_error
        ,"input_extension":input_extension
    }
    func_temp = inp.handle_multi_input(**handle_multi_input_params)(vt.change_audio_speed_1file)
    result = func_temp(**unique_input)
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

    for i in range(1,5):
        ost.delete_files_in_folder(test_output_paths[i],verbose=0)

    vt.change_subtitle_speed(test_input01,speedx=0.96,output_folder=test_output_paths[1] )             
    vt.change_subtitle_speed(test_input01,speedx=0.96,prefix="prefix",output_folder=test_output_paths[2] )                    
    vt.change_subtitle_speed(test_input01,speedx=0.96,suffix="0.96x",output_folder=test_output_paths[3] )       
    vt.change_subtitle_speed(test_input01,speedx=0.96,prefix="shift2sec",suffix="0.96x",output_folder=test_output_paths[4],shift_forward_sec=2 )   

def test_change_subtitle_speed_df_1file():
    sub_path01 = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Subtitle\French_whisper_base\BigBang FR S02E01_FR.srt"
    df_sub_modified = vt.change_subtitle_speed_df_1file(sub_path01,2)

def test_change_subtitle_speed_1file():
    sub_path01 = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Subtitle\French_whisper_base\BigBang FR S02E01_FR.srt"
    output_folder01 = r"C:\Users\Norat\OneDrive\Python MyLib\Python MyLib 01_test\video_toolkit_test\test_change_subtitle_speed_1file"
    vt.change_subtitle_speed_1file(sub_path01,2, output_folder01, suffix="speedx_2")
    vt.change_subtitle_speed_1file(sub_path01,0.96, output_folder01, suffix="speedx_0.96")
    vt.change_subtitle_speed_1file(sub_path01,0.959, output_folder01, suffix="speedx_0.959")

test_change_audio_speed()
test_change_subtitle_speed()
# test_change_subtitle_speed_1file()
# test_adjust_speed()