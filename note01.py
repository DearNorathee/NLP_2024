# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 11:00:24 2023

@author: Heng2020
"""

#########
# convert dataframe into 1d list
verb_list = test01_02.values.flatten().tolist()
# go the other direction
list_1d = df.values.flatten('F').tolist()
import pandas as pd
# wide to long using: .melt() , .wide_to_long()
# long to wide using: .pivot(), .pivot_table()
################ select some keys in the dictionary
subject = ['eu', 'ele', 'nos', 'eles']
dict01 = {'eu': 123, 'tu': 456, 'ele': 789, 'nós': 101112, 'vocês': 131415, 'eles': 161718}

def filter_dict(myDict,select_key):
    # should be in my lib
    ans = {key: value for key, value in myDict.items() if key in select_key}
    return ans

def change_key(myDict,rename_map):
    ans = {rename_map[key]: value for key, value in myDict.items()}
    return ans



filtered_dict = filter_dict(dict01,subject)



# create dataFrame whose columns are keys from dictionary
df = pd.DataFrame([dict01], columns=dict01.keys())
print(filtered_dict)

dict01 = {'eu': 123, 'tu': 456, 'ele': 789, 'nós': 101112, 'vocês': 131415, 'eles': 161718}

# Define a mapping of new key names
key_mapping = {'eu': 'I', 'tu': 'You', 'ele': 'He', 'nós': 'We', 'vocês': 'You all', 'eles': 'They'}

# Create a new dictionary with the updated key names
new_dict = change_key(dict01, key_mapping)
