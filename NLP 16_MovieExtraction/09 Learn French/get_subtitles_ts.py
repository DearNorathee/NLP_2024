# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 10:36:40 2025

@author: Norat
"""
import video_toolkit as vt
import shutil
import os_toolkit as ost
from typing import Literal
import pandas as pd


input_sub_folder = r"C:\C_Video\Learn French\Elisa"

sub_paths = ost.get_full_filename(input_sub_folder,extension=[".srt",".ass"])


fr_sub_paths = []
en_sub_paths = []

# sub must ended with language code for this script to auto detect it
for curr_path in sub_paths:
    temp_path = str(curr_path).split(".")[0]
    if temp_path.endswith("_EN"):
        en_sub_paths.append(curr_path)
    elif temp_path.endswith("_FR"):
        fr_sub_paths.append(curr_path)



df_sub_fr = vt.srt_to_df(fr_sub_paths[0])
df_sub_en = vt.srt_to_df(en_sub_paths[0])

df_sub_left = df_sub_fr.copy()
df_sub_right = df_sub_en.copy()

def align_simple_subtitle(
        df_sub_left:pd.DataFrame
        ,df_sub_right:pd.DataFrame
        ,verbose:int = 1
        ) -> pd.DataFrame:
    
    """
    Align two subtitle DataFrames based on start times(for simple subtitles such as French Elisa)
    
    This function takes two subtitle DataFrames (e.g., from different subtitle tracks or languages) 
    and aligns them by matching start times (minute + 0.01 × seconds). It returns a merged DataFrame 
    showing side-by-side subtitle sentences along with indicators for potential alignment issues.
    
    Parameters
    ----------
    df_sub_left : pd.DataFrame
        DataFrame containing the first subtitle set. Must contain the following columns:
        - 'start': Subtitle start timestamp (datetime-like or timedelta-like object).
        - 'end': Subtitle end timestamp.
        - 'sentence': Subtitle text.
    
    df_sub_right : pd.DataFrame
        DataFrame containing the second subtitle set. Must contain the same columns as `df_sub_left`.
    
    Returns
    -------
    pd.DataFrame
        A merged DataFrame with the following columns:
        - 'left_start_ts', 'left_end_ts', 'sentence_left': Original timing and text from `df_sub_left`.
        - 'right_start_ts', 'right_end_ts', 'sentence_right': Original timing and text from `df_sub_right`.
        - 'left_start_time', 'right_start_time': Numeric values computed from start timestamps for alignment.
        - 'start_time': Combined start time for sorting.
        - 'has_issue': Boolean flag indicating whether one of the subtitles is missing for a given start time.
    
    Notes
    -----
    - Matching is done using a simplified time representation (`minute + second × 0.01`), which may 
      not be precise enough for all cases.
    - Rows where one side is missing are flagged in `has_issue` for manual inspection.
    - A summary of the number of mismatches is printed after processing.
    
    Examples
    --------
    Align two subtitle tracks:
    >>> df1 = vt.sub_to_df("english.srt")
    >>> df2 = vt.sub_to_df("spanish.srt")
    >>> aligned_df = align_simple_subtitle(df1, df2)
    There are 3 issues in total. Fix manually.
    """

    import dataframe_short.move_column as mc

    df_sub_left = df_sub_left.rename(columns = {
        'start':'left_start_ts',
        'end': 'left_end_ts',
        'sentence':'sentence_left'
        })
    df_sub_left.index = range(1, len(df_sub_left) + 1)
    
    df_sub_right = df_sub_right.rename(columns = {
        'start':'right_start_ts',
        'end': 'right_end_ts',
        'sentence':'sentence_right'
        })
    df_sub_right.index = range(1, len(df_sub_right) + 1)
    
    df_sub_left['left_start_time'] = df_sub_left['left_start_ts'].apply(lambda t: t.minute + t.second*0.01)
    df_sub_right['right_start_time'] = df_sub_right['right_start_ts'].apply(lambda t: t.minute + t.second*0.01)
    
    df_merge_step1 = df_sub_left.merge(df_sub_right, left_on = ['left_start_time'], right_on = ['right_start_time'], how ='left')
    
    df_only_in_right = df_sub_left.merge(df_sub_right, left_on = ['left_start_time'], right_on = ['right_start_time'], how ='right', indicator = True)
    df_only_in_right = df_only_in_right.loc[df_only_in_right['_merge'].isin(['right_only'])]
    df_only_in_right = df_only_in_right.drop(columns = ['_merge'])
    
    
    df_merge_step2 = pd.concat([df_merge_step1,df_only_in_right])
    df_merge_step2['start_time'] = df_merge_step2['left_start_time'].combine_first(df_merge_step2['right_start_time'])
    
    df_merge_step2 = df_merge_step2.sort_values(['start_time'])
    
    df_merge_step2['has_issue'] = False
    df_merge_step2.loc[df_merge_step2['left_start_time'].isna() | df_merge_step2['right_start_time'].isna() ,'has_issue'] = True
    
    
    issue_count = df_merge_step2['has_issue'].sum()
    mc.to_first_col(df_merge_step2, cols =  ['sentence_left','sentence_right','has_issue'])
    
    if verbose >= 1:
        print(f'There are {issue_count} issues in total. Fix manually.')
    return df_merge_step2

result_df = align_simple_subtitle(df_sub_en,df_sub_fr)





