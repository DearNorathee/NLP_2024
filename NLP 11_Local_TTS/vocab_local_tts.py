# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 11:48:59 2024

@author: Heng2020
"""


# import excel_tool as xt
# import excel_tool.range as rg

# NEXT: set up French vocab process
# add alarm to test_create_audio_folder
# turn test_create_audio_folder into function create_audio_folder

import pyttsx3
import sys

from typing import Literal,Union,List

import dataframe_short as ds
import pandas as pd
from pathlib import Path
import py_string_tool as pst


excel_path = r"C:\Users\Heng2020\OneDrive\D_Documents\_Learn Languages\_LearnLanguages 02 Main\Duolingo\Duolingo French 02.xlsm"

sheet_name = "python_test"

# vocab_df = ds.pd_read_excel(excel_path,sheet_name=sheet_name)

#%%
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
        raise ValueError(f"Doesn't have '{language_in}' in the keyboard system. Please download this language in your keyboard. ")
    
    if isinstance(text, list):
        
        if isinstance(filename, list):
            if len(text) != len(filename):
                raise ValueError(f"The length of text is: {len(text)}. The length of filename is {len(filename)}. Make sure they have the same length.")
            
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
                  language:str = "auto",
                  add_prefix_number: bool = True,
                  ) -> None:
    """
    This already include the prefix number
    
    # haven't test when add_prefix_number = False,
    
    Parameters
    ----------
    df : pd.DataFrame
        DESCRIPTION.
    audio_col : str
        DESCRIPTION.
    output_folder : Union[str,Path], optional
        DESCRIPTION. The default is "".
    filename_col : str, optional
        DESCRIPTION. The default is None.
    language : str, optional
        DESCRIPTION. The default is "auto".

    Returns
    -------
    None.

    """
    if filename_col is None:
        filename_col_in = audio_col
    else:
        filename_col_in = filename_col
    
    if language in ["auto"]:
        language_in = detect_language(df[audio_col])
    else:
        language_in = language
    # for testing avalibility of the tts(keyboard in your pc)
    n_rows = df.shape[0]
    
    digit_rows = len(str(n_rows))
    
    
    engine = engine_by_lang(language_in)
    if engine is False:
        raise ValueError(f"Doesn't have '{language_in}' in the keyboard system. Please download this language in your keyboard. ")
    
    df_copy = df.copy()
    
    df_copy.reset_index(drop=True, inplace=True)
    df_copy.index += 1
    
    df_copy['chosen_filename'] = df_copy.index.map(lambda x: f"{str(x).zfill(digit_rows)}") + "_" + df_copy[filename_col_in]
    
    
    if add_prefix_number:
        chosen_col = 'chosen_filename'
    else:
        chosen_col = filename_col
    
    
    df_copy.apply(lambda row: create_audio(
        text = row[audio_col],
        filename = row[chosen_col],
        language = language_in,
        playsound = False,
        output_folder = output_folder
        ) ,
        axis = 1)

def create_audio_folder(excel_path,sheet_name):
    import excel_tool as xt
    import excel_tool.worksheet as ws
    vocab_df = ds.pd_read_excel(excel_path,sheet_name = sheet_name)
    vocab_dict_df = ds.pd_split_into_dict_df(vocab_df,add_prefix_index = True)
    
    first_df = vocab_dict_df['01_Basics 1']


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

def format_index_num(to_format_num, total_num):
    # imported from C:/Users/Heng2020/OneDrive/D_Code/Python/Python NLP/NLP 02/NLP_2024/NLP 11_Local_TTS
    # tested via pd_split_into_dict_df
    # adding leading 0 to the number
    # Determine the number of digits in the largest number
    total_digits = len(str(total_num))
    
    # Format the number with leading zeros
    formatted_num = f"{to_format_num:0{total_digits}d}"
    
    return formatted_num

# pd_read_excel doesn't seem to work properly so I will modify to make it work here
# then more testing need to be done before immigrate this to main lib
def pd_read_excel(filepath, sheet_name=0, header_row=1, start_row=None, end_row=None):
    import pandas as pd
    import xlwings as xw
    import numpy as np
    # Hard for both Cluade3 & GPT4
    # medium tested
    # took about 1.5 hr(include testing)
    """
    
    Read an Excel file into a Pandas DataFrame.

    Args:
        filepath (str): Path to the Excel file.
        sheet_name (int or str, optional): Name or index of the sheet to read. Default is 0.
        header_row (int or None, optional): Row number to use as the column names. If None, no header row is used. Default is 1.
        start_row (int or None, optional): Row number to start reading data. If None, start from the beginning. Default is None.
        end_row (int or None, optional): Row number to stop reading data. If None, read until the end. Default is None.

    Returns:
        Tuple containing:
            - pandas.DataFrame: The data read from the Excel file.
            - pandas.Series: The header row as a Series.
    """
    # header_row is False or None
    if header_row in [False,None] :
        header = False
    else:
        header = 1

    wb = xw.Book(filepath)
    sheet = wb.sheets[sheet_name]

    used_range = sheet.used_range

    # Convert the used range to a Pandas DataFrame
    df_read_ori = used_range.options(pd.DataFrame, header=header, index=False).value

    # Get the header row as a Series
    header_row_df = df_read_ori.iloc[[header_row - 2]]

    # Slice the DataFrame based on start_row and end_row
    if start_row is None:
        start_row_in = 0
    else:
        start_row_in = start_row -2 # Adjust for 0-based indexing and header row

    if end_row is None:
        df_info = df_read_ori.iloc[start_row_in:, :]
    else:
        end_row_in = end_row - 1  # Adjust for 0-based indexing
        df_info = df_read_ori.iloc[start_row_in:end_row_in, :]

    # Combine the header row and data into a single DataFrame
    out_df = pd.concat([header_row_df, df_info], ignore_index=True)
    out_df.columns = out_df.iloc[0]
    out_df = out_df[1:]
    out_df.reset_index(drop=True, inplace=True)

    return out_df

def rename_col_by_index(df, index, new_name, inplace=True):
    """
    medium tested
    Rename a column in a DataFrame based on its index (this can handle repeated name)

    Parameters:
    df (pd.DataFrame): The DataFrame whose column you want to rename.
    index (int): The index of the column to rename.
    new_name (str): The new name for the column.
    inplace (bool): If True, modifies the DataFrame in place (default is True).

    Returns:
    pd.DataFrame or None: The DataFrame with the renamed column if inplace is False, otherwise None.
    """
    # Ensure the index is within the valid range
    if not 0 <= index < len(df.columns):
        raise IndexError("Column index out of range.")
    
    # Copy df if not inplace
    if not inplace:
        df = df.copy()
    
    # Set new column name
    df.columns = df.columns[:index].tolist() + [new_name] + df.columns[index+1:].tolist()
    
    if not inplace:
        return df

# Sub
def create_folders(folder: Union[str, Path], 
                   name_list: List[str], 
                   replace: bool = True) -> None:
    import os
    import shutil
    """
    Create directories in the specified folder based on names provided in name_list.

    Parameters:
    folder (Union[str, Path]): The path where the directories will be created.
    name_list (List[str]): A list of directory names to create.

    Returns:
    None
    """
    
    # Ensure the folder path is a Path object
    folder = Path(folder)
    
    # Iterate through the list of names and create each folder
    for name in name_list:
        dir_path = folder / name  # Construct the full path for the new directory
        if not dir_path.exists():  # Check if the directory already exists
            os.makedirs(dir_path)  # Create the directory if it does not exist
            # print(f"Created directory: {dir_path}")
        else:
            if replace:
                shutil.rmtree(dir_path)
                os.makedirs(dir_path) 
                print(f"Directory already exists and replaced: {dir_path}")
            else:
                print(f"Directory already exists: {dir_path}")
                
#%%
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
    
    excel_path = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 02\NLP_2024\NLP 11_Local_TTS\Duolingo French 02.xlsm"
    
    out_folder01 = r"H:\D_Music\_Learn Languages\French\Local TTS generated\Duolingo\Food"
    
    out_folder02 = r"H:\D_Music\_Learn Languages\French\Local TTS generated\Duolingo\Animal"
    # French column seems to be missing when read using ds.pd_read_excel
    vocab_df01 = ds.pd_read_excel(excel_path,sheet_name="Food")
    audio_from_df(vocab_df01,'French',out_folder01,filename_col="filename")
    
    vocab_df02 = ds.pd_read_excel(excel_path,sheet_name="Animal")
    audio_from_df(vocab_df02,'French',out_folder02,filename_col="filename")

def test_create_audio_folder():
    # specify column manually for now
    # will change this to proper function later
    # based on pd. 2.1.3
    import py_string_tool as pst
    import dataframe_short as ds
    from tqdm import tqdm
    from playsound import playsound
    from pathlib import Path
    
    excel_path = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 02\NLP_2024\NLP 11_Local_TTS\Duolingo French 02.xlsm"
    sheet_name = "formated"
    out_folder01 = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 02\01 OutputData\test_create_audio_folder\test_01"
    
    vocab_df01 = ds.pd_read_excel(excel_path,sheet_name = sheet_name)
    vocab_df02 = vocab_df01.iloc[:,:3]
    vocab_df02 = vocab_df01.iloc[:,1:3]
    vocab_dict_df01 = ds.pd_split_into_dict_df(vocab_df02,add_prefix_index = True)
    test02 = detect_language(vocab_df01.iloc[:,0])
    test = detect_language(vocab_df01.iloc[:,1])
    
    chapter_limit = 10
    chapter_limit = "all"

    chapter_limit_in = chapter_limit if isinstance(chapter_limit,int) else len(vocab_dict_df01.items())
    chosen_index = 0
    # use 0-index to refer to OrderDictt
    curr_df = list(vocab_dict_df01.items())[0][1]
    
    chapter_list = list(vocab_dict_df01.keys())
    create_folders(out_folder01, chapter_list)
    
    progress_bar = tqdm(total=chapter_limit_in)
    i = 0
    for key,value in tqdm(vocab_dict_df01.items()):
        if i > chapter_limit_in:
            break
        chapter = key
        out_chapter_folder = Path(out_folder01) / chapter
        # out_chapter_folder_str just for debugging
        out_chapter_folder_str = str(out_chapter_folder)
        curr_df = value.copy()
        rename_col_by_index(curr_df,0,"French")
        rename_col_by_index(curr_df,1,"English")
        
        try:
            # first_df.rename(columns={first_df.columns[0]: 'French'}, inplace=True)
            # first_df.rename(columns={first_df.columns[1]: 'English'}, inplace=True)
            n_digit = len(str(curr_df.shape[0]))
            curr_df['formatted_index'] = (curr_df.index + 1).astype(str).str.zfill(n_digit)
            curr_df['English'] = curr_df['English'].astype(str)
            curr_df['filename_dirty'] =  curr_df['French'] + '_' + curr_df['English']
            curr_df['filename'] = curr_df.apply(
                lambda row: pst.clean_filename(row['filename_dirty']),
                axis = 1)
            
            audio_from_df(curr_df, 
                          audio_col = "French",
                          output_folder = out_chapter_folder,
                          filename_col = 'filename' ,
                          
                          )
        except ValueError:
            print(f"Error at chapter: {chapter}")
        i += 1
        progress_bar.update(1)
             
    print("test_create_audio_folder Pass !!!")
    print("Don't forget to rename your folder is generating is successfull !!!")



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


def create_basic_present():
    output_folder = r"H:\D_Music\_Learn Languages\French\Forvo\01 Basic Present"
    have_FR = ["j'ai","tu as", "il a", "elle a", "on a","nous avons" ,"vous avez", "ils ont", "elles ont" ]
    
    have_filename = ["I have_j'ai","You(sg) have_tu as", "He has_il a", "She has_elle a", "One has_on a","We have_nous avons", 
                     "You(pl) have_vous avez", "They(m) have_ils ont", "They(f) have_elles ont" ]
    
    be_FR = ["chui","tu es", "il est", "elle est", "on est","nous sommes", "vous êtes", "ils sont", "elles sont" ]
    
    be_filename = ["I am_je suis","You(sg) are_tu es", "He is_il est", "She is_elle est", "One is_on est","We are_nous sommes", 
                     "You(pl) are_vous êtes", "They(m) are_ils sont", "They(f) are_elles sont"  ]
    
    go_FR = ["je vais","tu vas", "il va", "elle va", "on va","nous allons", "vous allez", "ils vont", "elles vont" ]
    
    go_filename = ["I go_je vais","You(sg) go_tu vas", "He goes_il va", "She goes_elle va", "One goes_on va","We go_nous allons", 
                     "You(pl) go_vous allez", "They(m) go_ils vont", "They(f) go_elles vont"  ]
    
    all_verbs_FR = have_FR + be_FR + go_FR
    all_filename = have_filename + be_filename + go_filename
    
    create_audio(all_verbs_FR,language = "French",filename=all_filename,output_folder=output_folder)

create_basic_present()


test_pd_split_into_dict_df()
    

test_create_audio_folder()
# test_create_audio()
# test_audio_from_df()
duolingo_pilot()




