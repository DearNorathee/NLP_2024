# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 11:48:59 2024

@author: Heng2020
"""
# import excel_tool as xt
# import excel_tool.range as rg

# NEXT: write audio_from_df from create_audio

import pyttsx3
import sys

from typing import Literal,Union

import dataframe_short as ds
import pandas as pd
from pathlib import Path
import py_string_tool as pst
pst.format_index_num(4,534)

excel_path = r"C:\Users\Heng2020\OneDrive\D_Documents\_Learn Languages\_LearnLanguages 02 Main\Duolingo\Duolingo French 02.xlsm"

sheet_name = "python_test"

# vocab_df = ds.pd_read_excel(excel_path,sheet_name=sheet_name)

def lang_voice_name():
    """
    return the list of avaliable tts in your local machine

    Returns
    -------
    list.

    """
    import pyttsx3
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    out_list = []
    for voice in voices:
        out_list.append(voice.name)
    return out_list

def engine_by_lang(language):
    # must spell language correctly, the upper vs lower case doesn't matter
    voice_name = lang_voice_name()
    import pyttsx3
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # still can't tell the gender of the engine
    for i, name in enumerate(voice_name):
        if language.lower() in name.lower():
            used_id = voices[i].id
            engine.setProperty('voice', used_id) 
            
            return engine
    # can't find the language in the system
    return False

def create_audio(text:str,language:str = "auto",filename = "", output_folder = "",playsound = False):
    # doesn't seem to work in VSCode but it works fine in Spyder
    
    if language in ["auto"]:
        language_in = detect_language(text)
    else:
        language_in = language
        
    engine = engine_by_lang(language_in)
    if engine is False:
        raise Exception(f"Doesn't have '{language_in}' in the keyboard system. Please download this language in your keyboard. ")
    
    if isinstance(text, list):
        
        if isinstance(filename, list):
            if len(text) != len(filename):
                raise Exception(f"The length of text is: {len(text)}. The length of filename is {len(filename)}. Make sure they have the same length.")
            
        n_digit = len(str(len(text)))
            
        if filename in [""]:
            filename_in = list(text)
        else:
            filename_in = list(filename)
        
        out_filenames = []
        for i, curr_filename in enumerate(filename_in):
            out_filename = f"{i+1:0{n_digit}}_{curr_filename}"
            out_filenames.append(out_filename)

            
        for i, curr_text in enumerate(text):
            create_audio(
                curr_text,
                language = language,
                filename = out_filenames[i],
                output_folder = output_folder,
                playsound = playsound,
                
                )
        return
    
    
    if playsound:
        engine.say(text)
        
        
    engine.runAndWait()
        # engine.stop()
    if filename + str(output_folder) != "":
        if str(output_folder) == "":
            
            # have no extension
            if filename[-4] not in [".mp3",".wav"]:
                outpath = filename + ".mp3"
            else:
                outpath = filename
        else:
            if filename[-4] not in [".mp3",".wav"]:
                outpath = str(output_folder) + "\\" + filename + ".mp3"
            else:
                outpath = str(output_folder) + "\\" + filename
        # engine.save_to_file(text, filename)
        engine.save_to_file(text, outpath)

    # when there's something to save
    


def detect_language(input_text: Union[str,list[str]], 
                    return_as: Literal["full_name","2_chr_code","3_chr_code","langcodes_obj"] = "full_name"):
    import pandas as pd
    from langdetect import detect
    import langcodes
    # medium tested
    # wrote < 30 min(with testing)
    if isinstance(input_text, str):
    # assume only 1d list
        try:
            # Detect the language of the text
            # language_code is 2 character code
            lang_code_2chr = detect(input_text)
            language_obj = langcodes.get(lang_code_2chr)
            language_name = language_obj.display_name()
            lang_code_3chr = language_obj.to_alpha3()

            
            if return_as in ["full_name"]:
                ans = language_name
            elif return_as in ["2_chr_code"]:
                ans = lang_code_2chr
            elif return_as in ["3_chr_code"]:
                ans = lang_code_3chr
            elif return_as in ["langcodes_obj"]:
                ans = language_obj

            return ans
        except Exception as e:
            err_str = f"Language detection failed: {str(e)}"
            return False
        
    elif isinstance(input_text, list):
        out_list = []
        for text in input_text:
            detect_lang = detect_language(text, return_as = return_as)
            out_list.append(detect_lang)
        return out_list
    elif isinstance(input_text, pd.Series):
        # not tested this part yet
        unique_text = pd.Series(input_text.unique()).dropna(how="all")
        unique_text = unique_text.loc[unique_text != False]
        unique_text = unique_text.astype(str)
        data_types_check = unique_text.apply(lambda x: type(x).__name__)
        full_text = unique_text.str.cat(sep=' ')
        detect_lang = detect_language(full_text,return_as)
        return detect_lang

def audio_from_df(df: pd.DataFrame,
                  audio_col:str,
                  output_folder:Union[str,Path] = "", 
                  filename_col:str = None,
                  
                  ):
    
    if filename_col is None:
        filename_col_in = audio_col
    else:
        filename_col_in = filename_col
        
    language = detect_language(df[audio_col])
    # for testing avalibility of the tts(keyboard in your pc)
    n_rows = df.shape[0]
    
    digit_rows = len(str(n_rows))
    
    
    engine = engine_by_lang(language)
    if engine is False:
        raise Exception(f"Doesn't have '{language}' in the keyboard system. Please download this language in your keyboard. ")
    
    df_copy = df.copy()
    
    df_copy.reset_index(drop=True, inplace=True)
    df_copy.index += 1
    df_copy['chosen_filename'] = df_copy.index.map(lambda x: f"{str(x).zfill(digit_rows)}") + "_" + df_copy[filename_col_in]
    
    df_copy.apply(lambda row: create_audio(
        text = row[audio_col],
        filename = row['chosen_filename'],
        language = language,
        playsound = False,
        output_folder = output_folder
        ) ,
        axis = 1)

def create_audio_folder():
    pass
    
################################## Testing #######################
    
def test_create_audio():
    # still doesn't work in VSCode(didn't create audio as files),
    
    # seems like it's because of the path format
    # if I only use the output file(.mp3 only) it would create the audio normally
    language = "french"

    text_list = ["les pâtes", "la sauce", "le bonbon", "l'oignon ", "la carotte"]
    output_folder = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 02\01 OutputData\test_create_audio"
    
    text_list02 = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
    meaning_list02 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # test for 00 format
    text_list03 = ["le haricot", "la viande", "la tomate", "le sandwich", "la baguette", "la soupe", "tu bois", "l'eau ", "l'alcool ", "l'oeuf ", "la salade", "ils boivent", "le riz"]


    
    for text in text_list:
        create_audio(text,language,filename = text + ".mp3",playsound=True,output_folder = output_folder)
    
    # test for list
    create_audio(
        text = text_list02,
        language = language,
        filename = meaning_list02,
        output_folder = output_folder,
        playsound = True,
        )
    
    # test for 00 format
    create_audio(
        text = text_list03,
        language = language,
        
        output_folder = output_folder,
        playsound = True,
        )
    
    
    

def test_detect_language():
    
    texts = [
        "Hello, how are you?",
        "Hallo, wie geht es dir?",
        "Hola, ¿cómo estás?",
        "今日はどうですか？",
        "Привет, как дела?"
    ]
    
    detect_language(texts)

def test_audio_from_df():
    
    excel_path = r"C:\Users\Heng2020\OneDrive\D_Documents\_Learn Languages\_LearnLanguages 02 Main\Duolingo\Duolingo French 02.xlsm"
    sheet_name = "python_test"
    out_folder = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 02\01 OutputData\test_audio_from_df"
    vocab_df = ds.pd_read_excel(excel_path,sheet_name=sheet_name)
    
    audio_from_df(vocab_df,'French',out_folder)
    

def duolingo_pilot():
    
    excel_path = r"C:\Users\Heng2020\OneDrive\D_Documents\_Learn Languages\_LearnLanguages 02 Main\Duolingo\Duolingo French 02.xlsm"
    
    out_folder01 = r"H:\D_Music\_Learn Languages\French\Local TTS generated\Duolingo\Food"
    
    out_folder02 = r"H:\D_Music\_Learn Languages\French\Local TTS generated\Duolingo\Animal"
    
    vocab_df01 = ds.pd_read_excel(excel_path,sheet_name="Food")
    audio_from_df(vocab_df01,'French',out_folder01,filename_col="filename")
    
    vocab_df02 = ds.pd_read_excel(excel_path,sheet_name="Animal")
    audio_from_df(vocab_df02,'French',out_folder02,filename_col="filename")

def test_create_audio_folder():
    import py_string_tool as pst
    import dataframe_short as ds
    excel_path = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 02\NLP_2024\NLP 11_Local_TTS\Duolingo French 02.xlsm"
    sheet_name = "formated"
    out_folder01 = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 02\01 OutputData\test_create_audio_folder"
    
    vocab_df01 = ds.pd_read_excel(excel_path,sheet_name = sheet_name)
    vocab_df01 = vocab_df01.iloc[:,:3]
    vocab_df01 = vocab_df01.iloc[:,1:3]
    vocab_dict_df01 = ds.pd_split_into_dict_df(vocab_df01,add_prefix_index = True)
    test02 = detect_language(vocab_df01.iloc[:,0])
    test = detect_language(vocab_df01.iloc[:,1])
    print("test_create_audio_folder Pass !!!")


def pd_split_into_dict_df(df,add_prefix_index = False):
    # Initialize an empty dictionary to store DataFrames
    # requires: format_index_num
    # imported from C:/Users/Heng2020/OneDrive/D_Code/Python/Python NLP/NLP 02/NLP_2024/NLP 11_Local_TTS
    from collections import OrderedDict
    df_dict = OrderedDict()

    # Find the indices where the first column has a value and the rest are None
    index_list_used = df.index[df.iloc[:, 1:].isnull().all(axis=1) & df.iloc[:, 0].notnull()].tolist()

    # Use the values of the first column as keys and the slices between the found indices as dictionary values
    n_dict = len(index_list_used)
    i = 1
    for start, end in zip(index_list_used, index_list_used[1:] + [None]):  # Adding None to handle till the end of the DataFrame
        format_num = format_index_num(i, n_dict)
        if add_prefix_index:
            key = format_num + "_" + df.iloc[start, 0]  # The key is the value in the first column
        else:
            key = df.iloc[start, 0]
        # Slice the DataFrame from the current index to the next one in the list
        each_df = df.iloc[start+1:end].reset_index(drop=True)
        each_df = each_df.dropna(how='all')
        
        df_dict[key] = each_df
        i += 1
        

    return df_dict

def test_pd_split_into_dict_df():
    # Example DataFrame
    data = {
        'Column1': [None, 'Key1', None, None, 'Key2', None],
        'Column2': [None, None, 1, 2, None, 3],
        'Column3': [None, None, 'A', 'B', None, 'C']
    }
    
    df = pd.DataFrame(data)
    result_dict = pd_split_into_dict_df(df)
    print("test_pd_split_into_dict_df Pass!!!")

def format_index_num(to_format_num, total_num):
    # imported from C:/Users/Heng2020/OneDrive/D_Code/Python/Python NLP/NLP 02/NLP_2024/NLP 11_Local_TTS
    # tested via pd_split_into_dict_df
    # adding leading 0 to the number
    # Determine the number of digits in the largest number
    total_digits = len(str(total_num))
    
    # Format the number with leading zeros
    formatted_num = f"{to_format_num:0{total_digits}d}"
    
    return formatted_num

test_pd_split_into_dict_df()
    

test_create_audio_folder()
# test_create_audio()
# test_audio_from_df()
duolingo_pilot()




