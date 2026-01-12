#%%
import video_toolkit as vt
from pathlib import Path
from pydub import AudioSegment
import subprocess
import os_toolkit as ost
from tqdm.auto import tqdm
import os
import stable_whisper
#%%
# splitted_audio_folder:list[str|Path|None] = [None for _ in range(20)]
input_audio_folder: list[str|Path|None] = [None for _ in range(20)]
output_sub_folder: list[str|Path|None] = [None for _ in range(20)]


#%%
# season 1 has no sub for some unknown reason
# declare many paths
series_name:str = "The 100"


#%%
# season 1 has no sub for some unknown reason
# declare many paths
#!Change
for season_int in range(1,8):
    season_str = str(season_int).zfill(2)
    # splitted_audio_folder[season_int] = fr"C:\C_Video_Python\{series_name}\{series_name} Season {season_str}\Season {season_str} Splitted Audio\French"
    input_audio_folder[season_int] = fr"C:\C_Video_Python\{series_name}\{series_name} Season {season_str}\Season {season_str} Audio\French"
    output_sub_folder[season_int] = fr"C:\C_Video_Python\{series_name}\{series_name} Season {season_str}\Season {season_str} Subtitle\French_whisper_base"



#%%
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
fast_model_base = stable_whisper.load_faster_whisper('base', device='cuda')
processing_seasons = [7]
#%%
for season in tqdm(processing_seasons, desc= f"Season ",colour='#FFC000'):
    episode_names = ost.get_filename(input_audio_folder[season])
    n_episode = len(episode_names)
    # try:
    # for episode in range(1,n_episode+1):
    #     curr_prefix_names
    if not os.path.exists(input_audio_folder[season]):
        raise OSError("Please check the splitted audio path. Something wrong with the path. ❌")
    vt.audio_to_sub(
        audio_paths = input_audio_folder[season],
        output_folder = output_sub_folder[season],
        model = fast_model_base,
        progress_bar=True
    )
    # except:
    #     print(f"There's an error at season {season}")

