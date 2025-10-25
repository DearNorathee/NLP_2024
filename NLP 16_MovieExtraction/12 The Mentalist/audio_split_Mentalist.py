#%%
import video_toolkit as vt
from pathlib import Path
from pydub import AudioSegment
import subprocess
import os_toolkit as ost
from tqdm import tqdm
import os
import py_string_tool as pst

#%%
splitted_audio_folder:list[str|Path|None] = [None for _ in range(20)]
input_audio_folder: list[str|Path|None] = [None for _ in range(20)]
sub_folder: list[str|Path|None] = [None for _ in range(20)]


#%%
# season 1 has no sub for some unknown reason
# declare many paths


series_name:str = "The Mentalist"

for season_int in range(1,8):
    season_str = str(season_int).zfill(2)
    splitted_audio_folder[season_int] = fr"C:\C_Video_Python\{series_name}\{series_name} Season {season_str}\Season {season_str} Splitted Audio\French"
    input_audio_folder[season_int] = fr"C:\C_Video_Python\{series_name}\{series_name} Season {season_str}\Season {season_str} Audio\French"
    sub_folder[season_int] = fr"C:\C_Video_Python\{series_name}\{series_name} Season {season_str}\Season {season_str} Subtitle\English"

prefix_names: dict[int, list[str]] = {}

for season in range(1,8):
    episode_names = ost.get_filename(input_audio_folder[season])
    n_episode = len(episode_names)
    each_season = []
    for episode in range(1,n_episode + 1):
        season_str = str(season).zfill(2)
        episode_str = str(episode).zfill(2)
        each_season.append(f"The Mentalist FR S{season_str}E{episode_str}")
    prefix_names[season] = each_season


# about 1.5 min per episode(mp3)
# took about 20 min in season7(mp3)
#%%
for season in tqdm([7], desc= f"Season ",colour='#FFC000'):
    episode_names = ost.get_filename(input_audio_folder[season])
    n_episode = len(episode_names)
    # try:
    # for episode in range(1,n_episode+1):
    #     curr_prefix_names
    if not os.path.exists(splitted_audio_folder[season]):
        raise OSError("Please check the splitted audio path. Something wrong with the path. ❌")
    vt.split_audio_by_sub(
        media_paths = input_audio_folder[season],
        sub_paths = sub_folder[season],
        output_folder = splitted_audio_folder[season],
        prefix_names = prefix_names[season],
        modify_sub = False,
        progress_bar=True,
        out_audio_ext = "mp3"
        
    )
    # except:
    #     print(f"There's an error at season {season}")
    
# from testing with 1 episode,
# French audio splitting works better when use ts in English subtitle


######################################## split 1 episode for testing
vt.split_audio_by_sub(
    media_paths = r"C:\C_Video_Python\The Mentalist\The Mentalist Season 07\Season 07 Audio\French\The Mentalist_S07E01_3_FR.mp3",
    sub_paths = r"C:\C_Video_Python\The Mentalist\The Mentalist Season 07\Season 07 Subtitle\English\The Mentalist_S07E01_26_eng.srt",
    output_folder = splitted_audio_folder[season],
    prefix_names = prefix_names[7][0],
    modify_sub = False,
    progress_bar=True,
    out_audio_ext = "wav"
    
)