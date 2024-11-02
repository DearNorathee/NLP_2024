# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 15:25:18 2024

@author: Heng2020
"""

import video_toolkit as vt
import stable_whisper

def export_season_05():
    # as of Aug,10,2024 cuda was still not install correctly, so I'm going to use model from 
    import os
    # make sure that fast_whisper will not throw weird error
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
    
    faster_model_base = stable_whisper.load_faster_whisper('base')
    BigBangFR = r"H:\D_Video\BigBang French\BigBang FR Season 05\Season 05 Audio\French"
    output_folder = r"H:\D_Video\BigBang French\BigBang FR Season 05\Season 05 Audio\French Subtitle_base"
    
    vt.audio_to_sub(faster_model_base,BigBangFR,output_folder = output_folder)

def export_season_07():
    # as of Aug,10,2024 cuda was still not install correctly, so I'm going to use model from 
    import os
    # make sure that fast_whisper will not throw weird error
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
    
    faster_model_base = stable_whisper.load_faster_whisper('base')
    BigBangFR = r"H:\D_Video\BigBang French\BigBang FR Season 07\Season 07 Audio\French"
    output_folder = r"H:\D_Video\BigBang French\BigBang FR Season 07\Season 07 Audio\French Subtitle_base"
    
    vt.audio_to_sub(faster_model_base,BigBangFR,output_folder = output_folder)

def export_season_08():
    # as of Aug,10,2024 cuda was still not install correctly, so I'm going to use model from 
    import os
    # make sure that fast_whisper will not throw weird error
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
    
    faster_model_base = stable_whisper.load_faster_whisper('base')
    BigBangFR = r"H:\D_Video\BigBang French\BigBang FR Season 08\Season 08 Audio\French"
    output_folder = r"H:\D_Video\BigBang French\BigBang FR Season 08\Season 08 Audio\French Subtitle_base"
    
    vt.audio_to_sub(faster_model_base,BigBangFR,output_folder = output_folder)

def export_season_09():
    # as of Aug,10,2024 cuda was still not install correctly, so I'm going to use model from 
    import os
    # make sure that fast_whisper will not throw weird error
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
    
    faster_model_base = stable_whisper.load_faster_whisper('base')
    BigBangFR = r"H:\D_Video\BigBang French\BigBang FR Season 09\Season 09 Audio\French"
    output_folder = r"H:\D_Video\BigBang French\BigBang FR Season 09\Season 09 Audio\French Subtitle_base"
    
    vt.audio_to_sub(faster_model_base,BigBangFR,output_folder = output_folder)

def export_season_10():
    # as of Aug,10,2024 cuda was still not install correctly, so I'm going to use model from 
    import os
    # make sure that fast_whisper will not throw weird error
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
    
    faster_model_base = stable_whisper.load_faster_whisper('base')
    BigBangFR = r"H:\D_Video\BigBang French\BigBang FR Season 10\Season 10 Audio\French"
    output_folder = r"H:\D_Video\BigBang French\BigBang FR Season 10\Season 10 Audio\French Subtitle_base"
    
    vt.audio_to_sub(faster_model_base,BigBangFR,output_folder = output_folder)


def export_season_11():
    # as of Aug,10,2024 cuda was still not install correctly, so I'm going to use model from 
    import os
    # make sure that fast_whisper will not throw weird error
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
    
    faster_model_base = stable_whisper.load_faster_whisper('base')
    BigBangFR = r"H:\D_Video\BigBang French\BigBang FR Season 11\Season 11 Audio\French"
    output_folder = r"H:\D_Video\BigBang French\BigBang FR Season 11\Season 11 Audio\French Subtitle_base"
    
    vt.audio_to_sub(faster_model_base,BigBangFR,output_folder = output_folder)

# export_season_11()
# export_season_10()
# export_season_09()
# export_season_08()
# export_season_05()
export_season_07()
export_season_08()
