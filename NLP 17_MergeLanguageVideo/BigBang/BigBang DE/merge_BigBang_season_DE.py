
import os_toolkit as ost
from pprint import pprint
import shutil
from tqdm import tqdm
import video_toolkit as vt
from pathlib import Path
import pandas as pd

# season 1 the french audio doesn't seem to syn up perfectly

# took about 1hr to modify from French to German(I don't know if I could design the code such that it would reduce to 30 min)

# NEXT: 
    # S02E15 German has no audio at the beginning it seems to be like this only 1 video
    
# Context: right now German audio isn't syn because it's start timestamp is about 0.023021 sec behind the video
# Use this command to check start_timestamp
# ffprobe -v error -select_streams a:0 -show_entries stream=start_time -of default=noprint_wrappers=1:nokey=1 "BigBang DE S02E01_DE.mp3"
# I tried to reset the timestamp using ffmpeg but it doesn't seem to work
# There are 2 ideas that I think might work


# 1) Using ffmpeg to cut the beggining of audio check out Onenote
# 2) read mp3 using pydub then reexport it as mp3 again
    
#%%
def create_media_info_df_1season(
        season:int
        ,test:int) -> pd.DataFrame:
    
    season_str = str(season).zfill(2)
    input_video_folder:str|Path = fr"C:\C_Video\BigBang Portuguese\BigBang PT Season {season_str}"
    ep_seasons: list[str]| str = []
    
    test_folder = f"test_{str(test).zfill(2)}"
    
    output_folder:str = fr"C:\C_Video_Python\Merge Language Video\BigBang Merged\BigBang Season {season_str}" + "/" + test_folder
    
    episodes_by_season:dict[int,int] = {
        1: 18
        ,2: 23
        ,3: 23
        ,4: 24
        ,5: 24
        ,6: 24
        ,7: 24
        ,8: 24
        ,9: 24
        ,10: 24
        ,11: 24
        ,12: 24
        }
    
    curr_total_episodes = episodes_by_season[season]
    for i in range(1,curr_total_episodes +1):
        ep_str = str(i).zfill(2)
        ep_seasons.append(f"S{season_str}E{ep_str}")

    list_of_info: list[tuple[str,str,str]] = [
        # ('media_type','title','lang','input_filename_pattern')
        
        # ("subtitle", "English_ori",                 "eng",  "BigBang FR <>_1.srt"),
        # ("subtitle", "French_ori",                  "fre",  "BigBang FR <>_1.srt"),
        # ("audio",    "French",                      "fre",  "BigBang FR <>_FR.mp3"),
        # ("subtitle", "French_whisper",              "fre",  "BigBang FR <>_FR.srt"),
        
        ("subtitle", "German_Netflix",              "deu",  "BigBang DE <>.srt"),
        ("audio", "German_Netflix",              "deu",  "BigBang DE <>_DE.mp3"),
    ]

    # media_types: list[str] = ["subtitle","subtitle","subtitle","audio","subtitle"]
    # titles: list[str] = ["Portuguese_Brazilian_ori","English_ori","French_ori","French","French_whisper"]
    # lang_code_3chrs: list[str] = ["por","eng","fre","eng"]
    # input_filname_patterns: list[str] = ["BigBang PT <>.srt","BigBang FR <>_FR.mp3","BigBang FR <>_FR.srt","BigBang FR <>_EN.srt"]

    input_media_folders: list[str] = [
        fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Subtitle\German Netflix",
        fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Audio\German",

                                     ]
    
    
    output_folder_Path: Path = Path(output_folder)
    output_folder_Path.mkdir(parents=True, exist_ok=True)
    
    # use <> to represent the ep_seasons text
    media_info_df_season:pd.DataFrame
    
    media_info_df_season = vt.create_media_info_df(
        input_video_folder =  input_video_folder
        ,input_video_pattern = "BigBang PT <>.mkv"
        ,ep_seasons = ep_seasons
        ,input_media_folders = input_media_folders
        ,list_of_info = list_of_info
        ,output_folder = output_folder)
    try:
        media_info_df_season.to_excel(f"BigBang PT Season {season_str}_media info.xlsx")
    except PermissionError:
        print("The excel file media info is opened. Skip saving it....")
        
    return media_info_df_season
    

#%%
def merge_media_info_df_1season(
        season:int
        ,test:int
        ):
    
    season_str = str(season).zfill(2)
    test_folder = f"test_{str(test).zfill(2)}"
    output_folder:str = fr"C:\C_Video_Python\Merge Language Video\BigBang Merged\BigBang Season {season_str}" + "/" + test_folder
    # use <> to represent the ep_seasons text
    media_info_df_season:pd.DataFrame
    
    media_info_df_season = create_media_info_df_1season(season,test)
    
    # ############################## keep this to debug 1 episode #############################################
    # media_info_df_season_1ep = media_info_df_season.loc[media_info_df_season["input_video_name"].isin(["BigBang PT S01E01.mkv"])]
    
    ost.delete_files_in_folder(output_folder)
    
    # vt.merge_media_to1video(
    #     input_video_path= media_info_df_season_1ep.loc[0,"input_video_path"],
    #     input_info_df = media_info_df_season_1ep,
    #     output_folder = output_folder,
    #     errors="raise"
    #                         )
    # ---------------------------------------- keep this to debug 1 episode -------------------------------------------------
    
    vt.merge_media_to_video(media_info_df_season,errors="warn")
    print()

#%%
merge_media_info_df_1season(2,2)
# merge_media_info_df_1season(5,1)
# for season 2 took about 6 min 30 s

# input_video_path01 = r"H:\H_Video_Python\Merge Language Video\BigBang Merged\BigBang Season 07\BigBang PT S07E01.mkv"
# meta_data01 = vt.get_all_metadata(input_video_path01)


# ost.auto_rename_series(folder_path = "H:\H_Video\BigBang Portugues\BigBang PT Season 05", prefix = "BigBang PT")
# ost.rename_files_replace_text(folder_path, old_text, new_text)


