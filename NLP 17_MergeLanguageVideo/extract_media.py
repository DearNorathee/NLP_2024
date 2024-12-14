# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 11:48:32 2024

@author: Heng2020
# """

# Next: convert .ass to .srt (I may need to write a new function)

import video_toolkit as vt
sub_EN_ori_folder = r"C:\C_Video_Python\Merge Language Video\BigBang FR Season 06\English Ori Subtitles"
sub_FR_ori_folder = r"C:\C_Video_Python\Merge Language Video\BigBang FR Season 06\French Ori Subtitles"
FR_video_folder = r"C:\C_Video_Python\Merge Language Video\BigBang FR Season 06"

vt.extract_subtitle(FR_video_folder, output_folder = sub_EN_ori_folder,languages="eng")
vt.extract_subtitle(FR_video_folder, output_folder = sub_FR_ori_folder,languages="fre")

# vt.ass_to_df()