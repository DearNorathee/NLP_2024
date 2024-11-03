import video_toolkit as vt
from pathlib import Path
from pydub import AudioSegment
import subprocess
import os_toolkit as ost

splitted_audio_folder:list[str|Path|None] = [None for _ in range(20)]
input_audio_folder: list[str|Path|None] = [None for _ in range(20)]
sub_folder: list[str|Path|None] = [None for _ in range(20)]


audio_path01 = r"H:\D_Video\BigBang French\BigBang FR Season 06\Season 06 Audio\French\BigBang FR S06E01_FR.mp3"
sub_path01 = r"H:\D_Video\BigBang French\BigBang FR Season 06\Season 06 Audio\French Subtitle\BigBang FR S06E01_FR.srt"

for i in range(1,12):
    splitted_audio_folder[i] = fr"H:\D_Video_Python\French\BigBang French\BigBang FR Season 06\Season 06 Splitted Audio"
    input_audio_folder[i] = fr"H:\D_Video_Python\French\BigBang French\BigBang FR Season 06\Season 06 Splitted Audio"
    sub_folder[i] = r"H:\D_Video\BigBang French\BigBang FR Season 06\Season 06 Audio\French Subtitle\BigBang FR S06E01_FR.srt"


#vt.is_ffmpeg_installed()
#test_segment = AudioSegment.from_file(audio_path01)
ost.delete_files_in_folder(splitted_audio_folder[6])
vt.split_1audio_by_subtitle(
    video_path = audio_path01, 
    subtitle_path = sub_path01, 
    output_folder = splitted_audio_folder[6],
    modify_sub=True,
    prefix_name="BigBang FR S06E01"
    )



