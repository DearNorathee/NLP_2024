# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 10:22:59 2024

@author: Heng2020
"""
import video_toolkit as vt

from typing import List, Tuple, Literal, Union
from pathlib import Path
import inspect_py as inp
# Sub
import python_wizard as pw


def extract_the_Ark():
    import video_toolkit as vt
    folder_the_Ark = Path(r"H:\D_Video\The Ark Season 01 Portuguese")
    output_folder_PT = r"H:\D_Video\The Ark Season 01 Portuguese\Audio Extracted\Portuguese"
    output_folder_EN = r"H:\D_Video\The Ark Season 01 Portuguese\Audio Extracted\English"
    vt.extract_audio(folder_the_Ark, output_folder_PT,languages="portuguese")
    vt.extract_audio(folder_the_Ark, output_folder_EN,languages="english")
    print("extract_the_Ark")

extract_the_Ark()
