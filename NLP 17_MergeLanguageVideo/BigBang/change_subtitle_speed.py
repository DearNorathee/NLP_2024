# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 10:50:32 2025

@author: Norat
"""

import os_toolkit as ost
from pprint import pprint
import shutil
from tqdm import tqdm
import video_toolkit as vt
from pathlib import Path
import pandas as pd


def change_subtitle_sppeed_1file(sub_file):
    df_sub = vt.sub_to_df(sub_file)
    pass

def test_change_subtitle_sppeed_1file():
    sub_path01 = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Subtitle\French_whisper_base\BigBang FR S02E01_FR.srt"
    df_sub_modified = change_subtitle_sppeed_1file(sub_path01)


change_subtitle_sppeed_1file()