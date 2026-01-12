# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 10:15:16 2025

@author: Heng2020
"""

import pandas as pd
import dataframe_short as ds
import math
import os_toolkit as ost

excel_path = r"C:\Users\Heng2020\OneDrive\D_Documents\_Learn Languages\German\Learn German with Nico_A1_Reading.xlsx"

out_csv_folder = r"C:\Users\Heng2020\OneDrive\D_Documents\_Learn Languages\German\Nicos Anki"

df = ds.read_excel(excel_path,sheet_name="Anki_path")
df_list:list[pd.DataFrame] = []


n = math.ceil(df["Index"].max() / 100)

for i in range(1,n+1):
    df_temp = df.loc[((df["Index"]>= (100*(i-1))+1) & (df["Index"]<= 100*i)) & (df["English"]!= 0) ].reset_index(drop=True)
    df_list.append(df_temp)


for i in range(len(df_list)):
    output_name = f"GermanNico_A1_{100*(i+1)}.csv"
    output_path = out_csv_folder + "/" + output_name
    df_list[i].to_csv(output_path, index = False, encoding="utf-8-sig")



