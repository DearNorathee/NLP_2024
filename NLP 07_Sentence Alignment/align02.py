

"""
Created on Fri Nov 17 06:42:11 2023

@author: Heng2020
"""

import openpyxl
from lingtrain_aligner import aligner
from pathlib import Path
import pandas as pd
from playsound import playsound
# currently signature function is in lingtrain_aligner_func
# I'll export to here in the future.
from lingtrain_aligner_func import sentence_alignment, sen_alignment_df

sys.path.append(r'C:\Users\Heng2020\OneDrive\Python MyLib\Python MyLib 01\02 DataFrame')
sys.path.append(r'C:\Users\Heng2020\OneDrive\Python MyLib\Python MyLib 01\06 General Python')
sys.path.append(r'C:\Users\Heng2020\OneDrive\Python MyLib\Python MyLib 01\09 NLP_lib')
sys.path.append(r'C:\Users\Heng2020\OneDrive\Python MyLib\Python MyLib 01\10 OS')

import dataframe_short as ds
import video_tools as vt
import python_wizard01 as pw
import os_01 as ost


# NEXT: 
# test: read_movie_script2!!!

# read the link here of how to use Lingtrain
# https://habr.com/ru/articles/586574/

alarm_path = r"H:\D_Music\Sound Effect positive-logo-opener.mp3"

def read_sentences_from_excel(file_path, sheet_name, portuguese_col, english_col, nrows=None):
    """
    Reads Portuguese and English sentences from an Excel file.
    
    :param file_path: Path to the Excel file.
    :param sheet_name: Name of the sheet containing the sentences.
    :param portuguese_col: Column letter for Portuguese sentences.
    :param english_col: Column letter for English sentences.
    :return: Tuple of two lists containing Portuguese and English sentences.
    """

    df = ds.pd_read_excel(file_path,sheet_name=sheet_name,nrows=nrows,usecols=[portuguese_col,english_col])

    portuguese_sentences = df.iloc[:,0].tolist()
    english_sentences = df.iloc[:,1].tolist()


    return portuguese_sentences, english_sentences

    
def read_movie_script(file_path, sheet_name = "Sheet1", portuguese_col = 0, english_col = 1):
    # middle tested 
    # dependency: pd_by_column, pd_split_into_dict_df, pd_regex_index
    import pandas as pd
    import re
    
    # Load the dataset from the Excel file

    data_ori = ds.pd_read_excel(file_path, sheet_name=sheet_name)
    # playsound(alarm_path)
    
    data = ds.pd_by_column(data_ori,[portuguese_col, english_col])
    

    # Function to check if a cell value matches the episode identifier pattern (e.g., S01E01)
    # r'[Ss]\d{2}[Ee]\d{2}' => S01E01
    df_dict = ds.pd_split_into_dict_df(data,r'[Ss]\d{2}[Ee]\d{2}',0)
    # df_dict = pd_split_into_dict_df(data,index_list=episode_start_indices)
    return df_dict


def read_movie_script2(file_path, sheet_name, portuguese_col, english_col):
    
    df = ds.pd_read_excel(file_path, sheet_name=sheet_name)
    # df = pd_by_column(df_ori, [portuguese_col,english_col])
    import pandas as pd
    """
    Extracts content from a DataFrame based on 'Episode' information.

    Parameters
    ----------
    df : pandas.DataFrame
        The original DataFrame containing an 'Episode' column with format 'SxxExx',
        and columns for content ('sentence_PT', 'sentence_EN').

    Returns
    -------
    pandas.DataFrame
        A new DataFrame with 'season' and 'episode' as MultiIndex.
        Each row contains a DataFrame in the 'content' column, which itself
        contains 'sentence_PT' and 'sentence_EN' from the original DataFrame.

    Examples
    --------
    >>> main_df = pd.DataFrame({
    ...     'Episode': ['S06E08', 'S06E08', 'S01E01'],
    ...     'sentence_PT': ['sentence1_PT', 'sentence2_PT', 'sentence3_PT'],
    ...     'sentence_EN': ['sentence1_EN', 'sentence2_EN', 'sentence3_EN']
    ... })
    >>> read_movie_script2(main_df)
    """
    # Extract season and episode numbers from the 'Episode' column
    df['season'] = df['Episode'].str.extract(r'S(\d+)E\d+').astype(int)
    df['episode'] = df['Episode'].str.extract(r'S\d+E(\d+)').astype(int)
    
    # Prepare the data for the new DataFrame
    data = []
    
    # Group by 'season' and 'episode', then iterate over each group
    for (season, episode), group in df.groupby(['season', 'episode']):
        # Create a DataFrame for this group's content
        content_df = pd_by_column(group, [portuguese_col, english_col]).reset_index(drop=True)
        
        # Append season, episode, and content DataFrame to the list
        data.append({'season': season, 'episode': episode, 'content': content_df})
    
    # Convert the list to a DataFrame
    new_df = pd.DataFrame(data)
    
    # Set 'season' and 'episode' as the index
    new_df.set_index(['season', 'episode'], inplace=True)
    
    return new_df



folder = r"C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT"
filename = r"BigBang Sentence 01.xlsx"

folderpath = Path(folder)
file_path = folderpath / filename

data_ori = ds.pd_read_excel(file_path)

sheet_name = 'merge'
portuguese_col = 7  # Assuming Portuguese sentences are in column F
english_col = 2    # Assuming English sentences are in column B


# Read sentences from Excel
# portuguese_sentences, english_sentences = read_sentences_from_excel(file_path, sheet_name, portuguese_col, english_col)
dict_df = read_movie_script(file_path, sheet_name, portuguese_col, english_col)

df_script = read_movie_script2(file_path, sheet_name, portuguese_col, english_col)

# Align and save sentences
# align_sentences_to_df(portuguese_sentences, english_sentences)

test_episode = "S06E05"
script_df = dict_df[test_episode]

sen_aligned = sen_alignment_df(script_df,lang_from="pt",lang_to="en")

