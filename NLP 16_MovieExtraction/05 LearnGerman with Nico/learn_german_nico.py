# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 10:16:23 2025

@author: Heng2020
"""

import video_toolkit as vt
import os_toolkit as ost
import python_wizard as pw
import pandas as pd

print(pd.__version__)
############################################ split_audio_by_sub ###################################################
media_paths = [
    r"G:\My Drive\G_Videos\Learn German\Learn German with Nico\Learn German with Nico_A1.mp4",
    r"G:\My Drive\G_Videos\Learn German\Learn German with Nico\Learn German with Nico_A2.mp4",
    r"G:\My Drive\G_Videos\Learn German\Learn German with Nico\Learn German with Nico_B1.mp4",
    ]
sub_paths = [
    r"G:\My Drive\G_Videos\Learn German\Learn German with Nico\Learn German with Nico_A1_DE.srt",
    r"G:\My Drive\G_Videos\Learn German\Learn German with Nico\Learn German with Nico_A2_DE.srt",
    r"G:\My Drive\G_Videos\Learn German\Learn German with Nico\Learn German with Nico_B1_DE.srt",
    ]

prefix_names = [
    'GermanNico_A1',
    'GermanNico_A2',
    'GermanNico_B1',
    ]
output_folder = r"C:\C_Video_Python\Learn German\Learn German with Nico\Splitted Audio"
sub_paths = r"C:\C_Video_Python\Learn German\Learn German with Nico\Subtitles"

# vt.split_audio_by_sub(media_paths, sub_paths, output_folder,prefix_names=prefix_names)

audio_size = ost.filesize_in_folder(output_folder)

# vt.srt_to_Excel(srt_path, output_path)
# I could run below line in VSCode, but not in Spyder
vt.srt_to_Excel(srt_path = sub_paths, output_path = sub_paths)


