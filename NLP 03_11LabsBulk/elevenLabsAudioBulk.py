# -*- coding: utf-8 -*-

"""
Created on Sun Sep 17 14:31:05 2023

@author: Heng2020
"""

# majority done signature function is create_audio_bulk

# create_audio_bulk(data,
#                       output_folder = "",
#                       start_row = 3,
#                       end_row = None,
#                       col_transcribe = "Portuguese",
#                       col_translation = "English",
#                       col_filename = "AudioFileName",
#                       person = "Adam",
#                       model = "eleven_multilingual_v2"
#                       )

# add header_row(to specify the row of the header)
    # and change start_row to the data of the row(currently start_row means the header)
# NEXT: Add API if I wanna share this code with others

import pydantic
# print(pydantic.__version__)
from pydantic import model_validator
# from pydantic import 

import pandas as pd
import sys
import os
from playsound import playsound
import dataframe_short as ds

# import SrtToCsv as f1

from pathlib import Path

sentence_excel_path = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 01\NLP 03_11LabsBulk\eleven_labs_audio_template_pd.xlsb"

# !!!  output_folder should be the folder with subfolders SxxExx
# !!! otherwise I won't work properly
output_folder = Path(r"C:\Users\Heng2020\OneDrive\D_Documents\_Learn Languages\Portuguese\_LearnLanguages 04 BigBang PT\_BigBang PT\S06\Sentence Audio")

# sheet_name = "Useful", "Normal"

episode = "S06E04"
alarm_path = r"H:/D_Music/Sound Effect positive-logo-opener.mp3"


#%%
def clean_filename(ori_name):
    # update01: deal with '\n' case
    replace_with_empty = [".","?",":",'"' , "\\" ] 
    replace_with_space = ["\n", "/" ]
    
    new_name = ori_name
    for delimiter in replace_with_empty:
        new_name = new_name.replace(delimiter, "")
        
    for delimiter in replace_with_space:
        new_name = new_name.replace(delimiter, " ")

    return new_name

def St_TextBefore(text,delimiter):
    before_part = text.split(delimiter)[0]
    return before_part

def new_audio(new_audio,folder_path):
    existing_audio_ori = get_filename(folder_path,"mp3")
    existing_audio = [St_TextBefore(x, "_") for x in existing_audio_ori ]
    
    if not new_audio or pd.isna(new_audio):
        return False
    
    try:
        new_audio_prefix = St_TextBefore(new_audio, "_")
    except:
        print(f"Error at: {new_audio}")
    
    if new_audio_prefix in existing_audio:
        return False
    else:
        return True


def get_filename(folder_path,extension = "all"):
    # also include "folder"  case
# tested small
    if extension == "all":
        out_list = [ file for file in os.listdir(folder_path) ]

    elif isinstance(extension,str):
        extension_temp = [extension]

        out_list = []

        for file in os.listdir(folder_path):
            if "." in file:
                file_extension = file.split('.')[-1]
                for each_extention in extension_temp:
                    # support when it's ".csv" or only "csv"
                    if file_extension in each_extention:
                        out_list.append(file)
            elif extension == "folder":
                out_list.append(file)


    elif isinstance(extension,list):
        out_list = []
        for file in os.listdir(folder_path):

            if "." in file:
                file_extension = file.split('.')[-1]
                for each_extention in extension:
                    # support when it's ".csv" or only "csv"
                    if file_extension in each_extention:
                        out_list.append(file)

            elif "folder" in extension:
                out_list.append(file)

        return out_list

    else:
        print("Don't support this dataype for extension: please input only string or list")
        return False

    return out_list


def create_audio(text,
                 file_name,
                 folder = "",
                 person="Adam",
                 model = "eleven_multilingual_v2",
                 print_count = True,
                 alarm = True,
                 alarm_path = r"H:/D_Music/Sound Effect positive-logo-opener.mp3"
                 ):
    # middle tested
    # alarm only when the input is list
    from elevenlabs import clone, generate, play, set_api_key, Voice, VoiceDesign, Gender, Age, Accent,voices,save
    from elevenlabs.api import History, User
    from playsound import playsound
    
    if print_count:
        user = User.from_api()
        count_before = user.subscription.character_count
    
    if isinstance(text, str):
        
        outpath = folder + "\\" + file_name
        
        if ".mp3" not in file_name:
            outpath += ".mp3"
        
        audio = generate(
            text=text, 
            voice=person,
            model=model
            )
        save(audio,outpath)
        
    elif isinstance(text, list):
        
        if isinstance(file_name, str):
            # if file_name is string and number suffix at the end
            pass
        
        
        if len(text) != len(file_name):
            print("Check the number of elements in list")
            print(f"Currently file_name has {len(file_name)} elements")
            print(f"But it should be {len(text)} elements")
        
        for i, each_text in enumerate(text):
            create_audio(each_text,file_name[i],folder)
            
        if alarm:
            playsound(alarm_path)
            
    if print_count:
        user = User.from_api()
        count_after = user.subscription.character_count
        
        count_used = count_after - count_before
        left = user.subscription.character_limit - count_after
    
    if print_count:
        print(f"Used {count_used} tokens. Left with {left} tokens.")

def _create_audio(text,
                 file_name,
                 new_file = True,
                 folder = "",
                 person="Adam",
                 model = "eleven_multilingual_v2",
                 ):
    # high_tested
    # create_audio
    # created specifically to use with pd.df
    if new_file:
        create_audio(text,file_name,folder,person,model,False,False)

def tokens_used(API_KEY = "f8637df411c9b08173ab69abc6ad789e"):
    from elevenlabs import clone, generate, play, set_api_key, Voice, VoiceDesign, Gender, Age, Accent,voices,save
    from elevenlabs.api import History, User
    # medium tested
    set_api_key(API_KEY)
    user = User.from_api()
    used_count = user.subscription.character_count
    
    return used_count


def tokens_left(API_KEY = "f8637df411c9b08173ab69abc6ad789e"):
    from elevenlabs import clone, generate, play, set_api_key, Voice, VoiceDesign, Gender, Age, Accent,voices,save
    from elevenlabs.api import History, User
    # medium tested
    
    set_api_key(API_KEY)
    user = User.from_api()
    total_tokens = user.subscription.character_limit
    used_count = user.subscription.character_count
    
    left_tokens = total_tokens - used_count
    
    return left_tokens

def output_time(t_in_sec,replay ="Time spend:"):
    
    if t_in_sec >= 60:
        print(f"{replay} {t_in_sec/60:.2f} minutes")
    else:
        print(f"{replay} {int(t_in_sec)} seconds")

def create_audio_bulk(data,
                      output_folder = "",
                      sheet_name = 0,
                      header_row = 3,
                      start_row = 4,
                      end_row = None,
                      col_transcribe = "Portuguese",
                      col_translation = "English",
                      col_filename = "AudioFileName",
                      person = "Adam",
                      model = "eleven_multilingual_v2"
                      ):
    # elevenlabs 0.2.26, pydantic 2.5.2, pandas 2.1.3
    
    # can input df & Excel path
    # MAIN Function !!!!!!!!!!!!!!!!!!
    # medium tested
    # ADD:  characters left limit
    # ADD: change está => tá,.... para => pra
    
    #     create_audio_bulk,
    # and helper functions 
    # new_audio,St_TextBefore,create_audio,_create_audio,tokens_used,tokens_left
    # in 3 hr 40 min on Sep 23, 2023
    
    import pandas as pd
    from playsound import playsound
    from time import time
    import sys
    sys.path.append(r"C:\Users\Heng2020\OneDrive\Python MyLib\Python MyLib 01\02 DataFrame")
    import dataframe_short as ds
    df_sentence: pd.DataFrame
    alarm_path = r"H:/D_Music/Sound Effect positive-logo-opener.mp3"
    # when data is Excel path
    # when data is Excel object?
    # when data is df
    # need new_audio
    # add: overwrite (generate despite having the old audio)
    
    # Convert every other type to df
    if isinstance(data, pd.DataFrame):
        df_sentence = data.copy()
    
    # deal with Path object
    output_folder_in = str(output_folder) 
    
    if os.path.exists(output_folder_in) is False:
        print("This path doesn' exist. Please check the path again.")
        return False
    
    if isinstance(data, str):
        # if enter path as input
        df_read_ori = ds.pd_read_excel(data,sheet_name=sheet_name,header= 1)
        # df_read_ori = pd.read_excel(data,sheet_name=sheet_name)
        # header_row_df = df_read_ori.iloc[[header_row-2]]
        # if header_row is None:
        #     df_read = df_read_ori.iloc[:end_row-1,:]
            
        #     if end_row is None:
        #         df_read = df_read_ori.iloc[:,:]

        # elif header_row == 1 :
        #     df_read = df_read_ori.iloc[:end_row-1,:]
            
        #     if end_row is None:
        #         df_read = df_read_ori.iloc[:,:]
            
        # elif header_row >= 2:
            
        #     if end_row is None:
        #         df_read = df_read_ori.iloc[header_row-2:,:]
        #     else:   
        #         df_read = df_read_ori.iloc[header_row-2:end_row-1,:]
                
        #     df_read.columns = df_read.iloc[0]
        #     df_read = df_read[1:]
        #     df_read.reset_index(drop=True, inplace=True)
        df_read = ds.pd_read_excel2(data,sheet_name,header_row,start_row,end_row)
        df_sentence = df_read.loc[:,[col_transcribe,col_translation,col_filename]]
    
    # to ensure that filename is valid
    # can' be x[["AudioFileName"]] => otherwise clean_filename will not remove ? & .
    df_sentence[col_filename] = df_sentence.apply(lambda x: clean_filename(x[col_filename]),axis=1 )
    ts_start = time()
    before = tokens_left()
    
    # remove empty rows for faster processing
    df_sentence = df_sentence.loc[df_sentence[col_transcribe] != 0 ,:]
    
    df_sentence['NewAudio'] = df_sentence.apply(lambda row: new_audio(row[col_filename],output_folder_in)  ,axis=1)
    
    # remove empty rows
    df_sentence = df_sentence[df_sentence[col_transcribe].notnull() | df_sentence[col_translation].notnull()]
    
    df_sentence.apply(lambda row: _create_audio(
                                    row[col_transcribe],
                                    row[col_filename],
                                    row["NewAudio"],
                                    folder = output_folder_in,
                                    person = person,
                                    model = model,
                                        ),axis=1)
    after = tokens_left()
    n_sentence = len(df_sentence[(df_sentence['NewAudio'] == True) & ~(df_sentence[col_transcribe].isnull())])
    used_tokens = before - after
    print(f"Characters used for this audio generating: {used_tokens:,} characters")
    print(f"Total of sentences generated: {n_sentence}")
    print(f"Characters left: {after:,} characters ")
    ts_end = time()
    duration = ts_end - ts_start
    output_time(duration)
    playsound(alarm_path)
    



####################################################
#%%
def test_clean_filename():
    name01 = "This has . and ?"
    name02 = "our colleague/friendship"
    
    
    expect01 = "This has  and "
    expect02 = "our colleague friendship"
    
    actual01 = clean_filename(name01)
    actual02 = "our colleague friendship"
    
    assert actual01 == expect01, f"Not equal 01"
    # print(actual01)
    assert actual02 == expect02, f"Not equal 02"
    

def test_St_TextBefore():
    ex01_list = ["S06E01 001_Previously on The Big Bang Theory", "S06E01 002_I love this part!", "S06E01 003_You know, it's not exactly glamorous up there", "S06E01 004_The water that the astronauts drink is made from each other's recycled urine", "S06E01 005_I wonder what he's doing right this very second"]
    expect01 = ["S06E01 001","S06E01 002","S06E01 003","S06E01 004","S06E01 005"]
    actual01 = []
    for ex in ex01_list:
        actual = St_TextBefore(ex,"_")
        actual01.append(actual)
    assert actual01 == expect01, "Not equal"
    print(actual01)

def test_new_audio():
    folder_path = r"C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT\_BigBang PU\S06 Done\11Labs_test"
    ex01 = "S06E01 001_Previously on The Big Bang Theory"
    
    expect01 = False
    actual01 = new_audio(ex01,folder_path)
    assert actual01 == expect01, "Not equal"
    print(actual01)
    
    ex02 = "Yeahdfkef"
    expect02 = True
    actual02 = new_audio(ex01,folder_path)
    assert actual01 == actual02, "Not equal"
    print(actual01)

def test_create_audio_bulk():
    
    df_sentence = pd.read_excel(sentence_excel_path)
    df_sentence = df_sentence.iloc[1:,1:4]

    df_sentence.columns = df_sentence.iloc[0]

    df_sentence = df_sentence[1:]

    df_sentence.reset_index(drop=True, inplace=True)

    df_sentence["AudioFileName"] = df_sentence.apply(lambda x: clean_filename(x["AudioFileName"]),axis=1 )

    # create_audio_bulk(df_sentence,audio_output_folder)
    create_audio_bulk(sentence_excel_path,audio_output_folder,end_row = 15)
    
    
    
    

    
#%%

# this create_audio_bulk is designed for specific workbook format
# I also want to create a new function that will work for general worksheets/ .csv

sheet_name = "Normal"
audio_output_folder = output_folder / episode /sheet_name
create_audio_bulk(sentence_excel_path,audio_output_folder,sheet_name=sheet_name)

# sheet_name = "Useful"
# audio_output_folder = output_folder / episode /sheet_name
# create_audio_bulk(sentence_excel_path,audio_output_folder,sheet_name=sheet_name)

# create_audio_bulk(sentence_excel_path,audio_output_folder,sheet_name="Normal",end_row=103)




