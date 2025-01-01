# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 09:49:23 2024

@author: Heng2020
"""

import os_toolkit as ost

# D_video_mem = ost.filesize_in_folder(D_video)
# D_download_2023_mem = ost.filesize_in_folder(D_download_video_2023)
# D_download_2024_mem = ost.filesize_in_folder(D_download_video_2024)

big_bang_PT = r"H:\D_Video\BigBang Portugues"
big_bang_FR = r"H:\D_Video\BigBang French"


big_bang_PT_s06 = r"H:\D_Video\BigBang Portugues\BigBang PT Season 06"
big_bang_FR_s06 = r"H:\D_Video\BigBang French\BigBang FR Season 06"

merged_video = r"C:\C_Video_Python\Merge Language Video\tests\outputs\test_merge_media_to_video"
merged_video_s06 = r"C:\C_Video_Python\Merge Language Video\tests\outputs\test_merge_media_to_video\test_02"

big_bang_PT_mem = ost.filesize_in_folder(big_bang_PT)
big_bang_FR_mem = ost.filesize_in_folder(big_bang_FR)

merged_video_mem = ost.filesize_in_folder(merged_video)
big_bang_PT_s06_mem = ost.filesize_in_folder(big_bang_PT_s06)
big_bang_FR_s06_mem = ost.filesize_in_folder(big_bang_FR_s06)

big_bang_PT_s06_mem = big_bang_PT_s06_mem.loc[big_bang_PT_s06_mem["filesize"] > 1000].reset_index(drop=True)
big_bang_FR_s06_mem = big_bang_FR_s06_mem.loc[big_bang_FR_s06_mem["filesize"] > 1000].reset_index(drop=True)

merged_video_s06_mem = ost.filesize_in_folder(merged_video_s06)


