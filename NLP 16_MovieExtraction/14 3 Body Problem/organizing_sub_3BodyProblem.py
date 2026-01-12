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


    lang_dict_lower['por'] = 'Portuguese_Brazil'
    lang_dict_lower['spa'] = 'Spanish_Latin America'
    lang_dict_lower['hi-Latn'] = 'Hindi_ForcedNarrative'
    lang_dict_lower['zho'] = 'Chinese_Simplified'
    lang_dict_lower['ell'] = 'Greek_Modern'

    return lang_dict_lower

def test_map_filename_to_lang():
    """
    Test the map_filename_to_lang function.
    """
    path01 = r"C:\C_Video_Python\3 Body Problem\3 Body Problem Season 01\Season 01 Subtitle\All_temp\3 Body Problem_S01E01_21_glg.srt"
    mapping_dict = make_lang_start_dict()
    actual01 = map_filename_to_lang(path01, mapping_dict)
    expect01 = 'Galician'
    print(actual01)
    assert actual01 == expect01

def move_file_1season(
        season:int
        ,input_root_template
        ,output_root_template
        ,exclude_folder = ['Amazon_temp']
        ):

    season_str = str(season).zfill(2)
    
    input_root_path = pst.TString(input_root_template).fill_values(season_str)
    output_root_path = pst.TString(output_root_template).fill_values(season_str)
    
    
    
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
        ,progress_bar=False
        
    )

# move_media_file_bulk
def main_orginizer():
    
    from pandarallel import pandarallel
    import shutil
    from tqdm import tqdm
    from functools import partial

    
    input_root_template = r"C:\C_Video_Python\3 Body Problem\3 Body Problem Season {}\Season {} Subtitle\All_temp"
    output_root_template = r"C:\C_Video_Python\3 Body Problem\3 Body Problem Season {}\Season {} Subtitle"
    exclude_folder = ['All_temp']
    processing_seasons = [1]

    loop_season = tqdm(processing_seasons, colour = '#9c5700',position=0)
    for season in loop_season:
        loop_season.set_description(f"Processing season {season}")
        move_file_1season(season, input_root_template, output_root_template,exclude_folder = exclude_folder)
        # try:
        #     move_file_1season(season)
        # except:
        #     print(f"There's an error in season: {season}. Please check.❌")

def test_move_repeated_lang_media():
    # root_path01 = Path(r"C:\C_Video_Python\video_toolkit_test\test_move_repeated_lang_media\test_01")
    # file_path01 = root_path01 / 'French_1'
    # move_path01 = [root_path01 / 'French_1',root_path01 / 'French_2', root_path01 / 'French_CC',root_path01 / 'French_ForcedNarrative']
    # move_repeated_lang_media(file_path01,move_path01)
    
    
    root_path_02 = Path(r"C:\C_Video_Python\video_toolkit_test\test_move_repeated_lang_media\test_02")
    file_path_ZHO = root_path_02 / "Chinese_Simplified"
    move_path_ZHO = [root_path_02 / 'Chinese_Simplified',root_path_02 / 'Chinese_Traditional', root_path_02 / 'Chinese_ForcedNarrative']
    
    # eng episode 5 & 6 have only 1 sub
    file_path_ENG = root_path_02 / "English"
    move_path_ENG = [root_path_02 / 'English_ForcedNarrative',root_path_02 / 'English']
    
    file_path_FRA = root_path_02 / "French_1"
    move_path_FRA = [root_path_02 / 'French_1',root_path_02 / 'French_2', root_path_02 / 'French_CC',root_path_02 / 'French_ForcedNarrative']
    
    file_path_DEU = root_path_02 / "German_1"
    move_path_DEU = [root_path_02 / 'German_1',root_path_02 / 'German_2', root_path_02 / 'German_CC',root_path_02 / 'German_ForcedNarrative']
    
    file_path_HUN = root_path_02 / "Hungarian_1"
    move_path_HUN = [root_path_02 / 'Hungarian_1',root_path_02 / 'Hungarian_2',root_path_02 / 'Hungarian_ForcedNarrative']
    
    df_move_02_ZHO = ost.move_repeated_lang_media(file_path_ZHO,move_path_ZHO)
    df_move_02_ENG = ost.move_repeated_lang_media(file_path_ENG,move_path_ENG)
    df_move_02_FRA = ost.move_repeated_lang_media(file_path_FRA,move_path_FRA)
    df_move_02_DEU = ost.move_repeated_lang_media(file_path_DEU,move_path_DEU)
    df_move_02_HUN = ost.move_repeated_lang_media(file_path_HUN,move_path_HUN)
    

main_orginizer()
test_map_filename_to_lang()
# main_orginizer()
# test_make_language_dict()
# test_map_filename_to_lang()
    





