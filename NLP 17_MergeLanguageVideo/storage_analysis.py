# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 09:36:47 2025

@author: Norat
"""


import os_toolkit as ost
import numpy as np
import pandas as pd

path_test01 = r"C:/"
big_bang_FR = r"H:\D_Video\BigBang French"

amazon_prime_path = r'C:\DVDFab\StreamFab\Output\Amazon'

# path_test02 = r"C:\Users\Norat\OneDrive\D_Documents\_My Life\storage_2025_07_20.csv"

# g_video_path = r'G:\My Drive\G_Videos'

# C_drive_mem = ost.filesize_in_folder(path_test01)
# C_folders = np.array(ost.get_folders_name(path_test01))

# G_video_mem = ost.filesize_in_folder(g_video_path)

# G_HBO_series_path = r"G:\My Drive\G_Videos\HBO Series"
# G_series_path = r"G:\My Drive\G_Videos\Series"
# G_anime_path = r"G:\My Drive\G_Videos\Japanese Anime"
# G_Movie_path = r"G:\My Drive\G_Videos\Movies"

# G_HBO_series_mem = ost.filesize_in_folder(G_HBO_series_path)
# G_series_mem = ost.filesize_in_folder(G_series_path)
# G_anime_mem = ost.filesize_in_folder(G_anime_path)
# G_Movie_mem = ost.filesize_in_folder(G_Movie_path)

amazon_prime_mem = ost.filesize_in_folder(amazon_prime_path,unit="GB")
