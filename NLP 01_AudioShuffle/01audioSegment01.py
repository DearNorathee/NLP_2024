
########################## start run 1 ################################
import pysrt
import pandas as pd
import os
from pydub import AudioSegment
from datetime import datetime, timedelta
import time
from playsound import playsound
from typing import Literal, Union
from pathlib import Path
# Parse the SRT subtitle file

video_path = r"H:\D_Video\The Ark Season 01 Portuguese\The Ark S01E01 PT.mkv"
srt_path = r"H:\D_Video\The Ark Season 01 Portuguese\Subtitles\The Ark S01E01 PT.srt"
folder_path = r"H:\D_Video\The Ark Season 01 Portuguese\Subtitles"
prefix_name = "The Ark S01E01"


# prefix_name = "BigBang_S04E01"
alarm_path = r"H:\D_Music\Sound Effect positive-logo-opener.mp3"

def to_ms(time_obj):
    time_obj_ms = (time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second) * 1000 + time_obj.microsecond // 1000
    return time_obj_ms

def St_NumFormat0(num, max_num=None, digit=None):
    # ChatGPT solo
    # tested
    if max_num is not None:
        num_str = str(num).zfill(len(str(max_num)))
    elif digit is not None:
        num_str = str(num).zfill(digit)
    else:
        num_str = str(num)
    # print(num_str)
    return num_str

def audio_duration(video_path):


    if isinstance(video_path,str):
        video_audio = AudioSegment.from_file(video_path)
    else:
        video_audio = video_path

    # Get the duration of the audio segment in milliseconds
    duration_ms = len(video_audio)

    # Convert the duration from milliseconds to a timedelta object
    duration = timedelta(milliseconds=duration_ms)

    # Create a dummy datetime object with a zero timestamp
    dummy_datetime = datetime(1, 1, 1, 0, 0, 0)

    # Add the duration to the dummy datetime to get the final datetime
    final_datetime = dummy_datetime + duration

    return final_datetime.time()

def print_time(duration):
    # tested
    hours = duration // 3600
    minutes = (duration % 3600) / 60
    minutes_str = "{:.2f}".format(minutes)
    seconds = duration % 60
    seconds_str = "{:.2f}".format(seconds)
    if hours < 1:
        if minutes > 1:
            # only minutes
            print(f"{minutes_str} minutes", end="\n")
        else:
            # only seconds
            print(f"{seconds_str} seconds", end="\n")
    else:
        # hours with minutes
        print(f"{hours} hour", end=" ")
        print(f"{minutes_str} minutes", end="\n")

# Sub
def split_1audio_by_subtitle(video_path: Union[str,Path],
                            subtitle_path,
                            output_folder,
                            prefix_name = None,
                            out_audio_ext = "wav",
                            alarm_done_path:Union[Literal[False],str] = False,
                            verbose = 1,
                            ) -> None:
    
    # took about 1 hr(including testing)
    # Add feature: input as video_folder_path and subtitle_folder_path, then 
    # it would automatically know which subttile to use with which video(using SxxExx)
    
    # split_audio_by_subtitle

    import video_toolkit as vt
    import python_wizard as pw
    from playsound import playsound
    
    from pathlib import Path
    if prefix_name is None:
        prefix_name_in = Path(video_path).stem
    else:
        prefix_name_in = str(prefix_name)
        
    # with dot and no dots supported
    # but only tested with no dots out_audio_ext
    
    out_audio_ext_dot = out_audio_ext if out_audio_ext[0] == "." else ("." + out_audio_ext)
    out_audio_ext_no_dot = out_audio_ext[1:] if out_audio_ext[0] == "." else ( out_audio_ext)
    
    subs = vt.srt_to_df(subtitle_path)

    
    # TODO: write a function input is video/video path & subs/sub path
    t01 = time.time()
    video_audio = AudioSegment.from_file(video_path)
    t02 = time.time()
    t01_02 = t02-t01

    if verbose in [1]:
        print("Load video time: ", end = " ")
        pw.print_time(t01_02)
    
    if alarm_done_path:
        playsound(alarm_path)
    # ---------------------------- run til 1 -------------------------------
    ########################## start run 2 ################################
    t03 = time.time()
    video_length = audio_duration(video_audio)
    # Iterate over subtitle sentences
    n = subs.shape[0]
    t04 = time.time()
    for i in range(n):
        start_time = subs.loc[i,'start']
        end_time = subs.loc[i,'end']
        
        if start_time > video_length:
            break

        start_time_ms = to_ms(start_time)
        end_time_ms = to_ms(end_time)

        # Extract audio segment based on timestamps
        sentence_audio = video_audio[start_time_ms:end_time_ms]
        
        num_str = St_NumFormat0(i+1,n+1)
        # Save the audio segment to a file
        audio_name = f'{prefix_name_in}_{num_str}{out_audio_ext_dot}'
        audio_output = os.path.join(output_folder,audio_name)
        sentence_audio.export(audio_output, format=out_audio_ext_no_dot)
    t05 = time.time()

    t04_05 = t05-t04
    if alarm_done_path:
        playsound(alarm_path)

def test_split_1audio_by_subtitle():
    alarm_done_path = r"H:\D_Music\Sound Effect positive-logo-opener.mp3"
    video_path =    Path( r"H:\D_Video\The Ark Season 01 Portuguese\The Ark S01E01 PT.mkv")
    srt_path =      Path( r"H:\D_Video\The Ark Season 01 Portuguese\Subtitles\srt\The Ark S01E01 PT.srt")
    folder_path =   Path( r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 01\OutputData\split_audio_by_subtitle\test_01_Ark_S01E01")
    prefix_name =   "The Ark S01E01"
    split_1audio_by_subtitle(video_path,srt_path,output_folder = folder_path,alarm_done_path = alarm_done_path)

    
test__split_1audio_by_subtitle()
