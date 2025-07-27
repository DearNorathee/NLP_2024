# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 09:21:08 2025

@author: Norat
"""
# house of dragon


import os_toolkit as ost
import numpy as np
import pandas as pd

path_test01 = r"C:/"
big_bang_FR = r"H:\D_Video\BigBang French"

path_test02 = r"C:\Users\Norat\OneDrive\D_Documents\_My Life\storage_2025_07_20.csv"

C_drive_mem = ost.filesize_in_folder(path_test01)
C_folders = np.array(ost.get_folders_name(path_test01))


g_drive_path = r"G:\My Drive\G_Videos"

df_test02 = pd.read_csv(path_test02)

g_drive_mem = ost.filesize_in_folder(g_drive_path)
