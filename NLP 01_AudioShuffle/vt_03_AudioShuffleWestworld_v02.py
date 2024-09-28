# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 10:34:23 2023

@author: Heng2020
"""

#%%
folder_path = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 01\OutputData\Westworld S04E01"
script_path = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 01\OutputData\Westworld_S04E01_pd.xlsx"

#%%
from playsound import playsound
import os
import random
import pandas as pd

from pydub import AudioSegment
from pydub.playback import play

import whisper 

import ffmpeg
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
import os_toolkit as ost
# Example usage
import faster_whisper
from faster_whisper import WhisperModel

# get the name of available_models
# faster_whisper.available_models()

alarm_path = "H:\D_Music\Sound Effect positive-logo-opener.mp3"
speed_factor = 0.5  # Play at 50% slower speed
################################ reload model(needs to be runed) ######################################
# spyder can't have model_base &  model_large: I have to reload everytime

#%%
def play_audio_slower(audio_path, speed_factor):
    # still not working
    # right now I use this to play audio because playsound sometimes have weird problem
    # TODO: Find way to play audio with slower speed without changing the file
    audio = AudioSegment.from_file(audio_path)
    
    # slowed_audio = audio.speedup(playback_speed=1/speed_factor)
    slow_audio = audio._spawn(audio.raw_data, overrides={"frame_rate": int(audio.frame_rate * speed_factor)})
    play(slow_audio)


#%%
# this line prevent error(not sure how it works)
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
model_base = WhisperModel('base', device="cuda")
playsound(alarm_path)
model_large = WhisperModel('large-v3',device='cpu')
playsound(alarm_path)

model_distil_large = WhisperModel('distil-large-v3')
playsound(alarm_path)
#------------------------------ reload model ------------------------------


#%%
file_path = ost.get_filename(folder_path,[".mp3",".wav"])
file_path.insert(0,None)
script = pd.read_excel(script_path)
script = script.drop(script.columns[0],axis=1)
#%%
start_inx = 1
end_inx = 10

mySeed = 24
#%%
# 55 is too easy

skip_inx = [4,9,16,17,29,30,52,53,55,68,72,79,84, 124, 152, 153, 
            154, 155, 156, 184,186, 190, 191, 193,194,195,196,198,201,202,203,204, 219
            
            ]
easy = [1,11,14,6,8,10,7,26,32, 133, 147, 148, 165,179, 181, 188,199,200]

# (2,'2-Jul-23')
# (6,'2-Jul-23')
# (10,'2-Jul-23')
# (13,'2-Jul-23')
# (18,'2-Jul-23')

# (31,'2-Aug-23')
# (36,'2-Aug-23')
# (38,'2-Aug-23')

# (46,'9-Jul-23')
# (66,'31-Jul-23')
# (67,'31-Jul-23')
# (73,'31-Jul-23')
# (75,'31-Jul-23')

# (147,'9-Apr-23')
# (148,'9-Apr-23')
# (149,'9-Apr-23')

# (159,'11-Apr-23')
# (160,'11-Apr-23')

# (166,'12-Apr-23')

#%%
random_inx_list =list(range(start_inx,end_inx+1))

random_inx_list = [x for x in random_inx_list if x not in skip_inx]
#%%
print(f"Allow index is from 0 to {len(random_inx_list)-1}")
#%%
random.seed(mySeed)
random.shuffle(random_inx_list)
#%%
########################## run below recurrently ##################################
# chosen_inx = random_inx_list[3]
chosen_inx = 204
print(f"Index: {chosen_inx}")
audio_path = os.path.join(folder_path,file_path[chosen_inx])
speed_factor = 1

play_audio_slower(audio_path, speed_factor)

#%%
###################### show answer
ans = script.loc[chosen_inx-1,'sentence']
print(ans)
################################
segments, _ = model_base.transcribe(audio_path,language="pt")
text_pred = list(segments)[0][4]
print(text_pred)

segments, _ = model_large.transcribe(audio_path,language="pt")
text_pred = list(segments)[0][4]
playsound(alarm_path)
print(text_pred)

# model_distil_large doesn't work
# segments, _ = model_distil_large.transcribe(audio_path,language="pt")
# text_pred = list(segments)[0]
# playsound(alarm_path)
# print(text_pred)



                       
