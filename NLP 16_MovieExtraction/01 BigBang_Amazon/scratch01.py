import os_toolkit as ost
from pathlib import Path
import video_toolkit as vt

root_path_02 = Path(r"C:\C_Video_Python\The Big Bang Theory\The Big Bang Theory Season 06\Season 06 Subtitle")

file_path_FRA = root_path_02 / "French CC Amazon"
move_path_FRA = [root_path_02 / 'French CC Amazon',root_path_02 / 'French Amazon']

df_move_02_FRA = ost.move_repeated_lang_media(file_path_FRA,move_path_FRA)

sub_en = None
sub_fr = r"C:\C_Video_Python\The Big Bang Theory\The Big Bang Theory Season 06\Season 06 Subtitle\French CC Amazon\The Big Bang Theory_S06E01_8_fra.srt"

df_sub_fr = vt.sub_to_df(sub_fr)
