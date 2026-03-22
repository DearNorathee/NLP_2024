# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 09:57:22 2025

@author: Norat
"""

import video_toolkit as vt
import os_toolkit as ost
from typing import Dict, Literal, Union, List, Callable
from pathlib import Path
import os
from play_audio_file import play_alarm_done, play_alarm_error
import py_string_tool as pst
import pandas as pd

episode = "S06E11"

sub_01_path = fr"C:\C_Video_Python\The Big Bang Theory\The Big Bang Theory Season 06\Season 06 Subtitle\Portuguese Amazon\The Big Bang Theory_{episode}_4_por.srt"
sub_02_path = fr"C:\C_Video_Python\The Big Bang Theory\The Big Bang Theory Season 06\Season 06 Subtitle\English Amazon\The Big Bang Theory_{episode}_15_eng.srt"

sub_01_df = vt.sub_to_df(sub_01_path)
sub_02_df = vt.sub_to_df(sub_02_path)

# select when it's ()
sub_02_df_step2 = sub_02_df.loc[~(sub_02_df['sentence'].str[:1] == "(") |~(sub_02_df['sentence'].str[-1] == ")") ]


