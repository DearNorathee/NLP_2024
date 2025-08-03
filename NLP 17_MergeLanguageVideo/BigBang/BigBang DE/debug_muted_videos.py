# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 09:44:06 2025

@author: Norat
"""
import os_toolkit as ost
from pprint import pprint
import shutil
from tqdm import tqdm
import video_toolkit as vt
from pathlib import Path
import pandas as pd
import dataframe_short as ds

# season 9 seems to have no audio at all

media_path:str = r"C:/Users/Norat/OneDrive/D_Code/Python/Python NLP/NLP 02/NLP_2024/NLP 17_MergeLanguageVideo/BigBang/BigBang DE/BigBang PT Season 09_media info.xlsx"

media_info_df_season = ds.read_excel(media_path)


episode_1_media_info = media_info_df_season.loc[media_info_df_season['input_video_name'].isin(["BigBang PT S09E01.mkv"])]

episode_1_media_info.loc[:,'input_media_path'] = r"C:\C_Video_Python\Merge Language Video\BigBang Merged\BigBang Season 09\test_02"
vt.merge_media_to_video(episode_1_media_info)
