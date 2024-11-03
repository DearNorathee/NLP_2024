import video_toolkit as vt
from pathlib import Path
from pydub import AudioSegment
import subprocess

season_folder:list[str|Path|None] = [None for _ in range(20)]

season_folder[6] = r"H:\D_Video_Python\French\BigBang French\BigBang FR Season 06\Season 06 Splitted Audio"
audio_path01 = r"H:\D_Video\BigBang French\BigBang FR Season 06\Season 06 Audio\French Audio\BigBang FR S06E01_FR.mp3"
sub_path01 = r"H:\D_Video\BigBang French\BigBang FR Season 06\Season 06 Audio\French Subtitle\BigBang FR S06E01_FR.srt"

#vt.is_ffmpeg_installed()
#test_segment = AudioSegment.from_file(audio_path01)

vt.split_1audio_by_subtitle(
    video_path = audio_path01, 
    subtitle_path = sub_path01, 
    output_folder = season_folder[6],
    modify_sub=True
    )

result = subprocess.run([r"C:\PATH_Programs\ffmpeg.exe", "-version"], capture_output=True, text=True, check=True)

result = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True, check=True)
# vt.split_audio_by_sub()
import os
print(os.environ["PATH"])
