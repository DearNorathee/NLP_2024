#%%
import video_toolkit as vt
from pathlib import Path
from pydub import AudioSegment
import subprocess
import os_toolkit as ost
from tqdm.auto import tqdm
import os
#%%
splitted_audio_folder:list[str|Path|None] = [None for _ in range(20)]
input_audio_folder: list[str|Path|None] = [None for _ in range(20)]
sub_folder: list[str|Path|None] = [None for _ in range(20)]

series_name:str = "The Big Bang Theory"
prefix:str = "The Big Bang Theory PT_"

#%%
# season 1 has no sub for some unknown reason
# declare many paths
#!Change

# took about 1.5 min for the whole season



for season_int in range(1,13):
    season_str = str(season_int).zfill(2)
    splitted_audio_folder[season_int] = fr"C:\C_Video_Python\{series_name}\{series_name} Season {season_str}\Season {season_str} Splitted Audio\Portuguese Amazon"
    input_audio_folder[season_int] = fr"C:\C_Video_Python\{series_name}\{series_name} Season {season_str}\Season {season_str} Audio\Portuguese Amazon"
    sub_folder[season_int] = fr"C:\C_Video_Python\{series_name}\{series_name} Season {season_str}\Season {season_str} Subtitle\Portuguese Amazon"

prefix_names: dict[int, list[str]] = {}

for season in range(1,13):
    episode_names = ost.get_filename(input_audio_folder[season])
    n_episode = len(episode_names)
    each_season = []
    for episode in range(1,n_episode + 1):
        season_str = str(season).zfill(2)
        episode_str = str(episode).zfill(2)
        each_season.append(f"{prefix}S{season_str}E{episode_str}")
    prefix_names[season] = each_season




#%%
for season in tqdm(range(11,13), desc= f"Season ",colour='orange'):
    episode_names = ost.get_filename(input_audio_folder[season])
    n_episode = len(episode_names)
    # try:
    # for episode in range(1,n_episode+1):
    #     curr_prefix_names
    splitted_audio_folder_PATH = Path(splitted_audio_folder[season])
    splitted_audio_folder_PATH.mkdir(parents=True,exist_ok=True)
    if not os.path.exists(splitted_audio_folder[season]):
        raise OSError("Please check the splitted audio path. Something wrong with the path. ❌")
    vt.split_audio_by_sub(
        media_paths = input_audio_folder[season],
        sub_paths = sub_folder[season],
        output_folder = splitted_audio_folder[season],
        prefix_names = prefix_names[season],
        modify_sub = True,
        progress_bar=True
        
    )
    # except:
    #     print(f"There's an error at season {season}")

