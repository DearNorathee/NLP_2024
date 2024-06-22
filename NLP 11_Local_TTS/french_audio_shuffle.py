# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 10:18:44 2024

@author: Heng2020
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 10:34:23 2023

@author: Heng2020
"""
#%%

# folder_path = r"H:\D_Music\_Learn Languages\French\Local TTS generated\Duolingo\Food"
folder_path = r"H:\D_Music\_Learn Languages\French\Local TTS generated\Duolingo\04_Food"


folder_path = r"H:\D_Music\_Learn Languages\French\Local TTS generated\Duolingo\13_Verbs Present 1"

folder_path = r"H:\D_Music\_Learn Languages\French\Local TTS generated\Duolingo\12_Colors"
folder_path = r"H:\D_Music\_Learn Languages\French\Local TTS generated\Duolingo\05_Animals"
#%%

from playsound import playsound
import os
import random
import pandas as pd
import video_toolkit as vt
from pydub import AudioSegment
from pydub.playback import play


import ffmpeg
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play

import os_toolkit as ost
# Example usage

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

#------------------------------ reload model ------------------------------


#%%
file_path = ost.get_filename(folder_path,[".mp3",".wav"])
file_path.insert(0,None)

# what if the audio extension is .wav?

target_lang = [None]
eng_translation = [None]
for i in range(1,len(file_path)):
    filename = file_path[i]
    _, vocab, translation = filename.split("_")
    translation = translation.replace(".mp3","").replace(".wav","")
    target_lang.append(vocab)
    eng_translation.append(translation)

#%%
start_inx = 1
end_inx = 5


# keep_inx for 04_Food
keep_inx = [6,10, 25, 31]

# keep_inx for 13_Verbs Present 1
keep_inx = [7,29, 27, 31]

skip_inx = []

# easy for 04_Food
easy = [35,]

# easy for 13_Verbs Present 1
easy = [4,9,30, 38]
# (75,'31-Jul-23')


INCLUDE_KEEP_INDEX = False
random_inx_list =list(range(start_inx,end_inx+1))

if INCLUDE_KEEP_INDEX:
    random_inx_list = [x for x in random_inx_list if x not in skip_inx] + keep_inx
else:
    random_inx_list = [x for x in random_inx_list if x not in skip_inx]

print(f"Allow index is from 0 to {len(random_inx_list)-1}")

#%% ############ run this when I want to reshuffle the same audio set
mySeed = 1
random.seed(mySeed)
random.shuffle(random_inx_list)

#%%
###################### French word -> Audio/Translation
chosen_inx = random_inx_list[4]
ans = target_lang[chosen_inx]
print(f"Index: {chosen_inx}")
print(ans)

#---------------------------( French word -> Audio/Translation: show answer)
audio_path = os.path.join(folder_path,file_path[chosen_inx])
speed_factor = 1

vt.play_audio(audio_path)

ans = eng_translation[chosen_inx]
print(ans)

#%%
########################## Audio -> Translation ##################################
chosen_inx = random_inx_list[4]
# chosen_inx = 2
print(f"Index: {chosen_inx}")
audio_path = os.path.join(folder_path,file_path[chosen_inx])
speed_factor = 1

play_audio_slower(audio_path, speed_factor)

#%%
#--------------------------------- (Audio -> Translation: show answer) ------------------------
ans = file_path[chosen_inx]
print(ans)


#%%
###################### Translation -> Audio ##########################################
chosen_inx = random_inx_list[0]
# chosen_inx = 2
print(f"Index: {chosen_inx}")
translation = eng_translation[chosen_inx]
print(translation)

#--------------------------( Translation -> Audio: show answer)
audio_path = os.path.join(folder_path,file_path[chosen_inx])
speed_factor = 1
ans = target_lang[chosen_inx]
print(ans)

play_audio_slower(audio_path, speed_factor)



