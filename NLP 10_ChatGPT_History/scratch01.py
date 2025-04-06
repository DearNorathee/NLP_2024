# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 10:34:01 2024

@author: Heng2020
"""
import pandas as pd
import video_toolkit as vt

fr_sub_path = r"H:\H_Video_Python\Learn French\100 questions et réponses en français A1 à C1\100 questions et réponses en français (A1 à C1)_FR.srt"
output_folder = r"H:\H_Video_Python\Learn French\100 questions et réponses en français A1 à C1\French_Youtube_Subtitle_st.xlsx"

vt.srt_to_Excel(srt_path = fr_sub_path, output_path = output_folder)
