import video_toolkit as vt
from pathlib import Path
from pydub import AudioSegment
import subprocess
import os_toolkit as ost
from tqdm.auto import tqdm


splitted_audio_folder:list[str|Path|None] = [None for _ in range(20)]
input_audio_folder: list[str|Path|None] = [None for _ in range(20)]
sub_folder: list[str|Path|None] = [None for _ in range(20)]


# audio_path01 = r"H:\D_Video\BigBang French\BigBang FR Season 06\Season 06 Audio\French\BigBang FR S06E01_FR.mp3"
# sub_path01 = r"H:\D_Video\BigBang French\BigBang FR Season 06\Season 06 Audio\French Subtitle\BigBang FR S06E01_FR.srt"

# season 1 has no sub for some unknown reason
# declare many paths
for season_int in range(2,12):
    season_str = str(season_int).zfill(2)
    splitted_audio_folder[season_int] = fr"H:\D_Video_Python\French\BigBang French_test1\BigBang FR Season {season_str}\Season {season_str} Splitted Audio"
    input_audio_folder[season_int] = fr"H:\D_Video\BigBang French\BigBang FR Season {season_str}\Season {season_str} Audio\French"
                                        # "H:\D_Video\BigBang French\BigBang FR Season 11\Season 11 Audio\French"
    sub_folder[season_int] = fr"H:\D_Video\BigBang French\BigBang FR Season {season_str}"

prefix_names: dict[int, list[str]] = {}

for season in range(1,12):
    episode_names = ost.get_filename(input_audio_folder[season])
    n_episode = len(episode_names)
    each_season = []
    for episode in range(1,n_episode + 1):
        season_str = str(season).zfill(2)
        episode_str = str(episode).zfill(2)
        each_season.append(f"BigBang FR S{season_str}E{episode_str}")
    prefix_names[season] = each_season


#vt.is_ffmpeg_installed()
#test_segment = AudioSegment.from_file(audio_path01)
# ost.delete_files_in_folder(splitted_audio_folder[6])

for season in tqdm(range(6,12), desc= f"Season "):
    episode_names = ost.get_filename(input_audio_folder[season])
    n_episode = len(episode_names)
    # try:
    # for episode in range(1,n_episode+1):
    #     curr_prefix_names
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




