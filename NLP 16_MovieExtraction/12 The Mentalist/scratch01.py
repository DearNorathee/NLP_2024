# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 09:55:03 2025

@author: Norat
"""
import video_toolkit as vt
import os_toolkit as ost
from pathlib import Path
import pandas as pd

# def move_repeated_lang_media(media_with_file_path:str|Path, move_to_folders:list[str|Path]) -> pd.DataFrame:
#     import re
#     from collections import defaultdict
#     import pandas as pd
#     from send2trash import send2trash
    
#     """
#     Move duplicated multi-language media files into separate folders by episode.
    
#     This function organizes and separates repeated language versions of media files (e.g., multiple audio or subtitle 
#     tracks per episode) into different destination folders based on detected episode codes. It identifies episodes 
#     using a naming pattern like "S01E05" and distributes each language variant to a specified folder.
    
#     Parameters
#     ----------
#     media_with_file_path : str or Path
#         Path to a folder containing the media files to be organized. 
#         Filenames are expected to follow a pattern such as "ShowName_S01E05_lang_en.mp4".
    
#     move_to_folders : list of str or Path
#         A list of destination folders where each language variant will be moved.
#         The number of folders must match the number of language variants per episode.
    
#     Returns
#     -------
#     pd.DataFrame
#         A DataFrame showing the mapping between episode names and language indices.
#         Columns are labeled as `lang_01`, `lang_02`, etc., where each column corresponds 
#         to a destination folder in `move_to_folders`.
    
#     Raises
#     ------
#     ValueError
#         If the number of folders in `move_to_folders` does not match the number of language variants found.
#     FileNotFoundError
#         If a specified path does not exist.
    
#     Notes
#     -----
#     - The function detects episodes using the regular expression pattern `[Ss]\d\d[Ee]\d\d`.
#     - Each episode’s language variants are sorted by language index (the string following the episode code in the filename).
#     - Files are copied to the specified folders using `ost.copy_file_df`, and the originals are sent to the system trash.
#     - Missing or unmatched files will result in empty cells in the output DataFrame, indicating potential inconsistencies.
    
#     Examples
#     --------
#     Organize multilingual media into different folders:
#     >>> move_to_folders = ["./lang1", "./lang2", "./lang3"]
#     >>> df = move_repeated_lang_media("./media_folder", move_to_folders)
#     >>> print(df.head())
    
#     Output:
#       episode_name lang_01 lang_02 lang_03
#     0        S01E01      en      fr      es
#     1        S01E02      en      fr      es
    
#     Directory structure after execution:
#     media_folder/
#     ├── lang1/  → English files
#     ├── lang2/  → French files
#     └── lang3/  → Spanish files
#     """


def test_move_repeated_lang_media():
    # root_path01 = Path(r"C:\C_Video_Python\video_toolkit_test\test_move_repeated_lang_media\test_01")
    # file_path01 = root_path01 / 'French_1'
    # move_path01 = [root_path01 / 'French_1',root_path01 / 'French_2', root_path01 / 'French_CC',root_path01 / 'French_ForcedNarrative']
    # move_repeated_lang_media(file_path01,move_path01)
    
    
    root_path_02 = Path(r"C:\C_Video_Python\video_toolkit_test\test_move_repeated_lang_media\test_02")
    file_path_ZHO = root_path_02 / "Chinese_Simplified"
    move_path_ZHO = [root_path_02 / 'Chinese_Simplified',root_path_02 / 'Chinese_Traditional', root_path_02 / 'Chinese_ForcedNarrative']
    
    # eng episode 5 & 6 have only 1 sub
    file_path_ENG = root_path_02 / "English"
    move_path_ENG = [root_path_02 / 'English_ForcedNarrative',root_path_02 / 'English']
    
    file_path_FRA = root_path_02 / "French_1"
    move_path_FRA = [root_path_02 / 'French_1',root_path_02 / 'French_2', root_path_02 / 'French_CC',root_path_02 / 'French_ForcedNarrative']
    
    file_path_DEU = root_path_02 / "German_1"
    move_path_DEU = [root_path_02 / 'German_1',root_path_02 / 'German_2', root_path_02 / 'German_CC',root_path_02 / 'German_ForcedNarrative']
    
    file_path_HUN = root_path_02 / "Hungarian_1"
    move_path_HUN = [root_path_02 / 'Hungarian_1',root_path_02 / 'Hungarian_2',root_path_02 / 'Hungarian_ForcedNarrative']
    
    df_move_02_ZHO = ost.move_repeated_lang_media(file_path_ZHO,move_path_ZHO)
    df_move_02_ENG = ost.move_repeated_lang_media(file_path_ENG,move_path_ENG)
    df_move_02_FRA = ost.move_repeated_lang_media(file_path_FRA,move_path_FRA)
    df_move_02_DEU = ost.move_repeated_lang_media(file_path_DEU,move_path_DEU)
    df_move_02_HUN = ost.move_repeated_lang_media(file_path_HUN,move_path_HUN)

def hello():
    pass

hello()
    
    


# test_move_repeated_lang_media()
    

    



