# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 11:54:35 2024

@author: Heng2020
"""
import shutil
folder_test01 = r"C:\C_Video_Python\Merge Language Video\tests\outputs\test_ass_to_srt_1file\test_01"

folder_test02 = r"C:\C_Video_Python\Merge Language Video\tests\outputs"

shutil.copy(folder_test01,folder_test02)

shutil.copytree(folder_test01, folder_test02, dirs_exist_ok=True)
