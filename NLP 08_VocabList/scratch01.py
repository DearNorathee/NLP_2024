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


structure = {
    "Portuguese": {
        "Westworld Portuguese": {
            "Westworld Portugues 01": None,
            "Westworld Portugues 02": ["folder1","folder2"],
            "Westworld Portugues 03": None,
            "Westworld Portugues 04": None,
        },
        "BigBang Portuguese": [
            "BigBang PT Season 01"
            "BigBang PT Season 02"
            "BigBang PT Season 03"
            "BigBang PT Season 04"
            "BigBang PT Season 05"
            "BigBang PT Season 06"
            "BigBang PT Season 07"
            "BigBang PT Season 08"
            "BigBang PT Season 09"
            "BigBang PT Season 10"
            "BigBang PT Season 11"
        ],
        "The 100 PT": {
            "The 100 Season 01 Portuguese": None,
            "The 100 Season 02 Portuguese": None,
            "The 100 Season 03 Portuguese": None,
            "The 100 Season 04 Portuguese": None,
            "The 100 Season 05 Portuguese": None,
        },
    }
}

