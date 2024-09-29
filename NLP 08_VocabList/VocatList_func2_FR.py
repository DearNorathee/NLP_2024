# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 07:23:17 2023

@author: Heng2020
"""

############## This interesting  project is pretty much useless
# Next thing if I decided to continue at all is not incoperate more files but
# include "filter" my KNOWN words

# I did it with GPT4 for 2 days(may be about 10 hrs)

# spacy 3.7.2 needs 
# to have pydantic 1.10.12
# env: latest_python

# check the model name for each langauge here:
    # https://spacy.io/models
    
import warnings
import os

warnings.filterwarnings("ignore", message="'has_mps' is deprecated") # Suppress INFO and WARNING from spacy
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress INFO and WARNING from spacy


import nltk
import spacy
from collections import Counter
import pandas as pd
import seaborn as sns
# import textstat
import matplotlib.pyplot as plt
import warnings
# textstat.set_lang(lang)
import natural_language_processing as nlp
   
path_S06E01 = r"C:\Users\Heng2020\OneDrive\D_Documents\_Learn Languages\Portuguese\_LearnLanguages 04 BigBang PT\_BigBang PT\S06\BigBang S06E01 PT.xlsx"
path_S06E02 = r"C:\Users\Heng2020\OneDrive\D_Documents\_Learn Languages\Portuguese\_LearnLanguages 04 BigBang PT\_BigBang PT\S06\BigBang S06E02 PT.xlsx"

path01 = r"C:/Users/Heng2020/OneDrive/D_Code/Python/Python NLP/NLP 01/NLP 08_VocabList/O Google CRIOU um ROBÔ CONSCIENTE.txt"

path_list = [f"BigBang S06E{i:02}.xlsx" for i in range(1,25)]

input_sentence = pd.read_excel(path_S06E01)[['sentence']]
single_text = ' '.join(input_sentence['sentence'])

warnings.filterwarnings("ignore", category=UserWarning, module="spacy")
nlp_large = spacy.load("pt_core_news_lg")
# nlp = spacy.load("pt_core_news_md")

# French
# nlp_large = spacy.load("fr_dep_news_trf")



############ below tested
df1 = nlp.nlp_word_freq_all(path_S06E01, nlp_large)
df2 = nlp.nlp_word_freq_all(path_S06E02, nlp_large)

df_test01 = nlp_word_freq_all(path01, nlp_large)

test1 = nlp.concat_vocab_df(df1,df2)
# test2 = concat_vocab_df(df2, df1)



    

# common_words = pd_common_elements(df1['word'],df2['word'])




