# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 09:45:22 2023

@author: Heng2020
"""
import pandas as pd
df = pd.DataFrame({
    'text': ['Hello', 'world', 'this', 'is', 'a', 'test'],
    'other_column': [1, 2, 3, 4, 5, 6]
})

# Convert the 'text' column to a single string with space as separator
single_text = ' '.join(df['text'].astype(str))
