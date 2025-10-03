# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 11:47:38 2025

@author: Norat
"""
# took about    
    # 3 hr (Oct 3, 2025)


import video_toolkit as vt
import os_toolkit as ost
from typing import Dict, Literal, Union, List
from pathlib import Path
import os
from play_audio_file import play_alarm_done, play_alarm_error
import py_string_tool as pst
import pandas as pd



# lang_dict_upper is used inside map_filename_to_lang
lang_dict_lower = vt.make_all_language_dict(key_as="alpha2",value_as="name")  
lang_dict_upper = dict()
for key, value in lang_dict_lower.items():
    lang_dict_upper[key.upper()] = value
lang_dict_upper['PT'] = 'Portuguese_Brazil'
lang_dict_upper['ES'] = 'Spanish (Latin America)'


def test_make_language_dict():
    lang_dict = vt.make_all_language_dict(key_as="alpha2",value_as="object")  
    # count how many keys have length of 2, and how many have length of 3
    # then create seperate pd.df for these 2 groups
    count_2 = 0
    count_3 = 0
    for key in lang_dict.keys():
        if len(key) == 2:
            count_2 += 1
        elif len(key) == 3:
            count_3 += 1
    lang_dict_2 = dict()
    lang_dict_3 = dict()
    for key, value in lang_dict.items():
        if len(key) == 2:
            lang_dict_2[key] = value.language_name('en')
        elif len(key) == 3:
            lang_dict_3[key] = value.language_name('en')
    df_2 = pd.DataFrame(lang_dict_2.items(), columns=['alpha2', 'name'])
    df_3 = pd.DataFrame(lang_dict_3.items(), columns=['alpha3', 'name'])
    
    # key observation: main language would have 2key code as well
    
    print(f"Count of keys with length of 2: {count_2}")
    print(f"Count of keys with length of 3: {count_3}")
    print()

def map_filename_to_lang(path: str|Path) -> str:
    """
    Map the filename to the language.
    """
    
    path_obj = Path(path)

    
    filename = path_obj.stem
    lang_2chr = filename.split("_")[-1]
    language_name = lang_dict_upper[lang_2chr]
    return language_name

# move_media_file_bulk
def main_orginizer():
    
    from pandarallel import pandarallel
    pandarallel.initialize(progress_bar=True)
    
    input_root_path = r"C:\C_Video_Python\The Mentalist\The Mentalist Season 07\Season 07 Audio\Amazon_temp"
    output_root_path = r'C:\C_Video_Python\The Mentalist\The Mentalist Season 07\Season 07 Audio'
    
    
    
    filename = ost.get_filename(input_root_path)
    input_filepath = ost.get_full_filename(input_root_path)
    
    output_folder_names = ost.get_filename(output_root_path)
    output_folder_paths = ost.get_full_filename(output_root_path)
    
    folder_mapping = pd.DataFrame(
        {
            'language':output_folder_names
            ,'output_folder_path':output_folder_paths
        }
        )
    # exclude 'Amazon_temp' in folder_mapping
    folder_mapping = folder_mapping[~folder_mapping['language'].isin(['Amazon_temp']) ].reset_index(drop=True)

    

    
    df_orginized_step1 = pd.DataFrame(
        {
        'filepath':filename
        ,'filename':input_filepath
        }
        )
    # step2 apply map_filename_to_lang function to the filename column
    df_orginized_step1['language'] = df_orginized_step1['filename'].parallel_apply(map_filename_to_lang)
    df_orginized_step2 = pd.merge(df_orginized_step1, folder_mapping, on='language', how='left')

    print()


def test_map_filename_to_lang():
    """
    Test the map_filename_to_lang function.
    """
    path01 = r"C:\C_Video_Python\The Mentalist\The Mentalist Season 07\Season 07 Audio\Amazon_temp\The Mentalist_S07E01_0_DE.mp3"
    actual01 = map_filename_to_lang(path01)
    print(actual01)

main_orginizer()
# test_make_language_dict()
# test_map_filename_to_lang()
    





