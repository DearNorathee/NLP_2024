# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 09:49:23 2024

@author: Heng2020
"""

import os_toolkit as ost
search_drive = r"H:"
search_drive_mem = ost.filesize_in_folder(search_drive)
D_video = r"H:\D_Video"

C_drive = r"C:"

D_download_video_2023 = r"H:\D_Download\Video 01\2023"
D_download_video_2024 = r"H:\D_Download\Video 01\2024"
C_download_2024 = r"C:\C_Download\Video\2024"
# D_video_mem = ost.filesize_in_folder(D_video)
# D_download_2023_mem = ost.filesize_in_folder(D_download_video_2023)
# D_download_2024_mem = ost.filesize_in_folder(D_download_video_2024)

C_drive_mem = ost.filesize_in_folder(C_drive)
C_download_2024_mem = ost.filesize_in_folder(C_download_2024)
G_videos = r"G:\My Drive\G_Videos"
G_videos_mem = ost.filesize_in_folder(G_videos)
