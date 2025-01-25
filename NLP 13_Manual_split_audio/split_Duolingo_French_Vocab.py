# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 10:15:45 2024

@author: Heng2020
"""
# objective is to split vocab and put it in my phone to memorize
# C:\Users\Heng2020\OneDrive\D_Documents\_Learn Languages\French\Duolingo Vocab French 02.xlsm
# Done

import pandas as pd
import dataframe_short as ds
import py_string_tool as pst
import os_toolkit as ost
import numpy as np

excel_path01 = r"C:\Users\Heng2020\OneDrive\D_Documents\_Learn Languages\French\Duolingo Vocab French 02_pd.xlsm"
output_folder01 = r"C:\Users\Heng2020\OneDrive\D_Documents\_Learn Languages\French\Duolingo Auto Splitted\Test_01"
sheet_name = "formated"
# df01 = ds.read_excel(excel_path01,sheet_name = sheet_name)
df01_ori = pd.read_excel(excel_path01,sheet_name = sheet_name)

df01 = df01_ori.iloc[:, 1:3]

# encoding = "utf-8-sig" prevents getting Thai character for French unique alphabet
# to see example, just remove encoding, and open the .csv file in Excel, you'll find some weird error

ENCODING = "utf-8-sig"

splitted_df01 = ds.split_into_dict_df(df01,add_prefix_index=True)

for filename, df in splitted_df01.items():
    output_path = output_folder01 + "/" + "Duolingo_FR_" + pst.clean_filename(filename) + ".csv"
    curr_df = df.copy()
    # curr_df = curr_df.drop(index=0).reset_index(drop=True)
    curr_df.to_csv(output_path, index = False, encoding = ENCODING, header=False)
    # df.to_csv()
    
# test_df = splitted_df01['07_Plurals']
# test_df_drop = test_df.drop(index=0).reset_index(drop=True)

duoling_names = pd.DataFrame(ost.get_filename(r"C:\Users\Heng2020\OneDrive\D_Documents\_Learn Languages\French\Duolingo Auto Splitted\Test_01"))
