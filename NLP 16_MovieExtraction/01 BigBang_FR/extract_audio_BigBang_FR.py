# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 09:51:16 2024

@author: Heng2020
"""
# objective of this script is to extract audio from video in BigBang FR for all seasons

import video_toolkit as vt
import os_toolkit as ost
from typing import Dict, Literal, Union, List
from pathlib import Path
import os
import shutil

big_bang_FR: Dict[int, Union[str,Path]] = {}
big_bang_audio_folder_FR: Dict[int, Union[str,Path]] = {}
# "H:\D_Video\BigBang French\BigBang FR Season 01\Season 01 Audio"
# "H:\D_Video\BigBang French\BigBang FR Season 02"

# "H:\D_Video\BigBang French\BigBang FR Season 02\Season 02 Audio"
# "H:\D_Video\BigBang French\BigBang FR Season 02"

# "H:\D_Video\BigBang French\BigBang FR Season 03"
# "H:\D_Video\BigBang French\BigBang FR Season 02\Season 02 Audio"


# assuming all season have the same folder structure:
for season in range(1,12):
    season_str = str(season).zfill(2)
    big_bang_FR[season] = fr"H:\D_Video\BigBang French\BigBang FR Season {season_str}"
    big_bang_audio_folder_FR[season] = fr"H:\D_Video\BigBang French\BigBang FR Season {season_str}\Season {season_str} Audio"

skip_season = [2]

for season, audio_folder in big_bang_audio_folder_FR.items():
    french_folder = Path(audio_folder) / "French"
    english_folder = Path(audio_folder) / "English"
    if season not in skip_season:
        if os.path.exists(audio_folder):
            if not os.path.exists(french_folder):
                os.makedirs(french_folder, exist_ok=True)
                vt.extract_audio3(
                    video_folder=big_bang_FR[season],
                    output_folder=french_folder,
                    languages= ["French"]
                    )
            if not os.path.exists(english_folder):
                os.makedirs(english_folder, exist_ok=True)
                vt.extract_audio3(
                    video_folder=big_bang_FR[season],
                    output_folder=english_folder,
                    languages= ["English"]
                    )
        else:
            print(f"{audio_folder} does not exist")

