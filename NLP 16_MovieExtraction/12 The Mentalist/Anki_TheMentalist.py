# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 10:15:16 2025

@author: Heng2020
"""
# worked 
import pandas as pd
import dataframe_short as ds
import math
import os_toolkit as ost

# per episode

excel_path = r"C:\Users\Norat\OneDrive\D_Documents\_Learn Languages\French\Series subtitles\The Mentalist\The Mentalist Season 7 Script_FR_Anki.xlsm"
out_csv_folder = r"C:\Users\Norat\OneDrive\D_Documents\_Learn Languages\French\Series subtitles\The Menalist Anki\S07\S07E01"
prefix = "The Mentalist_S07E01"

df = ds.read_excel(excel_path,sheet_name="S07E01")
df_list:list[pd.DataFrame] = []


df_step2 = df.iloc[:,0:4]

n = math.ceil(df["Index"].max() / 100)

for i in range(1,n+1):
    df_temp = df_step2.loc[((df_step2["Index"]>= (100*(i-1))+1) & (df_step2["Index"]<= 100*i)) & (df_step2["English"]!= 0) ].reset_index(drop=True)
    df_list.append(df_temp)


for i in range(len(df_list)):
    output_name = f"{prefix}_{100*(i+1)}.csv"
    output_path = out_csv_folder + "/" + output_name
    df_list[i].to_csv(output_path, index = False, encoding="utf-8-sig")



# extract audio path in df
filename_01 = pd.DataFrame(
    ost.get_filename(r"C:\C_Video_Python\The Mentalist\The Mentalist Season 07\Season 07 Splitted Audio\French\The Mentalist_S07E01_3_FR"))