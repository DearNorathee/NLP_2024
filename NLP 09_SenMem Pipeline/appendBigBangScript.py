# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 05:19:49 2023

@author: Heng2020
"""

from pathlib import Path
import pandas as pd
from playsound import playsound
import xlwings as xw
import sys

sys.path.append(r'C:\Users\Heng2020\OneDrive\Python MyLib\Python MyLib 01\02 DataFrame')
import lib02_dataframe as ds

alarm_path = r"H:\D_Music\Sound Effect positive-logo-opener.mp3"

def indexAlignedAppend(df1, df2, col_name):
    # it works: medium tested
    import pandas as pd
    """
    Appends rows from df2 to df1 based on a specific column (col_name).
    And readjust the index in each episode via (col_name)
    
    Inspired by BigBang theory script
    
    The objective of this function is to align the index so that every starting episode
    should start with index 1 of Portuguese and English
    
    Parameters:
    - df1: DataFrame, the main DataFrame to which df2 will be appended
    - df2: DataFrame, the DataFrame to append to df1
    - col_name: str, the name of the column based on which the append will be done
    
    Returns:
    - merged_df: DataFrame, the merged DataFrame
    """
    # Find the starting indices for each unique value in the col_name column in both DataFrames
    df1_start_indices = df1.groupby(col_name).head(1).index.tolist()
    df2_start_indices = df2.groupby(col_name).head(1).index.tolist()
    
    # Initialize an empty DataFrame to store the merged data
    merged_df = pd.DataFrame()

    # Loop through the unique values to merge df1 and df2 based on the col_name column
    for df1_idx, df2_idx in zip(df1_start_indices, df2_start_indices):
        df1_value = df1.loc[df1_idx, col_name]
        df2_value = df2.loc[df2_idx, col_name]
        
        if df1_value == df2_value:
            # Extract df1 rows for this value
            if df1_idx == df1_start_indices[-1]:
                df1_rows = df1.loc[df1_idx:]
            else:
                next_df1_idx = df1_start_indices[df1_start_indices.index(df1_idx) + 1]
                df1_rows = df1.loc[df1_idx:next_df1_idx - 1]
            
            # Extract df2 rows for this value
            if df2_idx == df2_start_indices[-1]:
                df2_rows = df2.loc[df2_idx:]
            else:
                next_df2_idx = df2_start_indices[df2_start_indices.index(df2_idx) + 1]
                df2_rows = df2.loc[df2_idx:next_df2_idx - 1]
            
            df1_rows = df1_rows.reset_index(drop = True)
            df2_rows = df2_rows.reset_index(drop = True)
            # Append df2 rows to df1 rows for this value
            merged_rows = pd.concat([df1_rows, df2_rows],axis=1)
            
            # Append the merged rows to the final DataFrame
            merged_df = pd.concat([merged_df, merged_rows])

    return merged_df

folder = Path(r"C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT")
excel_name = "BigBang Sentence 01_ChatGPT.xlsx"

output_name = "BigBang Sentence 01.xlsx"
output_sheet = "merge"



input_path = folder / excel_name
output_path = folder / output_name
sheet1_name = "PT"
sheet2_name = "EN"


pt_df_ori = ds.pd_read_excel(input_path, sheet_name= sheet1_name,header = 1)
playsound(alarm_path)
en_df_ori = ds.pd_read_excel(input_path, sheet_name= sheet2_name, header = 1)
playsound(alarm_path)

pt_df = pt_df_ori.iloc[:,:5]
en_df = en_df_ori.iloc[:,:5]


pt_df_music = pt_df[pt_df['sentence_PT'].str.contains('♪', na=False) ]
en_df_music = en_df[en_df['sentence_EN'].str.contains('♪', na=False) ]

# Filter out rows where 'Column1' contains '♪'
en_df_filter = en_df[~en_df['sentence_EN'].str.contains('♪', na=False)]
pt_df_filter = pt_df[~pt_df['sentence_PT'].str.contains('♪', na=False)]
en_df_music = en_df_filter[en_df_filter['sentence_EN'].str.contains('♪', na=False) ]

ans_df = indexAlignedAppend(en_df_filter,pt_df_filter,"Episode")

col_name = "Episode"
test = en_df_filter.groupby(col_name).head(1).index.tolist()

# keep only the first occurrence of each column (Episode is duplicated)
ans_df = ans_df.loc[:, ~ans_df.columns.duplicated()]

out_wb = xw.Book(output_path)
sheet_names = [sheet.name for sheet in out_wb.sheets]

if output_sheet not in sheet_names:
    out_wb.sheets.add(output_sheet)
    out_wb.sheets.add
out_ws = xw.Sheet(output_sheet)
# put 
out_ws["A1"].options(index=False).value = ans_df


