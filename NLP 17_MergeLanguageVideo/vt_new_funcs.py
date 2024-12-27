# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 10:34:03 2024

@author: Heng2020
"""


import os_toolkit as ost

# import whisper
# from whisper.model import Whisper as whisper_model_Whisper
from typing import Any, Dict, List,Union
import pandas as pd

# import whisper.model.Whisper


import video_toolkit as vt
from typing import Union
import pandas as pd
from pathlib import Path
import dataframe_short as ds
from beartype import beartype
# vt.mer
# vt.merge_media_to1video(input_video_path, input_info_df, output_folder,)

def create_media_info_df(
    input_video_folder:str|Path    
    ,ep_seasons: list[str]| str
    ,media_types: list[str]
    ,input_media_folders: list[str]
    ,input_filname_patterns: list[str]
    ,titles: list[str]
    ,lang_code_3chrs: list[str]
    ,output_folder:str
    ) -> pd.DataFrame:
    """
    helper function to create media_info combinations(pd.df) to feed in to merge_media_to_video
    """
    def _replace_with_filename(patterns:list[str],new:str, old:str = "<>") -> List[str]:
        result: List[str] = patterns.copy()
        for i, x in enumerate(patterns):
            x_new = x.replace(old,new)
            result[i] = x_new
        return result

    lengths: List[int] = [len(media_types), len(input_media_folders), len(input_filname_patterns), len(titles), len(lang_code_3chrs)]
    if len(set(lengths)) > 1:
        raise ValueError(f"All input lists must have the same length, but got lengths: {lengths}")

    media_per_ep = len(media_types)
    out_df = pd.DataFrame()

    for i, ep_season_text in enumerate(ep_seasons):
        input_filenames = _replace_with_filename(input_filname_patterns,ep_season_text)
        
        input_media_paths = []
        for i, filename in input_filenames:
            input_media_paths.append(input_media_folders[i] + "/" + filename)
        
        output_folder_rep = [output_folder]*media_per_ep
        df_curr_ep = pd.DataFrame({
            'media_type': media_types,
            'title': titles,
            'lang_code_3alpha': lang_code_3chrs,
            'output_folder': output_folder_rep,
            'input_media_path':input_media_paths,
            'output_name': 'test'
            
        })
        out_df = pd.concat([out_df,df_curr_ep])
    return out_df


def test_merge_media_to1video():
    input_video_path = r"C:\C_Video_Python\Merge Language Video\BigBang PT Season 06\BigBang PT S06E02.mkv"
    output_folder = r"C:\C_Video_Python\Merge Language Video\tests\outputs\test_merge_media_to1video\test_01"
    output_name = "BigBang All S06E02_v02.mkv"
    
    info_df = pd.DataFrame({
        'media_type': ['subtitle','audio','subtitle'],
        'input_media_path': [
            r'C:\C_Video_Python\Merge Language Video\BigBang PT Season 06\BigBang PT S06E02.srt',
            r'C:\C_Video_Python\Merge Language Video\BigBang FR Season 06\Season 06 Audio\BigBang FR S06E02_FR.mp3',
            r'C:\C_Video_Python\Merge Language Video\BigBang FR Season 06\Season 06 Audio\French Subtitle\BigBang FR S06E02_FR.srt',
            ],
        'title': ['Portuguese_Brazilian_whisper','French','French_whisper'],
        'lang_code_3alpha': ['por','fre','fre']
        
        })
    
    vt.merge_media_to1video(input_video_path,info_df,output_folder,output_name)
    


def test_merge_media_to_video():
    media_excel_path = r"C:/Users/Heng2020/OneDrive/D_Code/Python/Python NLP/NLP 02/NLP_2024/NLP 17_MergeLanguageVideo/media_info_test1.xlsm"
    media_df1 = ds.read_excel(media_excel_path,sheet_name="1video")
    media_df2 = ds.read_excel(media_excel_path,sheet_name="multi")
    
    # merge_media_to_video(media_df1)
    vt.merge_media_to_video(media_df2)

def test_ass_to_srt_1file():
    srt_path01 = r"C:\C_Video_Python\Merge Language Video\BigBang FR Season 06\English Ori Subtitles\ass\BigBang FR S06E01_EN.ass"
    srt_path01_Path = Path(r"C:\C_Video_Python\Merge Language Video\BigBang FR Season 06\English Ori Subtitles\ass\BigBang FR S06E01_EN.ass")
    output_folder_01 = r"C:\C_Video_Python\Merge Language Video\tests\outputs\test_ass_to_srt_1file\test_01"
    output_folder_01_Path = Path(r"C:\C_Video_Python\Merge Language Video\tests\outputs\test_ass_to_srt_1file\test_01")
    
    # ass_to_srt_1file(srt_path01,output_folder_01)
    vt.ass_to_srt_1file(srt_path01_Path,output_folder_01_Path)

def test_ass_to_srt() -> None:
    srt_paths_01 = r"C:\C_Video_Python\Merge Language Video\BigBang FR Season 06\English Ori Subtitles\ass"
    srt_paths_02_Path = Path(r"C:\C_Video_Python\Merge Language Video\BigBang FR Season 06\English Ori Subtitles\ass")
    
    srt_paths_03 = [
        r"C:\C_Video_Python\Merge Language Video\BigBang FR Season 06\English Ori Subtitles\ass\BigBang FR S06E01_EN.ass"
        ,r"C:\C_Video_Python\Merge Language Video\BigBang FR Season 06\English Ori Subtitles\ass\BigBang FR S06E10_EN.ass"
        ,Path(r"C:\C_Video_Python\Merge Language Video\BigBang FR Season 06\English Ori Subtitles\ass\BigBang FR S06E10_EN.ass")
        ,Path(r"C:\C_Video_Python\Merge Language Video\BigBang FR Season 06\English Ori Subtitles\ass\BigBang FR S06E23_EN.ass")
        ]
    
    output_folder_01 = r"C:\C_Video_Python\Merge Language Video\tests\outputs\test_ass_to_srt\test_01"
    
    output_folder_02 = Path(r"C:\C_Video_Python\Merge Language Video\tests\outputs\test_ass_to_srt\test_02_Path")
    output_folder_03 = r"C:\C_Video_Python\Merge Language Video\tests\outputs\test_ass_to_srt\test_03_List"
    
    ost.delete_files_in_folder(output_folder_01)
    ost.delete_files_in_folder(output_folder_02)
    ost.delete_files_in_folder(output_folder_03)
    
    vt.ass_to_srt(srt_paths = srt_paths_01, output_folder = output_folder_01)
    vt.ass_to_srt(srt_paths = srt_paths_02_Path, output_folder = output_folder_02)
    vt.ass_to_srt(srt_paths = srt_paths_03, output_folder = output_folder_03)
    
def test_create_media_info_df():
    input_video_folder:str|Path = r"C:\C_Video_Python\Merge Language Video\BigBang PT Season 06"
    ep_seasons: list[str]| str = ["S06E01","S06E02","S06E03"]
    media_types: list[str] = ["subtitle","audio","subtitle","subtitle"]
    input_media_folders: list[str] = [r"C:\C_Video_Python\Merge Language Video\BigBang PT Season 06",
                                    r"C:\C_Video_Python\Merge Language Video\BigBang FR Season 06\Season 06 Audio",
                                    r"C:\C_Video_Python\Merge Language Video\BigBang FR Season 06\French Ori Subtitles\srt_converted",
                                    r"C:\C_Video_Python\Merge Language Video\BigBang FR Season 06\English Ori Subtitles\srt_converted"
                                      ]
    titles: list[str] = ["Portuguese_Brazilian_whisper","French","French_whisper","English_ori"]
    lang_code_3chrs: list[str] = ["por","fre","fre","eng"]
    output_folder:str = r"C:\C_Video_Python\Merge Language Video\tests\outputs\test_create_media_info_df\test_01"

    # use <> to represent the ep_seasons text
    # 
    input_filname_patterns: list[str] = ["BigBang PT <>.srt","BigBang FR <>_FR.mp3","BigBang FR <>_FR.srt","BigBang FR <>_EN.srt"]
    
    actual01 = create_media_info_df(
        input_video_folder =  input_video_folder
        ,ep_seasons = ep_seasons
        ,media_types = media_types
        ,input_media_folders = input_media_folders
        ,input_filname_patterns = input_filname_patterns
        ,titles = titles
        ,lang_code_3chrs = lang_code_3chrs
        ,output_folder = output_folder)
    print()

# it seems like subtitle(ENG) in S06E19 is slightly behind the audio(after minute 12)
# test_ass_to_srt_1file()
test_create_media_info_df()
test_ass_to_srt_1file()
test_ass_to_srt()
# vt.ass_to_srt(srt_paths, output_folder)










    