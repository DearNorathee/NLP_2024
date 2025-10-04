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

def map_filename_to_lang(path: str|Path, mapping_dict: dict[str, str]) -> str:
    """
    Map the filename to the language.
    """
    path_obj = Path(path)
    
    filename = path_obj.stem
    lang_2chr = filename.split("_")[-1]
    language_name = mapping_dict[lang_2chr]
    return language_name

def move_file_bulk(
    input_root_path: str|Path
    ,output_root_path: str|Path
    ,map_filename_func: Callable
    ,start_mapping_dict: dict
    ,exclude_folder: List[str] = []
    ):
    #%%
    """
        Move the media file to the output folder.
        
        Parameters
        ----------
        input_root_path : str|Path
            Root folder containing files to move.
        output_root_path : str|Path
            Root folder containing destination subfolders.
        map_filename_func : Callable
            Function that takes a filename and returns a mapping key (e.g., language name).
        start_mapping_dict : dict
            Initial mapping dictionary to merge with discovered output folders.
            Keys should match the output of map_filename_func.
        exclude_folder : List[str], optional
            List of folder names to exclude from output folders.
        
        You need to specify the start dictionary like following example
        ```python
        lang_dict_lower = vt.make_all_language_dict(key_as="alpha2",value_as="name")  
        lang_dict_upper = dict()
        for key, value in lang_dict_lower.items():
            lang_dict_upper[key.upper()] = value
        ```
        Returns
        -------
        None
        
        Raises
        ------
        ValueError
            If there are any na in output_folder_path.

        Example:
        --------
        ```python
        move_file_bulk(
            input_root_path = input_root_path
            ,output_root_path = output_root_path
            ,map_filename_func = map_filename_to_lang
            ,start_mapping_dict = lang_dict_upper
            ,exclude_folder = exclude_folder
        )
        ```
    """
    #%%
    from pandarallel import pandarallel
    import shutil
    from tqdm.auto import tqdm
    pandarallel.initialize(progress_bar=True)
    
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
    folder_mapping = folder_mapping[~folder_mapping['language'].isin(exclude_folder) ].reset_index(drop=True)

    df_orginized_step1 = pd.DataFrame(
        {
        'filepath':input_filepath
        ,'filename':filename
        }
        )
    # step2 apply map_filename_to_lang function to the filename column
    # df_orginized_step1['language'] = df_orginized_step1['filename'].parallel_apply(map_filename_func)
    df_orginized_step1['language'] = df_orginized_step1.apply(
        lambda row: map_filename_func(row['filename'])
        , axis=1)
    df_orginized_step2 = pd.merge(df_orginized_step1, folder_mapping, on='language', how='left')
    # raise error when there's a na in output_folder_path, also indicate which folder needs to be created
    if df_orginized_step2['output_folder_path'].isna().any():
        na_folders = list(df_orginized_step2[df_orginized_step2['output_folder_path'].isna()]['language'].unique())
        raise ValueError(f"The following folders need to be created: {na_folders}")


    copy_file_df(
        input_file_path=df_orginized_step2['filepath']
        ,output_folder_path=df_orginized_step2['output_folder_path']
        ,filename=df_orginized_step2['filename']
        ,progress_bar=True
    )

def copy_file_df(
    input_file_path: pd.Series,
    output_folder_path: pd.Series,
    filename: pd.Series | None = None,
    progress_bar: bool = True
) -> None:
    """
    Copy files from source paths to destination folders.
    
    Parameters
    ----------
    input_file_path : pd.Series
        Series of source file paths.
    output_folder_path : pd.Series
        Series of destination folder paths.
    filename : pd.Series | None, optional
        Series of filenames for display in progress bar. If None, uses source filenames.
    progress_bar : bool, optional
        Whether to show progress bar. Default is True.
    """

    # medium tested via main_orginizer

    import shutil
    from tqdm.auto import tqdm
    from pathlib import Path

    if len(input_file_path) != len(output_folder_path):
        raise ValueError("input_file_path and output_folder_path must have the same length")
    
    if filename is None:
        filename = input_file_path.apply(lambda x: Path(x).name)
    
    if progress_bar:
        loop_obj = tqdm(
            zip(input_file_path, output_folder_path, filename),
            total=len(input_file_path),
            colour='blue'
        )
    else:
        loop_obj = zip(input_file_path, output_folder_path, filename)
    
    for filepath, output_folder, fname in loop_obj:
        if progress_bar:
            loop_obj.set_description(f"Copying: {fname}")
        
        src = Path(filepath)
        dst_dir = Path(output_folder)
        dst_dir.mkdir(parents=True, exist_ok=True)
        dst = dst_dir / src.name
        shutil.copy2(src, dst)

def make_lang_start_dict():
    lang_dict_lower = vt.make_all_language_dict(key_as="alpha2",value_as="name")  
    lang_dict_upper = dict()
    for key, value in lang_dict_lower.items():
        lang_dict_upper[key.upper()] = value
    lang_dict_upper['PT'] = 'Portuguese_Brazil'
    lang_dict_upper['ES'] = 'Spanish (Latin America)'
    return lang_dict_upper

# move_media_file_bulk
def main_orginizer():
    
    from pandarallel import pandarallel
    import shutil
    from tqdm.auto import tqdm
    from functools import partial

    pandarallel.initialize(progress_bar=True)
    
    input_root_path = r"C:\C_Video_Python\video_toolkit_test\test_move_media_file_bulk\test_01\The Mentalist Season 07 Audio\Amazon_temp"
    output_root_path = r'C:\C_Video_Python\video_toolkit_test\test_move_media_file_bulk\test_01\The Mentalist Season 07 Audio'
    exclude_folder = ['Amazon_temp']
    
    # lang_dict_upper is used inside map_filename_to_lang
    lang_dict_upper = make_lang_start_dict()
    map_filename_to_lang_step2 = partial(map_filename_to_lang, mapping_dict=lang_dict_upper)

    move_file_bulk(
        input_root_path = input_root_path
        ,output_root_path = output_root_path
        ,map_filename_func = map_filename_to_lang_step2
        ,start_mapping_dict = lang_dict_upper
        ,exclude_folder = exclude_folder
    )

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
    





