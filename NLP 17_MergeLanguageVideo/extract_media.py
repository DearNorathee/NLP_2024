# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 11:48:32 2024

@author: Heng2020
# """

# Next: create the input_df(all combinations 24 episodes in pd.df)

import video_toolkit as vt
sub_EN_ori_ass_folder = r"C:\C_Video_Python\Merge Language Video\BigBang FR Season 06\English Ori Subtitles\ass"
sub_FR_ori_ass_folder = r"C:\C_Video_Python\Merge Language Video\BigBang FR Season 06\French Ori Subtitles\ass"
FR_video_folder = r"C:\C_Video_Python\Merge Language Video\BigBang FR Season 06"

sub_EN_srt_folder = r"C:\C_Video_Python\Merge Language Video\BigBang FR Season 06\English Ori Subtitles\srt_converted"
sub_FR_srt_folder = r"C:\C_Video_Python\Merge Language Video\BigBang FR Season 06\French Ori Subtitles\srt_converted"

# vt.extract_subtitle(FR_video_folder, output_folder = sub_EN_ori_ass_folder,languages="eng")
# vt.extract_subtitle(FR_video_folder, output_folder = sub_FR_ori_ass_folder,languages="fre")

vt.ass_to_srt(sub_EN_ori_ass_folder,output_folder=sub_EN_srt_folder)
vt.ass_to_srt(sub_FR_ori_ass_folder,output_folder=sub_FR_srt_folder)
# vt.ass_to_df()