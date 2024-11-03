# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 13:15:12 2024

@author: Heng2020
"""
import video_toolkit as vt
import modeling_tool as mlt
mlt.check_gpu()
srt_path_folder = "H:\D_Video\BigBang French\BigBang FR Season 06\Season 06 Audio\French Subtitle"
output_path = "H:\D_Video\BigBang French\BigBang FR Season 06\Season 06 Audio\Excel Extracted"
vt.srt_to_Excel(srt_path = srt_path_folder, output_path = output_path)
