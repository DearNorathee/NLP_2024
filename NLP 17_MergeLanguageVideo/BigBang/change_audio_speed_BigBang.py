# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 11:46:37 2025

@author: Norat
"""
import video_toolkit as vt
# vt.change_audio_speed_1file(audio_path, speedx, output_name)

# /change_audio_speed_1file still have some errors
def test_change_audio_speed_1file():
    audio_path01 = r"C:\C_Video_Python\video_toolkit_test\change_audio_speed_1file\BigBang season1 French\BigBang FR S01E01_FR.mp3"
    # SPEEDX = 0.9612
    SPEEDX = 0.5
    vt.change_audio_speed_1file(audio_path01,SPEEDX,"BigBang FR S01E01_FR_cs.mp3",print_errors=True)

def change_audio_speed_1file_v2(
        audio_path
        , speedx
        ,output_name
        ,output_folder):
    from pydub import AudioSegment
    from pathlib import Path
    # Load audio file (supports MP3, WAV, etc.)
    # medium tested
    audio = AudioSegment.from_file(audio_path)
    
    # Adjust speed (0.9764x slower)
    slowed_audio = audio._spawn(audio.raw_data, overrides={
        "frame_rate": int(audio.frame_rate * speedx)
    }).set_frame_rate(audio.frame_rate)
    
    filepath = Path(audio_path)
    folder_path = filepath.parent
    filename = filepath.stem
    
    if output_folder == "":
        output_folder_in = folder_path
    else:
        output_folder_in = Path(output_folder)
    output_path = output_folder_in / f"{output_name}"
    # Export slowed audio
    slowed_audio.export(output_path, format="mp3")

def test_change_audio_speed_1file_v2():
    # I use this function to create 1 audio per episode
    audio_path01 = r"C:\C_Video_Python\video_toolkit_test\change_audio_speed_1file\BigBang season1 French\BigBang FR S01E13_FR.mp3"
    output_folder = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 01\Season 01 Audio\French_adj_speed"
    SPEEDX = 0.95903619926980600
    change_audio_speed_1file_v2(audio_path01,SPEEDX,"BigBang FR S01E13_FR_cs_v1.mp3",output_folder = output_folder)
    
test_change_audio_speed_1file_v2()
# test_change_audio_speed_1file()