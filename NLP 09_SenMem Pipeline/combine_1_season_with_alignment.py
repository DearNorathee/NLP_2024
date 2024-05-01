# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 09:35:42 2024

@author: Heng2020

right before sen alignment I would like to add this feature
1) remove <i>, </i>
2) Split row when there's "- "
3) remove (UPPERCASE INSIDE PARENTHESIS)
"""

# NEXT: main alignment for whole season is done
# may need more testing but ready for testing for production



from typing import Literal, Union

import regex
import pandas as pd
import seaborn as sns
import re
import os
from pathlib import Path
import sys

sys.path.append(r'C:\Users\Heng2020\OneDrive\Python MyLib\Python MyLib 01\02 DataFrame')
sys.path.append(r'C:\Users\Heng2020\OneDrive\Python MyLib\Python MyLib 01\06 General Python')
sys.path.append(r'C:\Users\Heng2020\OneDrive\Python MyLib\Python MyLib 01\09 NLP_lib')
sys.path.append(r'C:\Users\Heng2020\OneDrive\Python MyLib\Python MyLib 01\10 OS')

import lib02_dataframe as ds
import video_tools as vt
import python_wizard01 as pw
import os_01 as ost



def combine_files_to_Excel():
    pass

def make_1_season_Excel_unaligned(EN_folder_path: Union[str,Path],
                                  PT_folder_path: Union[str,Path], 
                                  out_excel_name: Union[str,Path],
                                  output_folder = None,
                                  drop_timestamp = True,
                                  ):
    # medium tested
    # based on pd. 2.1.3
    # imported from NLP 09_SenMem Pipeline
    """
    

    Parameters
    ----------
    EN_folder_path : TYPE
        the path contains many Excel files of script in 1 episode(in English)
    PT_folder_path : TYPE
        the path contains many Excel files of script in 1 episode(in Portuguese)
    out_excel_name : TYPE
        DESCRIPTION.
    output_folder : TYPE
        DESCRIPTION.
     : TYPE
        DESCRIPTION.
    
    drop_timestamp: remove the timestamp from the output script
    (Not implemented)

    Returns
    -------
    out_df : TYPE
        DESCRIPTION.

    """
    import pandas as pd
    import sys
    from pathlib import Path
    
    sys.path.append(r'C:\Users\Heng2020\OneDrive\Python MyLib\Python MyLib 01\02 DataFrame')
    sys.path.append(r'C:\Users\Heng2020\OneDrive\Python MyLib\Python MyLib 01\06 General Python')
    sys.path.append(r'C:\Users\Heng2020\OneDrive\Python MyLib\Python MyLib 01\09 NLP_lib')
    sys.path.append(r'C:\Users\Heng2020\OneDrive\Python MyLib\Python MyLib 01\10 OS')
    
    import lib02_dataframe as ds
    import video_tools as vt
    import python_wizard01 as pw
    import os_01 as ost
    
    en_df = vt.combine_files_1_season(str(EN_folder_path))
    en_df = en_df.add_suffix('_EN')
    # en_df.rename(columns = {'sentence':'sentence_EN',
    #                                 'start':'start_EN',
    #                                 'end':'end_EN',
    #                                 'NoSentence':'NoSentence_EN',
    #                                 },
    #              inplace = True,
                 
    #              )
    en_df["Episode"] = en_df["Episode_EN"]
    en_df = en_df.drop(columns = ["Episode_EN"])
    
    en_df['NoSentence_EN'] = en_df['NoSentence_EN'].astype('int')
    en_df['NoSentence_EN'] = en_df['NoSentence_EN'] + 1
    en_df = en_df.reset_index(drop = True)



    pt_df = vt.combine_files_1_season(str(PT_folder_path))
    pt_df = pt_df.add_suffix('_PT')
    pt_df["Episode"] = pt_df["Episode_PT"]
    pt_df = pt_df.drop(columns = ["Episode_PT"])
    # pt_df.rename(columns = {'sentence':'sentence_PT',
    #                                 'start':'start_PT',
    #                                 'end':'end_PT',
    #                                 'NoSentence':'NoSentence_PT',
    #                                 },
    #              inplace = True,
    #              )
    pt_df['NoSentence_PT'] = pt_df['NoSentence_PT'].astype('int')
    pt_df['NoSentence_PT'] = pt_df['NoSentence_PT'] + 1
    pt_df = pt_df.reset_index(drop = True)

    out_df:pd.DataFrame

    pt_df_music = pt_df[pt_df['sentence_PT'].str.contains('♪', na=False) ]
    en_df_music = en_df[en_df['sentence_EN'].str.contains('♪', na=False) ]


    # Filter out rows where 'Column1' contains '♪'
    en_df_filter = en_df[~en_df['sentence_EN'].str.contains('♪', na=False)]
    pt_df_filter = pt_df[~pt_df['sentence_PT'].str.contains('♪', na=False)]
    en_df_music = en_df_filter[en_df_filter['sentence_EN'].str.contains('♪', na=False) ]


    out_df = ds.indexAlignedAppend(en_df_filter,pt_df_filter,"Episode")
    out_df = out_df.reset_index(drop = True)
    out_df.index = out_df.index + 1
    # keep only the first occurrence of each column (Episode is duplicated)
    out_df = out_df.loc[:, ~out_df.columns.duplicated()]
    
    # automatically add .xlsx extension to the file 
    out_excel_name_in = out_excel_name if ".xlsx" in out_excel_name else (out_excel_name + ".xlsx")
    
    ds.pd_move_col_front(out_df, "Episode")
    
    if output_folder is None:
        out_excel_path = str(out_excel_name_in)
    else:
        out_excel_path = str(Path(output_folder) / Path(out_excel_name_in))
    
    if drop_timestamp:
        out_df = out_df.drop(columns = ['start_EN','end_EN','start_PT','end_PT'])
    
    out_df['Episode'] = out_df['Episode'].ffill()
    out_df.to_excel(str(out_excel_path))
    
    return out_df

# read the link here of how to use Lingtrain
# https://habr.com/ru/articles/586574/

def read_sentences_from_excel(file_path, sheet_name, portuguese_col, english_col, nrows=None):
    # imported from NLP 09_SenMem Pipeline
    """
    Reads Portuguese and English sentences from an Excel file.
    
    :param file_path: Path to the Excel file.
    :param sheet_name: Name of the sheet containing the sentences.
    :param portuguese_col: Column letter for Portuguese sentences.
    :param english_col: Column letter for English sentences.
    :return: Tuple of two lists containing Portuguese and English sentences.
    """

    df = ds.pd_read_excel(file_path,sheet_name=sheet_name,nrows=nrows,usecols=[portuguese_col,english_col])

    portuguese_sentences = df.iloc[:,0].tolist()
    english_sentences = df.iloc[:,1].tolist()


    return portuguese_sentences, english_sentences

    
def read_movie_script2(file_path, sheet_name = "Sheet1", portuguese_col = 0, english_col = 1):
    # imported from NLP 09_SenMem Pipeline
    # middle tested 
    # dependency: pd_by_column, pd_split_into_dict_df, pd_regex_index
    # work with format that use title to seperate the episode
    import pandas as pd
    import re
    from openpyxl.utils import column_index_from_string
    
    # Load the dataset from the Excel file
    
    if pw.is_convertible_to_num(portuguese_col):
        portuguese_col_no = int(portuguese_col)
    else:
        portuguese_col_no = column_index_from_string(portuguese_col) - 1
        
    
    if pw.is_convertible_to_num(english_col):
        english_col_no = int(english_col)
    else:
        english_col_no = column_index_from_string(english_col) - 1
    
    # If it's the column name eg A, G,H
    
    data_ori = ds.pd_read_excel(file_path, sheet_name=sheet_name)
    # playsound(alarm_path)
    
    data = ds.pd_by_column(data_ori,[portuguese_col_no, english_col_no])
    

    # Function to check if a cell value matches the episode identifier pattern (e.g., S01E01)
    # r'[Ss]\d{2}[Ee]\d{2}' => S01E01
    df_dict = ds.pd_split_into_dict_df(data,r'[Ss]\d{2}[Ee]\d{2}',0)
    # df_dict = pd_split_into_dict_df(data,index_list=episode_start_indices)
    return df_dict


def read_movie_script(file_path, sheet_name, portuguese_col, english_col):
    # the main function that I should use from now on
    # imported from NLP 09_SenMem Pipeline
    from openpyxl.utils import column_index_from_string
    df = ds.pd_read_excel(file_path, sheet_name=sheet_name)
    # df = pd_by_column(df_ori, [portuguese_col,english_col])
    import pandas as pd
    """
    Extracts content from a DataFrame based on 'Episode' information.

    Parameters
    ----------
    df : pandas.DataFrame
        The original DataFrame containing an 'Episode' column with format 'SxxExx',
        and columns for content ('sentence_PT', 'sentence_EN').

    Returns
    -------
    pandas.DataFrame
        A new DataFrame with 'season' and 'episode' as MultiIndex.
        Each row contains a DataFrame in the 'content' column, which itself
        contains 'sentence_PT' and 'sentence_EN' from the original DataFrame.

    Examples
    --------
    >>> main_df = pd.DataFrame({
    ...     'Episode': ['S06E08', 'S06E08', 'S01E01'],
    ...     'sentence_PT': ['sentence1_PT', 'sentence2_PT', 'sentence3_PT'],
    ...     'sentence_EN': ['sentence1_EN', 'sentence2_EN', 'sentence3_EN']
    ... })
    >>> read_movie_script2(main_df)
    """
    
    if pw.is_convertible_to_num(portuguese_col):
        portuguese_col_no = int(portuguese_col)
    else:
        portuguese_col_no = column_index_from_string(portuguese_col) - 1
        
    
    if pw.is_convertible_to_num(english_col):
        english_col_no = int(english_col)
    else:
        english_col_no = column_index_from_string(english_col) - 1
    
    # Extract season and episode numbers from the 'Episode' column
    df['season'] = df['Episode'].str.extract(r'S(\d+)E\d+').astype(int)
    df['episode'] = df['Episode'].str.extract(r'S\d+E(\d+)').astype(int)
    
    # Prepare the data for the new DataFrame
    data = []
    
    # Group by 'season' and 'episode', then iterate over each group
    for (season, episode), group in df.groupby(['season', 'episode']):
        # Create a DataFrame for this group's content
        content_df = ds.pd_by_column(group, [portuguese_col_no, english_col_no]).reset_index(drop=True)
        
        # Append season, episode, and content DataFrame to the list
        data.append({'season': season, 'episode': episode, 'content': content_df})
    
    # Convert the list to a DataFrame
    new_df = pd.DataFrame(data)
    
    # Set 'season' and 'episode' as the index
    new_df.set_index(['season', 'episode'], inplace=True)
    
    return new_df


def align_1_season(excel_1_season_script,
                   out_excel_name: Union[str,Path],
                   output_folder = None,
                   sheet_name = 'Sheet1',
                   
                   n_episodes: Union[str,int] = "all",
                   portuguese_col = "F",
                   english_col = "D",
                   lang_from="PT",
                   lang_to="EN",
                   alarm = True,
                   alarm_path = r"H:\D_Music\Sound Effect positive-logo-opener.mp3",
                   
                   ) -> pd.DataFrame:
    
    # imported from NLP 09_SenMem Pipeline
    """
    
    it would take about 1.2 min per 1 episode of BigBang(20 min)
    about 20 min in 1 whole season
    
    create the Excel file for "aligned" sentences for 1 season for series

    Parameters
    ----------
    excel_1_season_script : TYPE
        Excel that has 1 sheet containing all episodes script
        
    out_excel_name : Union[str,Path]
        output Excel name, only ".xlsx" supported at the moment
        
    output_folder : TYPE, optional
        DESCRIPTION. The default is None.
    sheet_name : TYPE, optional
        DESCRIPTION. The default is 'Sheet1'.
    portuguese_col : TYPE, optional
        DESCRIPTION. The default is "F".
    english_col : TYPE, optional
        DESCRIPTION. The default is "D".
    lang_from : TYPE, optional
        DESCRIPTION. The default is "PT".
    lang_to : TYPE, optional
        DESCRIPTION. The default is "EN".

    Returns
    -------
    you need to set this saved as variable otherwise it would output df.head()
    it would export the Excel file and return pd.df at the same time
    pd.DataFrame

  """
    
    import pandas as pd
    import time
    from playsound import playsound
    from tqdm import tqdm
    
    episode_aligned: pd.DataFrame
    
    ts_start = time.perf_counter()
    
    df_script = read_movie_script(excel_1_season_script, sheet_name, portuguese_col, english_col)
    season_aligned = pd.DataFrame()
    ts_read  = time.perf_counter()
    error_episode = []
    
    
    
    # using 1-index system
    i = 1
    for curr_index in df_script.index:
        
        if isinstance(n_episodes, int):
            if i > n_episodes:
                break
            
        season, episode = curr_index
        episode_str = f'S{season:02d}E{episode:02d}'
        single_episode = df_script.loc[curr_index,"content"]
        
        try:
            
            # slow from here
            episode_aligned = sen_alignment_df(single_episode,lang_from=lang_from,lang_to=lang_to,alarm = False)
    
            episode_aligned.index = episode_aligned.index + 1
            episode_aligned['sentence_' + lang_from  ] = episode_aligned[lang_from]
            episode_aligned['sentence_' + lang_to  ] = episode_aligned[lang_to]
            
            episode_aligned = episode_aligned.drop(columns = [lang_from,lang_to])
            
            episode_aligned['Season'] =  season
            episode_aligned['Episode'] =  episode
            episode_aligned = episode_aligned.drop_duplicates(subset=['sentence_' + lang_from ,'sentence_' + lang_to])
            ds.pd_move_col_front(episode_aligned, ['Season','Episode'])
            # drop rows that are empty
            episode_aligned = episode_aligned.dropna(subset = ['sentence_' + lang_from] )
            
            season_aligned = pd.concat([season_aligned,episode_aligned])
            print(f"{episode_str} Done Aligning !!! ----------------------------------------")
        except:
            print(f"Error at {episode_str} was found !!! ########################")
            error_episode.append(episode_str)
        
        i += 1
            
    out_excel_name_in = out_excel_name if ".xlsx" in out_excel_name else (out_excel_name + ".xlsx")
    
    
    if output_folder is None:
        out_excel_path = str(out_excel_name_in)
    else:
        out_excel_path = str(Path(output_folder) / Path(out_excel_name_in))
    season_aligned.to_excel(str(out_excel_path))
    
    if len(error_episode) > 0:
        print("Errors occurred at these episodes")
        print(error_episode)
    
    ts_end = time.perf_counter()
    duration_read = ts_read - ts_start
    total_duration = ts_end - ts_start
    # i = counted episodes
    
    avg_per_ep = total_duration / i
    avg_per_ep /= 60
    print("Total processing time")
    pw.print_time(total_duration)
    
    print(f"{total_duration:.2f} min per episode")    
    if alarm:
        playsound(alarm_path)
    
    return season_aligned


def sen_alignment_df(df, lang_from = None, lang_to = None,
                       alarm = True,
                       alarm_path = r"H:\D_Music\Sound Effect positive-logo-opener.mp3",
                     ):
    # medium tested
    if lang_from is None: lang_from = df.columns[0]
    if lang_to is None: lang_to = df.columns[1]
    
    text_list_from = df.iloc[:, 0].tolist()
    text_list_to = df.iloc[:, 1].tolist()
    # assume that text from is
    result = sentence_alignment(text_list_from,text_list_to,lang_from,lang_to,alarm=alarm,alarm_path=alarm_path)
    
    return result
    

def sentence_alignment(text_from,text_to, lang_from = "pt", lang_to = "en",
                       alarm = True,
                       alarm_path = r"H:\D_Music\Sound Effect positive-logo-opener.mp3",
                       
                       ):
    # v02 => add alarm parameter
    # text_from, text_to are expected to be text or list
    # medium tested, seem to work pretty well now
    
    import os
    from lingtrain_aligner import preprocessor, splitter, aligner, resolver, reader, helper, vis_helper
    from pathlib import Path
    import lingtrain_aligner
    from playsound import playsound
    import numpy as np
    from time import time
    

    
    db_name = "book.db"
    
    db_path = folder / db_name

    
    models = ["sentence_transformer_multilingual", "sentence_transformer_multilingual_labse"]
    model_name = models[0]
    
    # convert to list of text_from,text_to is not list
    
        
    ts01 = time()
    if not isinstance(text_from, list):
        text1_prepared = preprocessor.mark_paragraphs(text1)
        splitted_from = splitter.split_by_sentences_wrapper(text1_prepared, lang_from)
    else:
        splitted_from = [str(x) for x in text_from if x is not np.nan ]
        # splitted_from = splitter.split_by_sentences_wrapper(text_from, lang_from)
    
    if not isinstance(text_to, list):
        
        text2_prepared = preprocessor.mark_paragraphs(text2)
        splitted_to = splitter.split_by_sentences_wrapper(text2_prepared, lang_to)
    else:
        splitted_to = [str(x) for x in text_to if x is not np.nan ]
        # splitted_to = splitter.split_by_sentences_wrapper(text_to, lang_to)

    # temp adding title, author, h1, h2 to make it work first,.... we'll look into it when this is not avaliable later
    
    
    # if lang_from == "pt" and lang_to == "en":
    #     marker = ["(No title)%%%%%title." , 
    #                "(No author)%%%%%author.", 
    #                "(No header_)%%%%%h1.", 
    #                "(No header_)%%%%%h2."]
    #     splitted_from = marker + splitted_from
    #     splitted_to = marker + splitted_to
        
        
    # Create the database and fill it.
    if os.path.isfile(db_path):
        os.unlink(db_path)
        
    aligner.fill_db(db_path, lang_from, lang_to, splitted_from, splitted_to)
    
    # batch_ids = [0,1]
    
    aligner.align_db(db_path, \
                    model_name, \
                    batch_size=100, \
                    window=40, \
                    # batch_ids=batch_ids, \
                    save_pic=False,
                    embed_batch_size=10, \
                    normalize_embeddings=True, \
                    show_progress_bar=True
                    )
    pic_name = "alignment_vis.png"
    pic_path = folder / pic_name
    vis_helper.visualize_alignment_by_db(db_path, output_path=pic_path, lang_name_from=lang_from, lang_name_to=lang_to, batch_size=400, size=(800,800), plt_show=True)
    
    # Explore the conflicts
    
    conflicts_to_solve, rest = resolver.get_all_conflicts(db_path, min_chain_length=2, max_conflicts_len=6, batch_id=-1)
    
    resolver.get_statistics(conflicts_to_solve)
    resolver.get_statistics(rest)
    
    # resolver.show_conflict(db_path, conflicts_to_solve[8])
    
    
    steps = 10
    batch_id = -1 
    
    for i in range(steps):
        conflicts, rest = resolver.get_all_conflicts(db_path, min_chain_length=2+i, max_conflicts_len=6*(i+1), batch_id=batch_id)
        resolver.resolve_all_conflicts(db_path, conflicts, model_name, show_logs=False)
        vis_helper.visualize_alignment_by_db(db_path, output_path="img_test1.png", lang_name_from=lang_from, lang_name_to=lang_to, batch_size=400, size=(600,600), plt_show=True)
    
        if len(rest) == 0: break
    
    paragraphs = reader.get_paragraphs(db_path)[0]
    
    paragraph_from_2D = paragraphs['from']
    paragraph_to_2D = paragraphs['to']

    paragraph_from_result = [item for list_1D in paragraph_from_2D for item in list_1D]
    paragraph_to_result = [item for list_1D in paragraph_to_2D for item in list_1D]
    
    paragraph_result = pd.DataFrame({lang_from:paragraph_from_result,
                                     lang_to:paragraph_to_result
                                     })
    
    ts02 = time()
    total_time = ts02-ts01
    pw.print_time(total_time)
    
    if alarm:
        playsound(alarm_path)
    
    return paragraph_result


def test_align_1_season():
    # imported from NLP 09_SenMem Pipeline
    folder = r"C:\Users\Heng2020\OneDrive\Python NLP\NLP 09_SenMem Pipeline"
    filename = r"BigBang S01.xlsx"
    output_name = "BigBang S01_aligned.xlsx"
    
    folderpath = Path(folder)
    file_path = folderpath / filename
    
    ans_df = align_1_season(file_path,output_name,n_episodes = 3)


def test_make_1_season_Excel_unaligned():
    # imported from NLP 09_SenMem Pipeline
    EN_folder_path = r"C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT\_BigBang EN\S01"
    PT_folder_path = r"C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT\_BigBang PT\S01"
    out_excel_name = "BigBang S01.xlsx"
    output_folder = None
    df_test = make_1_season_Excel_unaligned(EN_folder_path,PT_folder_path,out_excel_name,output_folder=output_folder)



# #################### keep this in case weird error happen again ##################



# en_df = vt.combine_files_1_season(EN_folder_path)
# en_df = en_df.rename(columns = {'sentence':'sentence_EN',
#                                 'start':'start_EN',
#                                 'end':'end_EN',
#                                 'NoSentence':'NoSentence_EN',
#                                 } )

# en_df['NoSentence_EN'] = en_df['NoSentence_EN'].astype('int')
# en_df = en_df.reset_index(drop = True)



# pt_df = vt.combine_files_1_season(PT_folder_path)
# pt_df = pt_df.rename(columns = {'sentence':'sentence_PT',
#                                 'start':'start_PT',
#                                 'end':'end_PT',
#                                 'NoSentence':'NoSentence_PT',
#                                 } )
# pt_df['NoSentence_PT'] = pt_df['NoSentence_PT'].astype('int')
# pt_df = pt_df.reset_index(drop = True)

# out_df:pd.DataFrame

# pt_df_music = pt_df[pt_df['sentence_PT'].str.contains('♪', na=False) ]
# en_df_music = en_df[en_df['sentence_EN'].str.contains('♪', na=False) ]


# # Filter out rows where 'Column1' contains '♪'
# en_df_filter = en_df[~en_df['sentence_EN'].str.contains('♪', na=False)]
# pt_df_filter = pt_df[~pt_df['sentence_PT'].str.contains('♪', na=False)]
# en_df_music = en_df_filter[en_df_filter['sentence_EN'].str.contains('♪', na=False) ]


# out_df = ds.indexAlignedAppend(en_df_filter,pt_df_filter,"Episode")

# # keep only the first occurrence of each column (Episode is duplicated)
# out_df = out_df.loc[:, ~out_df.columns.duplicated()]
# out_excel_name = "season01.xlsx"
# out_df.to_excel(out_excel_name)


