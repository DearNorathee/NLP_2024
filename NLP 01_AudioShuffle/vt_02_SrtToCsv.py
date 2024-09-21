
import pysrt
import pandas as pd
import os
from pydub import AudioSegment
from time import time
from playsound import playsound
from packaging import version
import video_toolkit as vt
# Parse the SRT subtitle file

# srt_path = r"H:\D_Video\Westworld Portugues 04\Eng Sub\Westworld.S04E01 EngSub 02.srt"
# sub_output_name = 'Westworld_S04E01_EN02.xlsx'

srt_folder_path = r"H:\D_Video\The Ark Season 01 Portuguese\Subtitles\srt"
output_folder = r"H:\D_Video\The Ark Season 01 Portuguese\Subtitles\Excel generated"

alarm_path = r"H:\D_Music\Sound Effect positive-logo-opener.wav"

vt.srt_to_Excel(srt_folder_path,output_folder)

# df = srt_to_df(srt_path)
# df_list = srt_to_df(srt_folder_path)
# print(df_list[3].head())
# string_list = df['sentence'].tolist()
# test_str3 = string_list[24]

# test_str = string_list[240]
# test_str2 = "corrected byFOLLOW US: <font color=""#ff0000"">@LIO_OFFICIAL</font>"
# clean_str = clean_subtitle(test_str3)

# clean_list = list(map(clean_subtitle,string_list))


