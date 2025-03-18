# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 11:48:32 2024

@author: Heng2020
# """

# Next: create the input_df(all combinations 24 episodes in pd.df)

import video_toolkit as vt


# season = 1
# season_str = str(season).zfill(2)
# sub_EN_ori_ass_folder = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 01\Season 01 Subtitle\English_ori .ass"
# sub_FR_ori_ass_folder = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 01\Season 01 Subtitle\French_ori .ass"
# FR_video_folder = fr"C:\C_Video_Python\Merge Language Video\BigBang FR Season 01"

# sub_EN_srt_folder = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 01\Season 01 Subtitle\English_ori .srt"
# sub_FR_srt_folder = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 01\Season 01 Subtitle\French_ori .srt"

# # # vt.extract_subtitle(FR_video_folder, output_folder = sub_EN_ori_ass_folder,languages="eng")
# # # vt.extract_subtitle(FR_video_folder, output_folder = sub_FR_ori_ass_folder,languages="fre")

# vt.ass_to_srt(sub_EN_ori_ass_folder,output_folder=sub_EN_srt_folder)
# vt.ass_to_srt(sub_FR_ori_ass_folder,output_folder=sub_FR_srt_folder)
# # # vt.ass_to_df()

def ass_to_srt_BigBang_1season(season:int):
    season_str = str(season).zfill(2)
    sub_EN_ori_ass_folder = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Subtitle\English_ori .ass"
    sub_FR_ori_ass_folder = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Subtitle\French_ori .ass"
    FR_video_folder = fr"C:\C_Video_Python\Merge Language Video\BigBang FR Season {season_str}"

    sub_EN_srt_folder = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Subtitle\English_ori .srt"
    sub_FR_srt_folder = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Subtitle\French_ori .srt"

    # # vt.extract_subtitle(FR_video_folder, output_folder = sub_EN_ori_ass_folder,languages="eng")
    # # vt.extract_subtitle(FR_video_folder, output_folder = sub_FR_ori_ass_folder,languages="fre")

    vt.ass_to_srt(sub_EN_ori_ass_folder,output_folder=sub_EN_srt_folder)
    vt.ass_to_srt(sub_FR_ori_ass_folder,output_folder=sub_FR_srt_folder)

for season in range(1,12):
    try:
        ass_to_srt_BigBang_1season(season = season)
        print(f"Converting ass to srt season {season} Sucessfull !!!✅\n")
    except:
        print(f"There's an error at season: {season}❌")


# extract 1 .ass file to debug
input_ass_path = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 07\Season 07 Subtitle\French_ori .ass\BigBang FR S01E06_1.ass"
output_folder = "C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 07\Season 07 Subtitle\French_ori .srt"


vt.ass_to_srt(input_ass_path,output_folder)
