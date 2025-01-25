import os_toolkit as ost
from pprint import pprint
import shutil
from tqdm import tqdm
import video_toolkit as vt
from pathlib import Path
# NEXT: 
# 1) Check what's wrong with S07E06, S07E19
# 2) Run other season

# I found the issue now, again it seems to be the problem when convertting .ass to .srt
# error S08E09
    #  the error seems to come from French_ori
    # 00:00:02:00,000 it should not have 00: in front

def create_media_info_df_1season(
        season:int
        ,test:int
        ):
    # error at S07E06
    
    season_str = str(season).zfill(2)
    input_video_folder:str|Path = fr"H:\D_Video\BigBang Portugues\BigBang PT Season {season_str}"
    ep_seasons: list[str]| str = []
    
    test_folder = f"test_{str(test).zfill(2)}"
    
    if season > 1:
        for i in range(1,25):
            ep_str = str(i).zfill(2)
            ep_seasons.append(f"S{season_str}E{ep_str}")

    list_of_info: list[tuple[str,str,str]] = [
        # ('media_type','title','lang','input_filename_pattern')

        # ("subtitle", "English_ori",                 "eng",  "BigBang FR <>_1.srt"),
        ("subtitle", "French_ori",                  "fre",  "BigBang FR <>_1.srt"),
        # ("audio",    "French",                      "fre",  "BigBang FR <>_FR.mp3"),
        # ("subtitle", "French_whisper",              "fre",  "BigBang FR <>_FR.srt"),
    ]

    # media_types: list[str] = ["subtitle","subtitle","subtitle","audio","subtitle"]
    # titles: list[str] = ["Portuguese_Brazilian_ori","English_ori","French_ori","French","French_whisper"]
    # lang_code_3chrs: list[str] = ["por","eng","fre","eng"]
    # input_filname_patterns: list[str] = ["BigBang PT <>.srt","BigBang FR <>_FR.mp3","BigBang FR <>_FR.srt","BigBang FR <>_EN.srt"]

    input_media_folders: list[str] = [
        # fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Subtitle\English_ori .srt",
        fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Subtitle\French_ori .srt",
        # fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Audio\French",
        # fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Subtitle\French_whisper_base",
                                      ]
    output_folder:str = fr"C:\C_Video_Python\Merge Language Video\BigBang Merged\BigBang Season {season_str}" + "/" + test_folder

    # use <> to represent the ep_seasons text
    
    
    media_info_df_season = vt.create_media_info_df(
        input_video_folder =  input_video_folder
        ,input_video_pattern = "BigBang PT <>.mkv"
        ,ep_seasons = ep_seasons
        ,input_media_folders = input_media_folders
        ,list_of_info = list_of_info
        ,output_folder = output_folder)
    
    # ############################## keep this to debug 1 episode #############################################
    media_info_df_season_1ep = media_info_df_season.loc[media_info_df_season["input_video_name"].isin(["BigBang PT S08E09.mkv"])]
    ost.delete_files_in_folder(output_folder)
    
    vt.merge_media_to1video(
        input_video_path= media_info_df_season_1ep.loc[0,"input_video_path"],
        input_info_df = media_info_df_season_1ep,
        output_folder = output_folder,
        errors="raise"
                            )
    # ---------------------------------------- keep this to debug 1 episode -------------------------------------------------
    # vt.merge_media_to1video(media_info_df_season_1ep)
    

    
    # vt.merge_media_to_video(media_info_df_season,errors="raise")
    print()

create_media_info_df_1season(8,2)
