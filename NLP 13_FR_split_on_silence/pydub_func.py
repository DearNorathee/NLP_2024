# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 09:52:53 2024

@author: Heng2020
"""


from pydub import AudioSegment
from pydub.silence import split_on_silence
from pydub.playback import play
from pydub.silence import detect_nonsilent
from playsound import playsound

alarm_path = r"H:\D_Music\Sound Effect positive-logo-opener.mp3"

filepath = r"G:\My Drive\G_Videos\Learn French\Learn to speak French in 5 minutes - a dialogue for beginners!.mp3"
audio = AudioSegment.from_file(filepath) 


start_time = 35 * 1000  # Start at 35 seconds
end_time = (1*60 + 35) * 1000    # End at 1 minute and 35 seconds

# Extract the segment from the audio
segment = audio[start_time:end_time]

chunks = split_on_silence(segment,min_silence_len=700,
    # -25 is good
    silence_thresh=-30,
    # keep 200 milliseconds of leading/trailing silence
    keep_silence=200
)
playsound(alarm_path)


time_chucks = detect_nonsilent(segment,min_silence_len=700,
    # -25 is good
    silence_thresh=-30,

)
playsound(alarm_path)


audio_index = 14
start_time_test = time_chucks[audio_index][0]
end_time_test = time_chucks[audio_index][1]

formatted_start = f"{start_time_test // 1000}_{start_time_test % 1000:03d}"
formatted_end = f"{end_time_test // 1000}_{end_time_test % 1000:03d}"

print(f"{formatted_start} : {formatted_end}")
test_audio = segment[start_time_test:end_time_test]
play(test_audio)

# Done til audio_index = 14
# merge 7 & 8

# cut 6
manual_edit = {
    6:  [14_633 , 15_933],
    7:  [24_455 , 25_534],
    8:  [25_888 , 27_550],
    9:  [27_899 , 30_000],
    10: [31_075 , 32_863],
    12: [37_280 , 42_100],
    14: [42_865 : 47_224],
    
    }


test_audio02 = segment[42_865 : 47_224]
play(test_audio02)

play(chunks[audio_index])
chunks[0].start_time



plot_loudness(segment)
