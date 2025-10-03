# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 16:23:31 2025

@author: Norat
"""

import video_toolkit as vt
from pathlib import Path
from pydub import AudioSegment
import subprocess
import os_toolkit as ost
from tqdm.auto import tqdm
import os


audio_path = r'C:\C_Video_Python\The 100\The 100 Season 01\Season 01 Audio\German'
sub_path = r'C:\C_Video_Python\The 100\The 100 Season 01\Season 01 Subtitle\German Amazon Auto'
output_path = r'C:\C_Video_Python\The 100\The 100 Season 01\Season 01 Splitted Audio\German'

prefix_names: dict[int, list[str]] = {}
# there's an error
season = 1
each_season = []
for episode in range(1,14):
    season_str = str(season).zfill(2)
    episode_str = str(episode).zfill(2)
    each_season.append(f"The_100 DE S{season_str}E{episode_str}")

# there's a bug in split_audio_by_sub, I can't split the audio
# possibly because of empyty text case

# wav vs mp3
# It took about 7 times longer to produce mp3 compared to wav
# But the memory of mp3 is 10 times less than wav

# when use wav it took about 30 sec per episode
vt.split_audio_by_sub(
    media_paths = audio_path
    , sub_paths = sub_path
    , output_folder = output_path
    , prefix_names=each_season
    ,out_audio_ext='wav'
    )


vt.split_audio_by_sub(
    media_paths = audio_path
    , sub_paths = sub_path
    , output_folder = output_path
    , prefix_names=each_season
    ,out_audio_ext='mp3'
    )

vt.srt_to_Excel(srt_path = sub_path, output_path = sub_path)
