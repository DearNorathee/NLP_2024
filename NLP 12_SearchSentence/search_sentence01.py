# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 08:35:31 2024

@author: Heng2020
"""
# conclusion for now
# seems like other -mos vocabs (s is pronounced at the end)

import sys
sys.path.append(r'C:\Users\Heng2020\OneDrive\Python MyLib\Python MyLib 01\09 NLP_lib')
sys.path.append(r'C:\Users\Heng2020\OneDrive\Python MyLib\Python MyLib 01\06 General Python')

sys.path.append(r'C:\Users\Heng2020\OneDrive\Python MyLib\Python MyLib 01\02 DataFrame')
sys.path.append(r'C:\Users\Heng2020\OneDrive\Python MyLib\Python MyLib 01\06 General Python')
sys.path.append(r'C:\Users\Heng2020\OneDrive\Python MyLib\Python MyLib 01\09 NLP_lib')
sys.path.append(r'C:\Users\Heng2020\OneDrive\Python MyLib\Python MyLib 01\10 OS')

import lib02_dataframe as ds
import video_tools as vt
import python_wizard01 as pw
import os_01 as ost


from playsound import playsound
import re


video_folder = r"H:\D_Video\Westworld Portugues 04"
sub_folder = r"H:\D_Video\Westworld Portugues 04\PT Subtitle"

out_excel_folder = r"H:\D_Video\Westworld Portugues 04\PT Subtitle Excel"

script_path = r"C:/Users/Heng2020/OneDrive/D_Code/Python/Python NLP/NLP 02/NLP 12_SearchSentence/Westworld S4 PT/Westworld S04E08 Portuguese.xlsx"

# extract_subtitle have an error
# vt.extract_subtitle(video_folder, sub_folder)

# vt.srt_to_Excel(sub_folder, out_excel_folder)

df = ds.pd_read_excel(script_path)

df = df.iloc[: , 1:]


# List of words to exclude
exclude = ['vamos', 'estamos']

# Create a regular expression pattern dynamically
exclude_pattern = '|'.join(exclude)

# Modify the regular expression pattern to exclude the words in the exclude list
pattern = r'\b(?!(?:' + exclude_pattern + r'))(\w+mos)\b'

# Extract words ending with "mos" but not in the exclude list
df['found'] = df['sentence'].str.extract(pattern,flags=re.IGNORECASE)
df_found = df.loc[~df['found'].isnull()]
