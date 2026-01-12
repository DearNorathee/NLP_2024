# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 11:47:38 2025

@author: Norat
"""
# took about    
    # 3 hr (Oct 3, 2025) (Done main logic)
    # 0.5 hr (Oct 4,2025) (Packaged functions and generalize)

# main logic is done NEXT: focus on package the function in main_orginizer(function)
# generalize to use this in other series, (move_file_bulk)

# seperate template_dict(original template dict for mapping langauge_code: langauge_name) this will speed things up quite a bit
# 

import video_toolkit as vt
import os_toolkit as ost
from typing import Dict, Literal, Union, List, Callable
from pathlib import Path
import os
from play_audio_file import play_alarm_done, play_alarm_error
import py_string_tool as pst
import pandas as pd



def map_filename_to_lang(path: str|Path, mapping_dict: dict[str, str]) -> str:
    """
    Map the filename to the language.
    """
    path_obj = Path(path)
    
    filename = path_obj.stem
    lang_2chr = filename.split("_")[-1]
    language_name = mapping_dict[lang_2chr]
    return language_name

def make_lang_start_dict():
    # seperate dict creation from mapping to langauge folder to speed things up quite significantly
    lang_dict_lower = vt.make_all_language_dict(key_as="alpha3",value_as="name")  
    lang_dict_upper = dict()
    for key, value in lang_dict_lower.items():
        lang_dict_upper[key.upper()] = value

    # lang_dict_upper['DE'] = 'German Amazon'
    # lang_dict_upper['ES'] = 'Spanish (Latin America) Amazon'
    # lang_dict_upper['EN'] = 'English Amazon'
    # lang_dict_upper['FR'] = 'French Amazon'
    # lang_dict_upper['IT'] = 'Italian Amazon'
    # lang_dict_upper['PT'] = 'Portuguese Amazon'
    # lang_dict_upper['TR'] = 'Turkish Amazon'
    return lang_dict_upper

def test_map_filename_to_lang():
    """
    Test the map_filename_to_lang function.
    """
    path01 = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 01\Season 01 Audio\Amazon_temp\The Big Bang Theory_S01E01_0_DE.mp3"
    mapping_dict = make_lang_start_dict()
    actual01 = map_filename_to_lang(path01, mapping_dict)
    print(actual01)

def move_file_1season(
        season:int
        ,input_root_template
        ,output_root_template
        ):

    season_str = str(season).zfill(2)
    
    input_root_path = pst.TString(input_root_template).fill_values(season_str)
    output_root_path = pst.TString(output_root_template).fill_values(season_str)
    
    exclude_folder = ['Amazon_temp']
    
    # lang_dict_upper is used inside map_filename_to_lang
    lang_dict_upper = make_lang_start_dict()
    # map_filename_to_lang_step2 = partial(map_filename_to_lang, mapping_dict=lang_dict_upper)

    # move_file_df is for debugging to see which files will go to which folder
    move_file_df = ost.make_move_file_bulk_df(
        input_root_path = input_root_path
        ,output_root_path = output_root_path
        ,map_filename_func = map_filename_to_lang
        ,mapping_dict = lang_dict_upper
        ,exclude_folder = exclude_folder
    )
    ost.move_file_bulk(
        input_root_path = input_root_path
        ,output_root_path = output_root_path
        ,map_filename_func = map_filename_to_lang
        ,mapping_dict = lang_dict_upper
        ,exclude_folder = exclude_folder
    )

# move_media_file_bulk
def main_orginizer():
    
    from pandarallel import pandarallel
    import shutil
    from tqdm.auto import tqdm
    from functools import partial

    loop_season = tqdm(range(1,13), colour = '#1b487b')
    
    input_root_template = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {}\Season {} Audio\Amazon_temp"
    output_root_template = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {}\Season {} Audio"


    for season in loop_season:
        loop_season.set_description(f"Processing season {season}")
        move_file_1season(season, input_root_template, output_root_template)
        # try:
        #     move_file_1season(season)
        # except:
        #     print(f"There's an error in season: {season}. Please check.❌")

# test_map_filename_to_lang()
main_orginizer()
# main_orginizer()
# test_make_language_dict()
# test_map_filename_to_lang()
    





