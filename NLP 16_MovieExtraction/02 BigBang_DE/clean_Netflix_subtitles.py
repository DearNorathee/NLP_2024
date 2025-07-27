# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 11:32:38 2025

@author: Norat
"""

import video_toolkit as vt
from pathlib import Path
from beartype import beartype
from typing import Union, Literal


@beartype
def clean_Netflix_srt_1file(
    sub_path:str|Path
    ,output_folder:str|Path ) -> None:

    """
    Clean Netflix-style speaker labels from an SRT subtitle file.

    This function processes a single `.srt` subtitle file by removing speaker name prefixes 
    commonly found in Netflix subtitles (e.g., "JOHN:", "(MAN):"). The cleaned subtitles are 
    saved in a new file with the same filename in the specified output folder.

    Parameters
    ----------
    sub_path : str or Path
        Path to the input `.srt` subtitle file.

    output_folder : str or Path
        Folder where the cleaned subtitle file will be saved.

    Returns
    -------
    None
        A new `.srt` file is saved in `output_folder`, containing cleaned subtitle sentences.

    Notes
    -----
    - Only speaker prefixes in uppercase or enclosed in parentheses followed by a colon (e.g., "JOHN:", "(WOMAN):") are removed.
    - The original sentence is stored in the `sentence_ori` column, and the speaker prefix (if detected) is stored in `speaker_prefix`.
    - The final output subtitle contains only the cleaned `sentence`, `start`, and `end` fields.

    Examples
    --------
    Clean a Netflix-style subtitle file and output the result:
    >>> clean_netflix_srt_1file("episode1.srt", "cleaned_subs/")
    """


    # medium tested
    df_sub_ori = vt.sub_to_df(sub_path)
    df_sub_copy_step1 = df_sub_ori.copy()

    PATTERN = r'^((?:\([A-Z\' ]+\)|[A-Z\']+):\s)'

    df_sub_copy_step1['sentence_ori'] = df_sub_copy_step1['sentence'].copy()
    # extract into a new column; missing ones become NaN
    df_sub_copy_step1['speaker_prefix'] = df_sub_copy_step1['sentence'].str.extract(PATTERN)
    df_sub_copy_step1['sentence'] = df_sub_copy_step1['sentence_ori'].str.replace(PATTERN, '', regex=True)

    df_sub_copy_step2 = df_sub_copy_step1[['sentence','start','end']]

    # out_sub_path = Path(output_folder) / Path(sub_path).name
    vt.df_to_srt(df_sub_copy_step2
                ,output_name=Path(sub_path).name
                ,output_folder=output_folder)

def clean_Netflix_srt(
    filepaths: Union[str, Path, list[str|Path]]
    ,output_folder: str|Path
    # input below would get import automatically
    ,replace: bool = True
    ,errors:Literal["warn","raise"] = "raise"
    ,print_errors:bool = False

    # handle_multi_input parameters
    ,progress_bar: bool = True
    ,verbose: int = 0
    ,alarm_done: bool = False
    ,alarm_error: bool = False
    ,input_extension: str|None = vt.SUBTITLE_ALL_EXTENSIONS
    ):
    
    import inspect_py as inp
    path_input = {
        "filepaths":filepaths
        ,"output_folder":output_folder
    }
    handle_multi_input_params = {
        "progress_bar": progress_bar
        ,"verbose":verbose
        ,"alarm_done":alarm_done
        ,"alarm_error":alarm_error
        ,"input_extension":input_extension
    }
    func_temp = inp.handle_multi_input(**handle_multi_input_params)(clean_Netflix_srt_1file)
    result = func_temp(**path_input)
    return result

def test_clean_netflix_srt_1file():
    sub_path = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Subtitle\German Netflix\original\BigBang DE S06E01.srt"
    output_folder = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Subtitle\German Netflix\original_no_speakers"
    clean_Netflix_srt_1file(sub_path, output_folder)

def test_clean_netflix_srt():
    sub_path01 = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Subtitle\German Netflix\original"
    output_folder01 = r"C:\C_Video_Python\video_toolkit_test\test_clean_netflix_srt\test_01"

    sub_path02 = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Subtitle\German Netflix\original\BigBang DE S06E01.srt"
    output_folder02 = r"C:\C_Video_Python\video_toolkit_test\test_clean_netflix_srt\test_02"

    sub_path03 = [
        r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Subtitle\German Netflix\original\BigBang DE S06E01.srt",
        r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Subtitle\German Netflix\original\BigBang DE S06E02.srt",
        r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Subtitle\German Netflix\original\BigBang DE S06E03.srt",
        
        ]
    output_folder03 = r"C:\C_Video_Python\video_toolkit_test\test_clean_netflix_srt\test_03"

    sub_path04 = [
        r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 06\Season 06 Subtitle\German Netflix\original"
    ]
    output_folder04 = r"C:\C_Video_Python\video_toolkit_test\test_clean_netflix_srt\test_04"

    clean_Netflix_srt(sub_path01, output_folder01)
    clean_Netflix_srt(sub_path02, output_folder02)
    clean_Netflix_srt(sub_path03, output_folder03)
    # list of folders are not yet implemented in inp.handle_multi_input
    # clean_Netflix_srt(sub_path04, output_folder04)  

# test_clean_netflix_srt_1file()
test_clean_netflix_srt()




