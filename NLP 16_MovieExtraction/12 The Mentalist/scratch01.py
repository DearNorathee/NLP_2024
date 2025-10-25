# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 09:55:03 2025

@author: Norat
"""
import video_toolkit as vt


df_sub_01 = vt.sub_to_df(
    r"C:\C_Video_Python\The Mentalist\The Mentalist Season 07\Season 07 Subtitle\French CC\The Mentalist_S07E06_20_fra.srt"
    )
vt.srt_to_Excel(srt_path = r'C:\C_Video_Python\The Mentalist\The Mentalist Season 07\Season 07 Subtitle\French CC'
                , output_path = r'C:\Users\Norat\OneDrive\D_Documents\_Learn Languages\French\Series subtitles\The Mentalist')

df_sub_02 = vt.sub_to_df(
    r"C:\C_Video_Python\The Mentalist\The Mentalist Season 07\Season 07 Subtitle\English\The Mentalist_S07E13_26_eng.srt"
    )

vt.extract_subtitle(filepaths = r"D:\D_Videos\Netflix Series\3 Body Problem\S01\3 Body Problem_S01E03_Destroyer of Worlds.mkv"
                    , output_folder = r"C:\C_Video_Python\3 Body Problem")