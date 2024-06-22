# -*- coding: utf-8 -*-
"""
Created on Sat May 11 10:07:29 2024

@author: Heng2020
"""

import video_toolkit as vt
from typing import List, Tuple, Literal, Union
from pathlib import Path
import inspect_py as inp
# Sub
import python_wizard as pw

def test_extract_audio_1file():
    folder_FR_bigbang = Path(r"H:\D_Download\Video 01\[ Torrent911.io ] The.Big.Bang.Theory.2007-2019.Integrale.Multi.WEB-DL.1080p.AVC-Ducks\Saison 6")
    chosen_video_name = "The Big Bang Theory_S06E01.mkv"
    chosen_video_path = folder_FR_bigbang / chosen_video_name
    alarm_done_path = r"H:\D_Music\Sound Effect positive-logo-opener.mp3"
    
    output_folder01 = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 01\OutputData\extract_audio_1file\test_01_all"
    output_folder02 = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 01\OutputData\extract_audio_1file\test_02_only_French"
    output_folder03 = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 01\OutputData\extract_audio_1file\test_03_Matrix_some_misspelled"
    output_name = "BigBang_FR_S06E01"
    
    
    
    matrix_video_path = r"G:/My Drive/G_Videos/Polyglot/The Matrix Resurrections 2021.mkv"
    # extract_audio_1file(video_path = chosen_video_path,
    #                     output_folder = output_folder01,
    #                     output_name = output_name,
    #                     alarm_done_path = alarm_done_path)
    
    # extract_audio_1file(video_path = chosen_video_path,
    #                     output_folder = output_folder02,
    #                     alarm_done_path = alarm_done_path,
    #                     languages="french"
    #                     )
    
    vt.extract_audio_1file(video_path = matrix_video_path,
                        output_folder = output_folder03,
                        play_alarm = alarm_done_path,
                        languages=["french","portugus","spanish","englih"]
                        )

def test_extract_audio3():
    import video_toolkit as vt
    folder_FR_bigbang = Path(r"H:\D_Download\Video 01\[ Torrent911.io ] The.Big.Bang.Theory.2007-2019.Integrale.Multi.WEB-DL.1080p.AVC-Ducks\Saison 6")
    output_folder01 = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 01\OutputData\extract_audio3\test_01"
    vt.extract_audio3(folder_FR_bigbang, output_folder01)
    print("test_extract_audio3")
def test_input_params():
    actual01 = inp.input_params(vt.extract_audio_1file)
    print("test_input_params Pass!!")
def main():
    test_extract_audio3()
    test_input_params()
    test_extract_audio_1file()

if __name__ == "__main__":
    main()
    