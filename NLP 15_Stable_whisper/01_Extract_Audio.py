# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 10:58:29 2024

@author: Heng2020
"""
import video_toolkit as vt
from pathlib import Path
import python_wizard as pw


BigBangFR_06 = Path(r"C:\Users\Heng2020\Downloads\BigBang FR\Saison 6")
output_folder = Path(r"C:\Users\Heng2020\Downloads\BigBang FR\Saison 6\Season 06 Audio")
vt.extract_audio3(video_folder = BigBangFR_06, output_folder = output_folder)
