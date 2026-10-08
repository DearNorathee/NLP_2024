# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 13:15:12 2024

@author: Heng2020
"""
#%%
import video_toolkit as vt
import modeling_tool as mlt
# mlt.check_gpu()
srt_path_folder = r"H:\D_Video\BigBang French\BigBang FR Season 06\Season 06 Audio\French Subtitle"
output_path = r"H:\D_Video\BigBang French\BigBang FR Season 06\Season 06 Audio\Excel Extracted"


# vt.srt_to_Excel(srt_path = srt_path_folder, output_path = output_path)

#%%
srt_path = r"C:\C_Video_Python\The Big Bang Theory\The Big Bang Theory Season 06\Season 06 Subtitle\French CC Amazon\The Big Bang Theory_S06E04_8_fra.srt"
df = vt.srt_to_df(srt_path)
df.to_clipboard()

# %%
