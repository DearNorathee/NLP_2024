# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 11:32:08 2024

@author: Heng2020
"""

import os_toolkit as ost
from pprint import pprint
import shutil
from tqdm import tqdm
import video_toolkit as vt

def create_bigbang_merge_folder() -> None:
    big_bang_merge_folder = r"C:\C_Video_Python\Merge Language Video"
    season_folder_names = []

    for i in range(1,13):
        season_folder_names.append(f"BigBang Season {str(i).zfill(2)}")
    big_bang_merge_structure = {
        "BigBang Merged": season_folder_names
        }
    ost.create_folder_structure(root_folder = big_bang_merge_folder, structure = big_bang_merge_structure)

def create_bigbang_working_folder() -> None:
    """
    create bigbang working folders to store audio and subtitle(but not video)

    Returns
    -------
    None
        DESCRIPTION.

    """
    create_structure_at = r"C:\C_Video_Python"
    lang_folder = ["French","Portuguese","English","Spanish","German"]
    sub_lang_folder = ["English_ori .ass",  "English_ori .srt",  "French_ori .ass",
                       "French_ori .srt",  "French_whisper_base",  "Portuguese_ori",  "Portuguese_whisper_base"]
    
    # what folder_structure example looks like for 1 season
    
    # folder_structure = {
    #     "The Big Bang Theory":{
    #         "BigBang Theory Season 07": {
    #             "Season 07 Audio": lang_folder,
    #             "Season 07 Splitted Audio": lang_folder,
    #             "Season 07 Subtitle": sub_lang_folder,
    #             }
    #         }
    #     }
    
    folder_structure = {
        "The Big Bang Theory":{}
        }
    
    
    for season in range(1,13):
        season_str = str(season).zfill(2)
        curr_season_structure = {
                    f"Season {season_str} Audio": lang_folder,
                    f"Season {season_str} Splitted Audio": lang_folder,
                    f"Season {season_str} Subtitle": sub_lang_folder,
                    }
                
        folder_structure["The Big Bang Theory"][f"BigBang Theory Season {season_str}"] = curr_season_structure
        # pprint(curr_season_structure)
    # pprint(folder_structure)
    ost.create_folder_structure(root_folder = create_structure_at , structure = folder_structure)
    
    

def copy_files_to_dedicated_working_folder() -> None:
    """
    copy files from the videos to dedicated working folder

    Returns
    -------
    None
        DESCRIPTION.

    """
    
    # exclude season 11 because naming scheme is a bit different for some videos
    
    for season in tqdm(range(1,11)):
        try:
            copy_files_per_season(season)
        except Exception as e:
            print(e)
            

def copy_files_per_season(season:int) -> None:
    
    """
    copy french_audio_folder, french_whisper_sub, portuguese_ori_sub
    """
    
    season_str = str(season).zfill(2)
    
    french_audio_folder = fr"H:\D_Video\BigBang French\BigBang FR Season {season_str}\Season {season_str} Audio\French"
    french_whisper_sub = fr"H:\D_Video\BigBang French\BigBang FR Season {season_str}\Season {season_str} Audio\French Subtitle_base"
    portuguese_ori_sub = fr"H:\D_Video\BigBang Portugues\BigBang PT Season {season_str}"
    
    out_french_audio_folder = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Audio\French"
    out_french_whisper_sub = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Subtitle\French_whisper_base"
    out_portuguese_ori_sub = fr"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season {season_str}\Season {season_str} Subtitle\Portuguese_ori"
    
    ost.delete_files_in_folder(out_french_audio_folder)
    ost.delete_files_in_folder(out_french_whisper_sub)
    ost.delete_files_in_folder(out_portuguese_ori_sub)
    
    shutil.copytree(src = french_audio_folder, dst = out_french_audio_folder, dirs_exist_ok=True)
    shutil.copytree(src = french_whisper_sub, dst = out_french_whisper_sub, dirs_exist_ok=True)
    
    portuguese_ori_sub_paths = ost.get_full_filename(portuguese_ori_sub,".srt")
    
    for filepath in portuguese_ori_sub_paths:
        shutil.copy(filepath,out_portuguese_ori_sub)
    

def run_extract_bigbang_sub_per_season():
    pass

def extract_bigbang_sub_per_season(season:int) -> None:
    french_video_folder = r"H:\D_Video\BigBang French\BigBang FR Season 02"
    fr_sub_ass_folder = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Subtitle\French_ori .ass"
    fr_sub_srt_folder = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Subtitle\French_ori .srt"
    
    en_sub_ass_folder = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Subtitle\English_ori .ass"
    en_sub_srt_folder = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Subtitle\English_ori .srt"
    
    
    vt.extract_subtitle(video_folder = french_video_folder, output_folder = fr_sub_ass_folder,languages="fre")
    vt.extract_subtitle(video_folder = french_video_folder, output_folder = en_sub_ass_folder,languages="eng")
    pass

def test_extract_sub_1_video():
    video_path01 = r"H:\D_Video\BigBang French\BigBang FR Season 02\BigBang FR S02E01.mkv"

    french_video_folder = r"H:\D_Video\BigBang French\BigBang FR Season 02"
    fr_sub_ass_folder = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Subtitle\French_ori .ass"
    fr_sub_srt_folder = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Subtitle\French_ori .srt"
    
    en_sub_ass_folder = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Subtitle\English_ori .ass"
    en_sub_srt_folder = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 02\Season 02 Subtitle\English_ori .srt"

    vt.extract_sub_1_video(video_path=video_path01,output_folder=fr_sub_ass_folder,languages="fre")


def main():
    # copy_files_to_dedicated_working_folder()
    # test_extract_sub_1_video()
    extract_bigbang_sub_per_season(2)
    # copy_files_per_season(10)
    # copy_files_to_dedicated_working_folder()
    pass
if __name__ == "__main__":
    main()

    