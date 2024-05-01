# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:19:26 2024

@author: Heng2020
"""

import sys
sys.path.append(r'C:\Users\Heng2020\OneDrive\Python MyLib\Python MyLib 01\09 NLP_lib')
sys.path.append(r'C:\Users\Heng2020\OneDrive\Python MyLib\Python MyLib 01\06 General Python')
import video_tools as vt
import python_wizard01 as pw
from playsound import playsound


video_EN_folder = r'H:\D_Video\TheBigBangTheory\The Big Bang Theory 01'
sub_EN_folder = r'H:\D_Video\TheBigBangTheory\The Big Bang Theory 01\EN Subtitles'
excel_EN_folder = r'C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT\_BigBang EN\S01'

alarm_done_path = r"H:\D_Music\Sound Effect positive-logo-opener.mp3"

sub_EN_folder_list = [
    r"H:\D_Video\TheBigBangTheory\BigBang EN Season 01\EN Subtitles",
    r"H:\D_Video\TheBigBangTheory\BigBang EN Season 02\EN Subtitles",
    r"H:\D_Video\TheBigBangTheory\BigBang EN Season 03\EN Subtitles",
    r"H:\D_Video\TheBigBangTheory\BigBang EN Season 04\subtitles\english",
    r"H:\D_Video\TheBigBangTheory\BigBang EN Season 05\subtitles\english",
    # r"H:\D_Video\TheBigBangTheory\BigBang EN Season 06\EN Subtitles",
    r"H:\D_Video\TheBigBangTheory\BigBang EN Season 07\EN Subtitles",
    r"H:\D_Video\TheBigBangTheory\BigBang EN Season 08\EN Subtitles",
    r"H:\D_Video\TheBigBangTheory\BigBang EN Season 09\EN Subtitles",
    r"H:\D_Video\TheBigBangTheory\BigBang EN Season 10 Russian\EN Subtitles",
    r"H:\D_Video\TheBigBangTheory\BigBang EN Season 11\EN Subtitles",
    
    ]

excel_EN_folder_list = [
    r"C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT\_BigBang EN\S01",
    r"C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT\_BigBang EN\S02",
    r"C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT\_BigBang EN\S03",
    r"C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT\_BigBang EN\S04",
    r"C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT\_BigBang EN\S05",
    # r"C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT\_BigBang EN\S06",
    r"C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT\_BigBang EN\S07",
    r"C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT\_BigBang EN\S08",
    r"C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT\_BigBang EN\S09",
    r"C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT\_BigBang EN\S10",
    r"C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT\_BigBang EN\S11",
    ]


sub_PT_folder_list = [
    r"H:\D_Video\BigBang Portugues\BigBang PT Season 01",
    r"H:\D_Video\BigBang Portugues\BigBang PT Season 02",
    r"H:\D_Video\BigBang Portugues\BigBang PT Season 03",
    r"H:\D_Video\BigBang Portugues\BigBang PT Season 04",
    r"H:\D_Video\BigBang Portugues\BigBang PT Season 05",
    # r"H:\D_Video\BigBang Portugues\BigBang PT Season 06",
    r"H:\D_Video\BigBang Portugues\BigBang PT Season 07",
    r"H:\D_Video\BigBang Portugues\BigBang PT Season 08",
    r"H:\D_Video\BigBang Portugues\BigBang PT Season 09",
    r"H:\D_Video\BigBang Portugues\BigBang PT Season 10",
    r"H:\D_Video\BigBang Portugues\BigBang PT Season 11",

    
    ]

excel_PT_folder_list = [
    r"C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT\_BigBang PT\S01",
    r"C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT\_BigBang PT\S02",
    r"C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT\_BigBang PT\S03",
    r"C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT\_BigBang PT\S04",
    r"C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT\_BigBang PT\S05",
    # r"C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT\_BigBang PT\S06",
    r"C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT\_BigBang PT\S07",
    r"C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT\_BigBang PT\S08",
    r"C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT\_BigBang PT\S09",
    r"C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT\_BigBang PT\S10",
    r"C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT\_BigBang PT\S11",
    ]



for i in range(10):
    sub_EN_folder = sub_EN_folder_list[i]
    excel_EN_folder = excel_EN_folder_list[i]
    vt.srt_to_Excel(sub_EN_folder, excel_EN_folder)
playsound(alarm_done_path)

# have error in season 11:(Not sure it's coming from PT or EN)
for i in range(10):
    try:
        sub_PT_folder = sub_PT_folder_list[i]
        excel_PT_folder = excel_PT_folder_list[i]
        vt.srt_to_Excel(sub_PT_folder, excel_PT_folder)
    except UnicodeDecodeError:
        print(f"Error at {sub_PT_folder}")
playsound(alarm_done_path)


srt_file_folder = r"H:\D_Video\BigBang Portugues\BigBang PT Season 01"
extract_sub_output_folder = r"C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT\_BigBang PT\S01"

vt.srt_to_Excel(srt_file_folder, extract_sub_output_folder)