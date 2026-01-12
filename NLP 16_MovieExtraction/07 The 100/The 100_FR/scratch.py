# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 10:57:56 2025

@author: Norat
"""

import whisper
import os
import os_toolkit as ost

whisper.__version__
whisper.available_models()
small = whisper.load_model('small')
medium = whisper.load_model('medium')
large_v3 = whisper.load_model('large-v3')
import stable_whisper
stable_whisper.__version__
import video_toolkit as vt

medium = stable_whisper.load_faster_whisper('medium', device='cuda')
large_v3 = stable_whisper.load_faster_whisper('large-v3')

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# took about  for 20 min of audio
vt.audio_to_sub(
    audio_paths = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Audio\German Amazon\The Big Bang Theory_S06E01_0_DE.mp3",
    output_folder = r"C:\C_Video_Python\video_toolkit_test\test_audio_to_sub",
    model = medium,
    progress_bar=True
)


vt.audio_to_sub(
    audio_paths = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Audio\German Amazon\The Big Bang Theory_S06E01_0_DE.mp3",
    output_folder = r"C:\C_Video_Python\video_toolkit_test\test_audio_to_sub",
    model = large_v3,
    progress_bar=True
)
sub_01 = vt.sub_to_df(r"C:\C_Video_Python\video_toolkit_test\test_audio_to_sub\The Big Bang Theory_S06E01_DE_assembly_AI.srt")
sub_02 = vt.sub_to_df(r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Subtitle\German Amazon\The Big Bang Theory_S06E01_13_deu.srt")


