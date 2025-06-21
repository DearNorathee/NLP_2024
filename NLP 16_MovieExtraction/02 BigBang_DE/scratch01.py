# -*- coding: utf-8 -*-
"""
Created on Tue Jun  3 10:15:36 2025

@author: Norat
"""

from pathlib import Path
from typing import Type,Union, Optional

import py_string_tool as pst
import os_toolkit as ost  
  
import video_toolkit as vt
import inspect_py as inp



def test_cut_front():
    audio01 = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Audio\German\ori_audio"
    output_folder01 = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Audio\German\cut_front_1_sec"
    vt.cut_front(audio01,1,output_folder01)

test_cut_front()
    