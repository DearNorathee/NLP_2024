# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 15:25:18 2024

@author: Heng2020
"""
import video_toolkit as vt
import stable_whisper

def export_season_6():
    # as of Aug,10,2024 cuda was still not install correctly, so I'm going to use model from 
    import os
    # make sure that fast_whisper will not throw weird error
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
    
    faster_model_base = stable_whisper.load_faster_whisper('base')
    BigBangFR_S02E01 = r"H:\D_Video\BigBang French\BigBang FR Season 06\Season 06 Audio\French"
    output_folder = r"H:\D_Video\BigBang French\BigBang FR Season 06\Season 06 Audio\French Subtitle"
    
    vt.audio_to_sub(faster_model_base,BigBangFR_S02E01,output_folder = output_folder)
export_season_6()