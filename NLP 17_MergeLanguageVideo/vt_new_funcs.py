# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 10:34:03 2024

@author: Heng2020
"""
import os_toolkit as ost


import whisper
from whisper.model import Whisper as whisper_model_Whisper
from typing import Any, Dict, List
import pandas as pd

# import whisper.model.Whisper


import video_toolkit as vt
from typing import Union
import pandas as pd
from pathlib import Path
import dataframe_short as ds
# vt.mer
# vt.merge_media_to1video(input_video_path, input_info_df, output_folder,)
def test_merge_media_to1video():
    input_video_path = r"C:\C_Video_Python\Merge Language Video\BigBang PT Season 06\BigBang PT S06E02.mkv"
    output_folder = r"C:\C_Video_Python\Merge Language Video\tests\outputs"
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
    
# test_merge_media_to1video()


def test__create_media_dict_info():
    media_excel_path = r"C:/Users/Heng2020/OneDrive/D_Code/Python/Python NLP/NLP 02/NLP_2024/NLP 17_MergeLanguageVideo/media_info_test1.xlsm"
    media_df1 = ds.read_excel(media_excel_path,sheet_name="1video")
    media_df2 = ds.read_excel(media_excel_path,sheet_name="multi")
    
    actual01 = vt._create_media_dict_info(media_df1)
    actual02 = vt._create_media_dict_info(media_df2)
    print()


    
def test_merge_media_to_video():
    media_excel_path = r"C:/Users/Heng2020/OneDrive/D_Code/Python/Python NLP/NLP 02/NLP_2024/NLP 17_MergeLanguageVideo/media_info_test1.xlsm"
    media_df1 = ds.read_excel(media_excel_path,sheet_name="1video")
    media_df2 = ds.read_excel(media_excel_path,sheet_name="multi")
    
    # merge_media_to_video(media_df1)
    vt.merge_media_to_video(media_df2)
    
# test_merge_media_to_video()
# test_create_media_dict_info()

ass_path = r"C:\C_Video_Python\Merge Language Video\BigBang FR Season 06\English Ori Subtitles\ass"
ass_sub_df = vt.ass_to_df(ass_path)

# ass_sub_df.dtypes
srt_sub_df = vt.srt_to_df(r"H:\D_Video\The Ark Season 01 Portuguese\Whisper base Subtitle PT\The Ark S01E01 PT_PT.srt")
# srt_sub_df.dtypes


def df_to_srt(df: pd.DataFrame, output_name: str, output_folder: Union[str, Path] = "") -> None:
    """
    Converts a DataFrame with subtitle data into an SRT file.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the subtitles with columns: "sentence", "start", "end".
    output_name : str
        The name of the output SRT file (e.g., "subtitles.srt").
    output_folder : str or Path, optional
        The folder where the SRT file will be saved. Defaults to the current directory.

    Returns
    -------
    None
    """
    # medium tested
    
    # Ensure output folder is a Path object
    output_folder = Path(output_folder)
    output_path = output_folder / output_name
    
    df_in = df.copy()
    # Write the SRT file
    with open(output_path, 'w', encoding='utf-8') as f:
        df_in['start'] = df_in['start'].astype(str)
        df_in['end'] = df_in['end'].astype(str)
        for index, row in df_in.iterrows():
            # Write subtitle index
            f.write(f"{index + 1}\n")

            # Format and write time stamps
            start_time = row['start'].replace('.', ',')[:-3]
            end_time = row['end'].replace('.', ',')[:-3]
            f.write(f"{start_time} --> {end_time}\n")

            # Write the subtitle sentence
            f.write(f"{row['sentence']}\n\n")

df_to_srt(ass_sub_df[0],"BigBang FR S06E01_EN.srt",r"C:\C_Video_Python\Merge Language Video\BigBang FR Season 06\English Ori Subtitles\srt_converted")

df_to_srt(ass_sub_df[0],"BigBang FR S06E01_EN.srt",Path(r"C:\C_Video_Python\Merge Language Video\BigBang FR Season 06\English Ori Subtitles\srt_converted"))


    