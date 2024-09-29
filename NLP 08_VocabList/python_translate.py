# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 09:34:01 2024

@author: Heng2020
"""
# https://openai.com/api/pricing/
import pandas as pd
# based on deep_translator, 1.11.4
from deep_translator import GoogleTranslator
from typing import Literal
from deep_translator import (GoogleTranslator,
                             ChatGptTranslator,
                             MicrosoftTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             PapagoTranslator,
                             DeeplTranslator,
                             QcriTranslator,
                             single_detection,
                             batch_detection)

# Function to translate text
def translate_text(text):
    try:
        translated = translator.translate(text, src='fr', dest='en')
        return translated
    except Exception as e:
        print(f"Error translating '{text}': {e}")
        return text

# Function to translate text
def translate_text(
        series
        ,lang_from = "auto"
        ,lang_to = "en"
        ,engine:Literal["Google","ChatGPT","Microsoft","Pons","Linguee","MyMemory","Yandex"] = "Google"
        ):
    from tqdm import tqdm
    from pandarallel import pandarallel
    pandarallel.initialize()
    tqdm.pandas() 
    
    out_series = series.parallel_apply(
        lambda text: translate_string(
            text,
            lang_from=lang_from,
            lang_to=lang_to,
            engine=engine
        ))
    return out_series

def translate_string(
        text:str
        ,lang_from = "auto"
        ,lang_to = "en"
        ,engine:Literal["Google","ChatGPT","Microsoft","Pons","Linguee","MyMemory","Yandex"] = "Google"
        ):
    from deep_translator import (GoogleTranslator,
                                 ChatGptTranslator,
                                 MicrosoftTranslator,
                                 PonsTranslator,
                                 LingueeTranslator,
                                 MyMemoryTranslator,
                                 YandexTranslator,
                                 PapagoTranslator,
                                 DeeplTranslator,
                                 QcriTranslator,
                                 single_detection,
                                 batch_detection)
    
    
    if engine in ["Google"]:
        translator = GoogleTranslator(src = lang_from, dest = lang_to)
    elif engine in ["Microsoft"]:
        translator = MicrosoftTranslator(src = lang_from, dest = lang_to)
    
    try:
        translated_text = translator.translate(text)
        return translated_text
    except Exception as e:
        print(f"Error translating '{text}': {e}")
        return text

df1['eng'] = translate_text(df1['word'])

# Apply the translation to the DataFrame column
df['English_Text'] = translate_text(df['French_Text'])

print(df)

text = 'Bonjour tout le monde'

translated = translator.translate(text, src='auto', dest='en')


# Sample text
text = 'Bonjour tout le monde'

# Initialize the translator
translator = GoogleTranslator(source='fr', target='en')

# Translate the text
translated_text = translator.translate(text)

print(translated_text)

