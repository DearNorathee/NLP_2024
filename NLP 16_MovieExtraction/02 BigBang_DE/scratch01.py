# -*- coding: utf-8 -*-
"""
Created on Tue Jun  3 10:15:36 2025

@author: Norat
"""

from pathlib import Path
from typing import Type,Union

import py_string_tool as pst
import os_toolkit as ost  
  
import video_toolkit as vt


def test_reset_start_timestamp_1audio():
    input_path01 = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Audio\German\ori_audio\BigBang DE S02E02_DE.mp3"
    vt.reset_start_timestamp_1audio(input_path01,outfilename=None
                                    ,output_folder=r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Audio\German\test_01")

def test_reset_start_timestamp():
    input_path01 = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Audio\German\ori_audio"
    vt.reset_start_timestamp(input_path01
                                    ,output_folder=r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Audio\German")
    
test_reset_start_timestamp()
test_reset_start_timestamp_1audio()
