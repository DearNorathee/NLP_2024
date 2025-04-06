# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 11:46:37 2025

@author: Norat
"""
import video_toolkit as vt


# /change_audio_speed_1file still have some errors
def test_change_audio_speed_1file():
    audio_path01 = r"C:\C_Video_Python\video_toolkit_test\change_audio_speed_1file\BigBang season1 French\BigBang FR S01E01_FR.mp3"
    # SPEEDX = 0.9612
    SPEEDX = 0.5
    vt.change_audio_speed_1file(audio_path01,SPEEDX,"BigBang FR S01E01_FR_cs.mp3",print_errors=True)

test_change_audio_speed_1file()