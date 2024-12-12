# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 09:36:52 2024

@author: Heng2020
"""

import video_toolkit as vt
from typing import Union
import pandas as pd
from pathlib import Path

# vt.merg
bigbang_PT_video_folder = r"C:\C_Video_Python\Merge Language Video\BigBang PT Season 06"
audio_extracted_folder = r"C:\C_Video_Python\Portuguese\BigBang PT\Audio Extracted\Portuguese"
sub_PT_extracted_folder = r"C:\C_Video_Python\Portuguese\BigBang PT\Ori_Subtitle"

# vt.extract_audio(bigbang_PT_video_folder, audio_extracted_folder,languages="Portuguese")
# vt.extract_audio(bigbang_PT_video_folder, audio_extracted_folder,languages="Portuguese")
vt.extract_subtitle(bigbang_PT_video_folder, sub_PT_extracted_folder)

# merge_media_to1video()


def merge_media_to1video(
    input_video_path: Union[str, Path],
    input_info_df:pd.DataFrame,
    output_folder: str,
    output_name: Union[str, Path] = ""
):
    import subprocess
    from pathlib import Path

    video_path = Path(input_video_path)
    output_path = Path(output_folder) / output_name

    command = ['ffmpeg', '-i', str(video_path)]

    for _, row in input_info_df.iterrows():
        command.extend(['-i', str(row['input_media_path'])])

    command.append('-map')
    command.append('0')

    audio_count = 0
    sub_count = 0
    total_media = len(input_info_df)

    # Mapping
    for idx, row in enumerate(input_info_df.itertuples(), start=1):
        if row.media_type == 'audio':
            command.append('-map')
            command.append(f'{idx}:a')
        elif row.media_type == 'subtitle':
            command.append('-map')
            command.append(f'{idx}:s')

    # Metadata
    for row in input_info_df.itertuples():
        lang = row.lang_code_3alpha
        title = row.title
        if row.media_type == 'audio':
            command.extend([f'-metadata:s:a:{audio_count}', f'language={lang}'])
            command.extend([f'-metadata:s:a:{audio_count}', f'title={title}'])
            audio_count += 1
        elif row.media_type == 'subtitle':
            command.extend([f'-metadata:s:s:{sub_count}', f'language={lang}'])
            command.extend([f'-metadata:s:s:{sub_count}', f'title={title}'])
            sub_count += 1

    command.extend(['-c', 'copy', str(output_path)])
    result = subprocess.run(command, text=True, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print("Error encountered:")
        print(result.stderr)
