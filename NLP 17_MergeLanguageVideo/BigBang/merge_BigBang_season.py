import os_toolkit as ost
from pprint import pprint
import shutil
from tqdm import tqdm
import video_toolkit as vt
from pathlib import Path
# NEXT: 
# 1.(Optional) modify create_media_info_df so that it could work with info_tuple
# 2.(Split) Tuple into list and run the whole season 7

# 3.(If run successful) quickly generalize this to any seasons

def create_media_info_df_1season(season:int):
    input_video_folder:str|Path = r"H:\D_Video\BigBang Portugues\BigBang PT Season 07"
    ep_seasons: list[str]| str = []
    season_str = str(season).zfill(2)
    if season > 1:
        for i in range(1,25):
            ep_str = str(i).zfill(2)
            ep_seasons.append(f"S{season_str}E{ep_str}")

    info_tuple:list[tuple[str,str,str]] = [
        # ('media_type','title','lang','input_filename_pattern')
        ("subtitle", "Portuguese_Brazilian_ori",    "por",  "BigBang PT <>.srt"),
        ("subtitle", "English_ori",                 "eng",  "BigBang FR <>_1.srt"),
        ("subtitle", "French_ori",                  "fre",  "BigBang FR <>_1.srt"),
        ("audio",    "French",                      "fre",  "BigBang FR <>_FR.mp3"),
        ("subtitle", "French_whisper",              "eng",  "BigBang FR <>.srt"),
    ]

    media_types: list[str] = ["subtitle","subtitle","subtitle","audio","subtitle"]
    titles: list[str] = ["Portuguese_Brazilian_ori","English_ori","French_ori","French","French_whisper"]
    lang_code_3chrs: list[str] = ["por","eng","fre","eng"]
    input_filname_patterns: list[str] = ["BigBang PT <>.srt","BigBang FR <>_FR.mp3","BigBang FR <>_FR.srt","BigBang FR <>_EN.srt"]

    input_media_folders: list[str] = [r"H:\D_Video\BigBang Portugues\BigBang PT Season 07",
                                    r"C:\C_Video_Python\French\BigBang French\BigBang FR Season 07\Season 07 Subtitle\English_ori .srt",
                                    r"C:\C_Video_Python\French\BigBang French\BigBang FR Season 07\Season 07 Subtitle\French_ori .srt",
                                    r"C:\C_Video_Python\French\BigBang French\BigBang FR Season 07\Season 07 Audio\French",
                                    r"C:\C_Video_Python\French\BigBang French\BigBang FR Season 07\Season 07 Subtitle\French_whisper_base",
                                      ]
    output_folder:str = r"C:\C_Video_Python\Merge Language Video\BigBang Merged\BigBang Season 07"

    # use <> to represent the ep_seasons text
    # 
    
    create_media_info_df_season = vt.create_media_info_df(
        input_video_folder =  input_video_folder
        ,input_video_pattern = "BigBang PT <>.mkv"
        ,ep_seasons = ep_seasons
        ,media_types = media_types
        ,input_media_folders = input_media_folders
        ,input_filname_patterns = input_filname_patterns
        ,titles = titles
        ,lang_code_3chrs = lang_code_3chrs
        ,output_folder = output_folder)
    print()