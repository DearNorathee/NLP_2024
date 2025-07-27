# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 11:32:38 2025

@author: Norat
"""

import video_toolkit as vt
from pathlib import Path
from beartype import beartype
from typing import Union, Literal

def test_clean_netflix_srt_1file():
    sub_path = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Subtitle\German Netflix\original\BigBang DE S06E01.srt"
    output_folder = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Subtitle\German Netflix\original_no_speakers"
    vt.clean_Netflix_srt_1file(sub_path, output_folder)

def test_clean_netflix_srt():
    sub_path01 = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Subtitle\German Netflix\original"
    output_folder01 = r"C:\C_Video_Python\video_toolkit_test\test_clean_netflix_srt\test_01"

    sub_path02 = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Subtitle\German Netflix\original\BigBang DE S06E01.srt"
    output_folder02 = r"C:\C_Video_Python\video_toolkit_test\test_clean_netflix_srt\test_02"

    sub_path03 = [
        r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Subtitle\German Netflix\original\BigBang DE S06E01.srt",
        r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Subtitle\German Netflix\original\BigBang DE S06E02.srt",
        r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Subtitle\German Netflix\original\BigBang DE S06E03.srt",
        
        ]
    output_folder03 = r"C:\C_Video_Python\video_toolkit_test\test_clean_netflix_srt\test_03"

    sub_path04 = [
        r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Subtitle\German Netflix\original"
    ]
    output_folder04 = r"C:\C_Video_Python\video_toolkit_test\test_clean_netflix_srt\test_04"

    vt.clean_Netflix_srt(sub_path01, output_folder01)
    vt.clean_Netflix_srt(sub_path02, output_folder02)
    vt.clean_Netflix_srt(sub_path03, output_folder03)
    # list of folders are not yet implemented in inp.handle_multi_input
    # clean_Netflix_srt(sub_path04, output_folder04)  

# test_clean_netflix_srt_1file()
test_clean_netflix_srt()




