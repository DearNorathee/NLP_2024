# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 13:33:43 2025

@author: Heng2020
"""

import video_toolkit as vt
import shutil
import os_toolkit as ost

sub_paths = [
    r"C:\C_Video\Learn German\03_Kurzgesagt German\01_Hier ist der Beweis Du bist tot_DE.srt"
    ,r"C:\C_Video\Learn German\03_Kurzgesagt German\02_Kannst du dein Bewusstsein auf einem Computer speichern und ewig leben_DE.srt"
    ,r"C:\C_Video\Learn German\03_Kurzgesagt German\03_Wie funktioniert das Universum  Die Stringtheorie erklärt_DE.srt"
    ,r"C:\C_Video\Learn German\03_Kurzgesagt German\04_Das Immunsystem erklärt_DE.srt"
    ,r"C:\C_Video\Learn German\03_Kurzgesagt German\05_Wer ist schuld am Klimawandel  Wer muss jetzt handeln_DE.srt"
    ]

sub_input_folder = r"C:\C_Video\Learn German\03_Kurzgesagt German"
sub_output_folder = r"C:\C_Video_Python\Learn German\Kurzgesagt German\Extracted subtitle Raw"

media_paths = [
    r"C:\C_Video\Learn German\03_Kurzgesagt German\01_Hier ist der Beweis Du bist tot.mp4"
    ,r"C:\C_Video\Learn German\03_Kurzgesagt German\02_Kannst du dein Bewusstsein auf einem Computer speichern und ewig leben.mp4"
    ,r"C:\C_Video\Learn German\03_Kurzgesagt German\03_Wie funktioniert das Universum  Die Stringtheorie erklärt.mp4"
    ,r"C:\C_Video\Learn German\03_Kurzgesagt German\04_Das Immunsystem erklärt.mp4"
    ,r"C:\C_Video\Learn German\03_Kurzgesagt German\05_Wer ist schuld am Klimawandel  Wer muss jetzt handeln.mp4"
    ]

output_folder = r"C:\C_Video_Python\Learn German\Kurzgesagt German\Splitted Audio"

prefix_names = []
for i in range(1,6):
    prefix_names.append(f"de_Kurzgesagt_video_{str(i).zfill(2)}")

vt.split_audio_by_sub(
    media_paths = media_paths
    , sub_paths = sub_paths
    , output_folder = output_folder
    ,prefix_names= prefix_names
    ,create_media_folder=True
    )

# vt.split_1audio_by_subtitle(
#     media_path = media_paths[0]
#     , subtitle_path = sub_paths[0]
#     , output_folder = output_folder
    
#     )
srt_df = vt.srt_to_df(sub_input_folder)
vt.srt_to_Excel(srt_path = sub_input_folder, output_path = sub_output_folder)



