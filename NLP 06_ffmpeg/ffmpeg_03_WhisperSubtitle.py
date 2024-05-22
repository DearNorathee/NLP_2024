# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 11:35:19 2023

@author: Heng2020
"""

import whisper
from whisper.utils import get_writer
from playsound import playsound
from time import time
import pandas as pd
import stable_whisper
from stable_whisper.result import WhisperResult
from faster_whisper import WhisperModel
# import os
# os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
# os.environ["OMP_NUM_THREADS"] = "1"
# I should try lower version of stable_whisper

# based on stable_whisper: 2.13.7
######## Not done
## stable_whisper suppose to improve timestamp syncing when creating  substitles


result2:WhisperResult

alarm_done_path = r"H:\D_Music\Sound Effect positive-logo-opener.mp3"

ts01 = time()

input_path1 = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 01\OutputData\extract_audio3\test_01\The Big Bang Theory_S06E01_EN.mp3"
input_path2 = r"C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT\_BigBang PT\S06 Done\Sentence Audio\S06E01\Normal\S06E01 Normal 001_I invited him..mp3"
output_folder  = r"C:\Users\Heng2020\OneDrive\Python NLP\InputData"


# model_fast = stable_whisper.load_model('base')
# result2 = model_fast.transcribe(input_path1)

# result2.to_srt_vtt('The Big Bang Theory_S06E02_EN.srt')

from faster_whisper import WhisperModel

model_size = "base"

# Run on GPU with FP16
model = WhisperModel(model_size, device="cpu")

# or run on GPU with INT8
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
# model = WhisperModel(model_size, device="cpu", compute_type="int8")

segments, info = model.transcribe(input_path1, beam_size=5)

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

text_list = []
for segment in segments:
    text_list.append([segment.start, segment.end, segment.text])

text_df = pd.DataFrame(text_list,columns = ["start","end","text"])
model = whisper.load_model("base")

model_fast2 = stable_whisper.load_faster_whisper('base')

result2 = model_fast2.transcribe_stable(input_path1)
playsound(alarm_done_path)

result2.to_srt_vtt('The Big Bang Theory_S06E02_EN.srt')

outputpath = r"Westworld S04E01 Portuguese_01_Whisper"

writer = get_writer("srt", str(output_folder))
writer(result,outputpath)

transcribe_df = pd.DataFrame(result['segments'])[["text","start","end","avg_logprob","no_speech_prob"]]

ts02 = time()

duration = ts02 - ts01 
print(duration)

playsound(alarm_done_path)



def write_subtitle_from_transcribe(transcribe,output_name,output_folder = None):
    
    from datetime import timedelta
    import os
    segments = transcribe['segments']
    for segment in segments:
        startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
        endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
        text = segment['text']
        segmentId = segment['id']+1
        segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] is ' ' else text}\n\n"
        
        srtFilename = os.path.join("SrtFiles", f"VIDEO_FILENAME.srt")
        with open(srtFilename, 'a', encoding='utf-8') as srtFile:
            srtFile.write(segment)