# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 08:49:31 2024

Next:
    1) seperate assistent vs user
    1.1) replace \n with the actual space
    2) Find whether it's GPT3 or 4
    3) Bring the channel to the first row
    4) set index to start at 1

Mon Apr  8: 3.5 hrs

Now it can export as Excel file
I tried to search online doesn't seem anyone wrote this online

@author: Heng2020


"""

# read json into pd.df

#%%

import pandas as pd
import json
from collections import OrderedDict
from typing import Union, Literal
#%%
json_path = r'C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 02\NLP 10_ChatGPT_History\My_ChatGPT_conversations.json'
df = pd.read_json(json_path)

# pd.json_normalize()
# df02 = pd.json_normalize(json_path)
# %%
df_dtypes = df.dtypes

# Open the JSON file
with open(json_path) as f:
    data_json = json.load(f)

# Now 'data' contains the contents of the JSON file

print("eyp")


def read_chatGPT_channel(channel):
    exclude_role = ['system']
    error_row = []
    df_info = pd.DataFrame()


    message_list = []
    for key,value in channel.items():
        message_list.append(value['message'])

    content_type_list = set()
    i = 0

    for key,value in channel.items():
        dict_info = {}
        curr_message = value['message']
        if curr_message is None:
            continue
        curr_message['id'] = value['id']
        curr_message['parent_id'] = value['parent']
        test_n_children = len(value['children'])

        if test_n_children == 0:
            # first chat in channel
            curr_message['children_id'] = None
        else:
            curr_message['children_id'] = value['children'][0]

        if test_n_children > 1:
            # ignore this case for now
            # print(f"index '{i}' has more than 1 child")
            pass

        if curr_message is not None:
            dict_info['role'] = curr_message['author']['role']
            
            role = curr_message['author']['role']
            content_type = curr_message['content']['content_type']
            
            if content_type not in ['text','code']:
                content_type_list.add((i,content_type))

            if role in ['assistant','user']:
                if content_type in ['text']:
                    
                    dict_info['message'] = curr_message['content']['parts']
                    test_len = len(curr_message['content']['parts'])
                    if test_len > 1:
                        print(f"index {i} has more than 1 element in message list")
                    
                    if 'model_slug' in curr_message['metadata'].keys():
                        dict_info['model'] = curr_message['metadata']['model_slug']
                    else:
                        dict_info['model'] = None
                            
                elif content_type in ['code']:
                    dict_info['message'] = curr_message['content']['text']
                    dict_info['language'] = curr_message['content']['language']

            elif role in ['tool']:  
                dict_info['tool_name'] = curr_message['author']['name']
            elif role not in exclude_role:
                print(f"new row {role} at index = {i}")
                error_row.append(curr_message)
            del role
            del content_type

        curr_df_info = pd.DataFrame([dict_info])
        df_info = pd.concat([df_info,curr_df_info])
        i += 1
    df_info = df_info.reset_index(drop = True)
    # print(content_type_list)
    return df_info

def read_chatGPT_history(
        json_path_or_df: Union[str,pd.DataFrame]
                         ) -> pd.DataFrame:
    import pandas as pd

    if isinstance(json_path_or_df,str):
        df = pd.read_json(json_path_or_df)
    elif isinstance(json_path_or_df,pd.DataFrame):
        df = json_path_or_df

    channel_list = [pd.Series(row) for index, row in df.iterrows()]

    df_history = pd.DataFrame()

    for i in range(len(channel_list)):
        # df_channel = pd.DataFrame()
        # I just have the channel at the end for now
        channel = channel_list[i]['title']
        df_channel = read_chatGPT_channel(channel_list[i]['mapping'])
        df_channel['channel'] = channel

        df_history = pd.concat([df_history,df_channel],axis=0)

    return df_history


def test_read_chatGPT_channel():
    json_path = r'C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 02\NLP 10_ChatGPT_History\My_ChatGPT_conversations.json'
    df = pd.read_json(json_path)
    channel_0 = df.iloc[0]
    channel_list = [pd.Series(row) for index, row in df.iterrows()]
    channel_0 = channel_list[0]

    channel_0_map = OrderedDict(channel_0['mapping'])

    channel_15 = channel_list[15]
    channel_15_map = OrderedDict(channel_15['mapping'])

    message_list = []

    for key,value in channel_15_map.items():
        message_list.append(value['message'])
    # channel is the single chat thread

    current_channel = channel_list[15]['mapping']
    df_1_channel = read_chatGPT_channel(current_channel)


    curr_message = message_list[4]

def test_read_chatGPT_history():
    json_path = r'C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 02\NLP 10_ChatGPT_History\My_ChatGPT_conversations.json'
    df = pd.read_json(json_path)

    ans01 = read_chatGPT_history(json_path)
    ans02 = read_chatGPT_history(json_path)
    ans02.to_excel('ChatGPT_History.xlsx')
# try to convert info into dictionary


test_read_chatGPT_channel()
test_read_chatGPT_history()
