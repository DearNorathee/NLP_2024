# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 09:52:53 2024

@author: Heng2020
"""

#%%
from pydub import AudioSegment
from pydub.silence import split_on_silence
from pydub.playback import play
from pydub.silence import detect_nonsilent
from playsound import playsound
import py_string_tool as pst
from typing import *
import python_wizard as pw

#%%
def text_to_milisecond(time_text:Union[str,int,float],delimiter:str = ".") -> Union[int,float]:
    """
    time_text should be seperated by dot for :
    convert strings to miliseconds to easily convert back and forth between video view and pydub input
    if it's already int it would return the same
    
    Convert time text to milliseconds.

    Args:
    time_text (Union[str, int, float]): Time in format "hr.min.sec" or "min.sec" or milliseconds.

    Returns:
    Union[int, float]: Time in milliseconds.

    Examples:
    "4.32" => (4*60 + 32) * 1000 = 272000 ms (4 min 32 sec)
    "1.40.32" => (1*3600 + 40*60 + 32) * 1000 = 6032000 ms (1 hr 40 min 32 sec)
    """
    if isinstance(time_text, (int, float)):
        return time_text

    if not isinstance(time_text, str):
        raise ValueError("Input must be a string, int, or float.")

    parts = time_text.split(delimiter)
    
    if len(parts) == 2:
        minutes, seconds = map(int, parts)
        return (minutes * 60 + seconds) * 1000
    elif len(parts) == 3:
        hours, minutes, seconds = map(int, parts)
        return (hours * 3600 + minutes * 60 + seconds) * 1000
    else:
        raise ValueError("Invalid time format. Use 'min.sec' or 'hr.min.sec'.")


    

def export_audio(audio_segment:AudioSegment,
                 start_end_time_dict: Dict[int,Tuple[int,int]],
                 output_names:Dict[int,str],
                 output_folder:str = "",
                 progress_bar:bool = True,
                 ) -> None:
    
    # medium tested
    """
    Key feature: 
        1) Remove the invalid path in output_names automatically
    the timestamp should be in miliseconds units(for now)
    export multiple audio_segments
    make sure that index in output_names is also in start_end_time_dict
    
    example of start_end_time_dict
        start_end_time_dict = {
        6:  [14_633 , 15_933],
        7:  [24_455 , 25_534],
        8:  [25_700 , 27_550],
        9:  [27_899 , 30_000],
        10: [31_075 , 32_863],
        11: [33_439 , 36_188],
        12: [37_280 , 42_100],
        14: [42_865 , 47_224],
        
        }

    TOADD: replace => it would check if file already exists, if so depending on it's True or False, it would replace the file
    """
    import py_string_tool as pst
    clean_output_names = {}
    for inx, output_name in output_names.items():
        clean_output_names[inx] = pst.clean_filename(output_name)
    
    from tqdm import tqdm
    if progress_bar:
        loop_obj = tqdm(start_end_time_dict.items())
    else:
        loop_obj = start_end_time_dict.items()
    
    for inx, time_stamp in loop_obj:
        start_time, end_time = time_stamp
        try:
            output_name = clean_output_names[inx]
        except KeyError:
            raise KeyError(f"there's no index {inx} in your output_names(Dict). Please check your index again.")
        output_path = output_folder + "/" + output_name
        curr_audio = audio_segment[start_time:end_time]
        
        try:
            curr_audio.export(output_path)
        except PermissionError:
            raise KeyError(f"Please close the file {output_path} first.")
            
    
    
#%%
        
def test_export_audio():
    filepath = r"G:\My Drive\G_Videos\Learn French\Learn to speak French in 5 minutes - a dialogue for beginners!.mp3"
    audio = AudioSegment.from_file(filepath) 

    OUTPUT_FOLDER:str = "G:\My Drive\G_Videos\Learn French\Pydub Export test01"

    start_time = 35 * 1000  # Start at 35 seconds
    end_time = (1*60 + 35) * 1000    # End at 1 minute and 35 seconds
    
    manual_edit = {
        6:  [14_633 , 15_933],
        7:  [24_455 , 25_534],
        8:  [25_700 , 27_550],
        9:  [27_899 , 30_000],
        10: [31_075 , 32_863],
        11: [33_439 , 36_188],
        12: [37_280 , 42_100],
        14: [42_865 , 47_224],
        
        }
    
    # output_names01 has no index 10
    output_names01 = {
        6:  "01.01_I'm....mp3",
        7:  "01.02_Pleased to meet you.mp3",
        8:  "01.03_That's a nice name.mp3",
        9:  "01.05_Can I ask you a question?.mp3",
        11: "01.06_What do you like to do on a weekend?.mp3",
        12: "01.07_I like to learn French and read and you?.mp3",
        14: "01.08_I like to watch television.mp3",
        
        }
    
    output_names02 = {
        6:  "01.01_I'm....mp3",
        7:  "01.02_Pleased to meet you.mp3",
        8:  "01.03_That's a nice name.mp3",
        9:  "01.05_Can I ask you a question?.mp3",
        10: "01.07_Yes, of course.mp3",
        11: "01.08_What do you like to do on a weekend?.mp3",
        12: "01.09_I like to learn French and read and you?.mp3",
        14: "01.10_I like to watch television.mp3",
        
        }
    
    output_names03 = {
        6:  "01.01_I'm....wav",
        7:  "01.02_Pleased to meet you.wav",
        8:  "01.03_That's a nice name.wav",
        9:  "01.05_Can I ask you a question?.wav",
        10: "01.07_Yes, of course.mp3",
        11: "01.08_What do you like to do on a weekend?.wav",
        12: "01.09_I like to learn French and read and you?.wav",
        14: "01.10_I like to watch television.wav",
        
        }
    
    # Extract the segment from the audio
    segment = audio[start_time:end_time]
    try:
        export_audio(segment, manual_edit, output_names01,output_folder=OUTPUT_FOLDER)
    except Exception as error:
        assert isinstance(error, KeyError)
        
    export_audio(segment, manual_edit, output_names02,output_folder=OUTPUT_FOLDER)
    export_audio(segment, manual_edit, output_names03,output_folder=OUTPUT_FOLDER)

def test_text_to_milisecond():
    import inspect_py as inp
    actual01 = text_to_milisecond("4.32") # Output: 272000
    actual02 = text_to_milisecond("1.40.32")  # Output: 6032000
    actual03 = text_to_milisecond(5000)  # Output: 5000
    
    expect01 = 272_000
    expect02 = 6032000
    expect03 = 5000
    
    assert actual01 == expect01, inp.assert_message(actual01, expect01)
    assert actual02 == expect02, inp.assert_message(actual02, expect02)
    assert actual03 == expect03, inp.assert_message(actual03, expect03)

# test_text_to_milisecond()

# test_export_audio()
#%%
alarm_path = r"H:\D_Music\Sound Effect positive-logo-opener.mp3"

filepath = r"G:\My Drive\G_Downloads\Ebook\2024\Pimsleur - French - Complete Course\Pimsleur - French I\Pimsleur - French I - Lesson 01.mp3"
audio = AudioSegment.from_file(filepath) 

OUTPUT_FOLDER:str = "G:\My Drive\G_Videos\Learn French\Pimsleur"

#%%
start_time = 35 * 1000  # Start at 35 seconds
end_time = (1*60 + 35) * 1000    # End at 1 minute and 35 seconds

#%%
# Extract the segment from the audio
segment = audio[start_time:end_time]

chunks = split_on_silence(segment,min_silence_len=700,
    # -25 is good
    silence_thresh=-30,
    # keep 200 milliseconds of leading/trailing silence
    keep_silence=200
)
playsound(alarm_path)

#%%
time_chucks = detect_nonsilent(segment,min_silence_len=700,
    # -25 is good
    silence_thresh=-30,

)
playsound(alarm_path)

#%%
audio_index = 16
start_time_test = time_chucks[audio_index][0]
end_time_test = time_chucks[audio_index][1]

formatted_start = f"{start_time_test // 1000}_{start_time_test % 1000:03d}"
formatted_end = f"{end_time_test // 1000}_{end_time_test % 1000:03d}"

print(f"{formatted_start} : {formatted_end}")
test_audio = segment[start_time_test:end_time_test]
play(test_audio)

# Done til audio_index = 14
# merge 7 & 8
#%%
# cut 6
manual_edit = {
    1:  [4_400 , 18_000],
    2:  [565_000 , 569_000],
    3:  [579_000 , 571_000],
    # 8:  [25_700 , 27_550],
    # 9:  [27_899 , 30_000],
    # 10: [31_075 , 32_863],
    # 11: [33_439 , 36_188],
    # 12: [37_280 , 42_100],
    # 14: [42_865 , 47_224],
    # 15: [52_404 , 54_800],
    # 16: [55_901 , 58_200],
    
    }

#%%
time_in_str:str = "9.39"
text_to_milisecond(time_in_str)

#%%
output_names = {
    6:  "01.01_Full_Conversation.mp3",
    # 7:  "01.02_Pleased to meet you.mp3",
    # 8:  "01.03_That's a nice name.mp3",
    # 9:  "01.05_Can I ask you a question?.mp3",
    # 10: "01.07_Yes, of course.mp3",
    # 11: "01.08_What do you like to do on a weekend?.mp3",
    # 12: "01.09_I like to learn French and read and you?.mp3",
    # 14: "01.10_I like to watch television.mp3",
    # 15: "01.11_I have to go sorry bye!.mp3",
    # 16: "01.12_Goodbye, thank you.mp3",
    
    }

#%%
manual_index = 3
test_audio02 = audio[manual_edit[manual_index][0] : manual_edit[manual_index][1]]
play(test_audio02)

#%%
play(chunks[audio_index])
export_audio(segment, manual_edit, output_names,output_folder=OUTPUT_FOLDER)


# plot_loudness(segment)
