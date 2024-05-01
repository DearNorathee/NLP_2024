# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 14:41:20 2023

@author: Heng2020
"""

import inspect_py as inp
import visual_auto_gui as vui
import python_wizard as pw
import os_toolkit as ost
import excel_toolkit as xt
import excel_toolkit.range as rg
import pandas as pd
import dataframe_short as ds
import video_toolkit as vt

import py_string_tool as pst



dict01 = {'A': [1, 2, 3], 'B': [4, 5, 1], 'C': [7, 1, 9]}
df01_01 = pd.DataFrame(dict01, index=['X', 'Y', 'Z'])
df01_02 = pd.DataFrame(dict01)

actual = ds.df_value_index(df01_01,1)
expect_dict = {'row_index': ['X', 'Y', 'Z'], 'col_index': ['A', 'C', 'B']}

print("From testing local lib")


pw.package_version()








