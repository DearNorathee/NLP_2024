# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 14:56:57 2023

@author: Heng2020
"""
######## This file is for testing elevenlabs API
from elevenlabs import clone, generate, play, set_api_key, Voice, VoiceDesign, Gender, Age, Accent,voices,save
from elevenlabs.api import History, User
import os



# from elevenlabs import *

import tkinter as tk
import tkinter.messagebox as mb
from playsound import playsound
# root = tk.TK()

# root.mainloop()
# root.quit()
# mb.showinfo("Run sucessfully!!",message="Audio is generated sucessfully")

######## Right now I can generate audio with 1 text
######## Next is to expand to df


alarm_path = r"H:/D_Music/Sound Effect positive-logo-opener.mp3"
model = "eleven_multilingual_v2"
person = "Adam"
API_KEY = "f8637df411c9b08173ab69abc6ad789e"

output_folder = r"C:\Users\Heng2020\OneDrive\D_Documents\_LearnLanguages 04 BigBang PT\_BigBang PU\S06 Done\11Labs_test"
out_1file_name = "test01.mp3"


out_path01 = os.path.join(output_folder,out_1file_name)
out_path02 = output_folder + "\\" + out_1file_name

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
    
def tokens_used(API_KEY = "f8637df411c9b08173ab69abc6ad789e"):
    set_api_key(API_KEY)
    user = User.from_api()
    used_count = user.subscription.character_count
    
    return used_count


def tokens_left(API_KEY = "f8637df411c9b08173ab69abc6ad789e"):
    set_api_key(API_KEY)
    user = User.from_api()
    total_tokens = user.subscription.character_limit
    used_count = user.subscription.character_count
    
    left_tokens = total_tokens - used_count
    
    return left_tokens
    
    
    

set_api_key(API_KEY)

user = User.from_api()
user2 = user.subscription.character_count
print(user)


text1 = "Eu ouço você sem o telefone."

name_list = ['test01','test02','test03','test04','test05']
text_list = ["Por que acha que ele sabe o que é e eu não?", "Na verdade, eu vou ficar com a Penny. ", "Como já declarei antes, em numerosas ocasiões...", "a única criatura do mar pela qual eu consideraria ser comido é o Kraken. ", "Além do mais, eu vou jantar com a Amy."]

num = tokens_left()
create_audio(text_list,name_list,output_folder)

# my_info = get_user_info(API_KEY)
# voices = voices()
# voice_list = list(voices)
# print(voices)

# voice_out = [Voice(voice_id='21m00Tcm4TlvDq8ikWAM', name='Rachel', category='premade', description=None, labels={'accent': 'american', 'description': 'calm', 'age': 'young', 'gender': 'female', 'use case': 'narration'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/21m00Tcm4TlvDq8ikWAM/df6788f9-5c96-470d-8312-aab3b3d8f50a.mp3', settings=None), Voice(voice_id='2EiwWnXFnvU5JabPnv8n', name='Clyde', category='premade', description=None, labels={'accent': 'american', 'description': 'war veteran', 'age': 'middle aged', 'gender': 'male', 'use case': 'video games'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/2EiwWnXFnvU5JabPnv8n/65d80f52-703f-4cae-a91d-75d4e200ed02.mp3', settings=None), Voice(voice_id='AZnzlk1XvdvUeBnXmlld', name='Domi', category='premade', description=None, labels={'accent': 'american', 'description': 'strong', 'age': 'young', 'gender': 'female', 'use case': 'narration'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/AZnzlk1XvdvUeBnXmlld/508e12d0-a7f7-4d86-a0d3-f3884ff353ed.mp3', settings=None), Voice(voice_id='CYw3kZ02Hs0563khs1Fj', name='Dave', category='premade', description=None, labels={'accent': 'british-essex', 'description': 'conversational', 'age': 'young', 'gender': 'male', 'use case': 'video games'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/CYw3kZ02Hs0563khs1Fj/872cb056-45d3-419e-b5c6-de2b387a93a0.mp3', settings=None), Voice(voice_id='D38z5RcWu1voky8WS1ja', name='Fin', category='premade', description=None, labels={'accent': 'irish', 'description': 'sailor', 'age': 'old', 'gender': 'male', 'use case': 'video games'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/D38z5RcWu1voky8WS1ja/a470ba64-1e72-46d9-ba9d-030c4155e2d2.mp3', settings=None), Voice(voice_id='EXAVITQu4vr4xnSDxMaL', name='Bella', category='premade', description=None, labels={'accent': 'american', 'description': 'soft', 'age': 'young', 'gender': 'female', 'use case': 'narration'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/EXAVITQu4vr4xnSDxMaL/941b779e-c2ad-48d4-bddb-28d1a68fa27e.mp3', settings=None), Voice(voice_id='ErXwobaYiN019PkySvjV', name='Antoni', category='premade', description=None, labels={'accent': 'american', 'description': 'well-rounded', 'age': 'young', 'gender': 'male', 'use case': 'narration'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/ErXwobaYiN019PkySvjV/ee9ac367-91ee-4a56-818a-2bd1a9dbe83a.mp3', settings=None), Voice(voice_id='GBv7mTt0atIp3Br8iCZE', name='Thomas', category='premade', description=None, labels={'accent': 'american', 'description': 'calm', 'age': 'young', 'gender': 'male', 'use case': 'meditation'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/GBv7mTt0atIp3Br8iCZE/98542988-5267-4148-9a9e-baa8c4f14644.mp3', settings=None), Voice(voice_id='IKne3meq5aSn9XLyUdCD', name='Charlie', category='premade', description=None, labels={'accent': 'australian', 'description': 'casual', 'age': 'middle aged', 'gender': 'male', 'use case': 'conversational'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/IKne3meq5aSn9XLyUdCD/102de6f2-22ed-43e0-a1f1-111fa75c5481.mp3', settings=None), Voice(voice_id='LcfcDJNUP1GQjkzn1xUU', name='Emily', category='premade', description=None, labels={'accent': 'american', 'description': 'calm', 'age': 'young', 'gender': 'female', 'use case': 'meditation'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/LcfcDJNUP1GQjkzn1xUU/e4b994b7-9713-4238-84f3-add8fccaaccd.mp3', settings=None), Voice(voice_id='MF3mGyEYCl7XYWbV9V6O', name='Elli', category='premade', description=None, labels={'accent': 'american', 'description': 'emotional', 'age': 'young', 'gender': 'female', 'use case': 'narration'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/MF3mGyEYCl7XYWbV9V6O/d8ecadea-9e48-4e5d-868a-2ec3d7397861.mp3', settings=None), Voice(voice_id='N2lVS1w4EtoT3dr4eOWO', name='Callum', category='premade', description=None, labels={'accent': 'american', 'description': 'hoarse', 'age': 'middle aged', 'gender': 'male', 'use case': 'video games'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/N2lVS1w4EtoT3dr4eOWO/ac833bd8-ffda-4938-9ebc-b0f99ca25481.mp3', settings=None), Voice(voice_id='ODq5zmih8GrVes37Dizd', name='Patrick', category='premade', description=None, labels={'accent': 'american', 'description': 'shouty', 'age': 'middle aged', 'gender': 'male', 'use case': 'video games'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/ODq5zmih8GrVes37Dizd/0ebec87a-2569-4976-9ea5-0170854411a9.mp3', settings=None), Voice(voice_id='SOYHLrjzK2X1ezoPC6cr', name='Harry', category='premade', description=None, labels={'accent': 'american', 'description': 'anxious', 'age': 'young', 'gender': 'male', 'use case': 'video games'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/SOYHLrjzK2X1ezoPC6cr/86d178f6-f4b6-4e0e-85be-3de19f490794.mp3', settings=None), Voice(voice_id='TX3LPaxmHKxFdv7VOQHJ', name='Liam', category='premade', description=None, labels={'accent': 'american', 'age': 'young', 'gender': 'male', 'use case': 'narration', 'description ': 'neutral'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/TX3LPaxmHKxFdv7VOQHJ/63148076-6363-42db-aea8-31424308b92c.mp3', settings=None), Voice(voice_id='ThT5KcBeYPX3keUQqHPh', name='Dorothy', category='premade', description=None, labels={'accent': 'british', 'description': 'pleasant', 'age': 'young', 'gender': 'female', 'use case': "children's stories"}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/ThT5KcBeYPX3keUQqHPh/981f0855-6598-48d2-9f8f-b6d92fbbe3fc.mp3', settings=None), Voice(voice_id='TxGEqnHWrfWFTfGW9XjX', name='Josh', category='premade', description=None, labels={'accent': 'american', 'description': 'deep', 'age': 'young', 'gender': 'male', 'use case': 'narration'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/TxGEqnHWrfWFTfGW9XjX/3ae2fc71-d5f9-4769-bb71-2a43633cd186.mp3', settings=None), Voice(voice_id='VR6AewLTigWG4xSOukaG', name='Arnold', category='premade', description=None, labels={'accent': 'american', 'description': 'crisp', 'age': 'middle aged', 'gender': 'male', 'use case': 'narration'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/VR6AewLTigWG4xSOukaG/316050b7-c4e0-48de-acf9-a882bb7fc43b.mp3', settings=None), Voice(voice_id='XB0fDUnXU5powFXDhCwa', name='Charlotte', category='premade', description=None, labels={'accent': 'english-swedish', 'description': 'seductive', 'age': 'middle aged', 'gender': 'female', 'use case': 'video games'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/XB0fDUnXU5powFXDhCwa/942356dc-f10d-4d89-bda5-4f8505ee038b.mp3', settings=None), Voice(voice_id='XrExE9yKIg1WjnnlVkGX', name='Matilda', category='premade', description=None, labels={'accent': 'american', 'description': 'warm', 'age': 'young', 'gender': 'female', 'use case': 'audiobook'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/XrExE9yKIg1WjnnlVkGX/b930e18d-6b4d-466e-bab2-0ae97c6d8535.mp3', settings=None), Voice(voice_id='Yko7PKHZNXotIFUBG7I9', name='Matthew', category='premade', description=None, labels={'accent': 'british', 'age': 'middle aged', 'gender': 'male', 'use case': 'audiobook', 'description ': 'calm'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/Yko7PKHZNXotIFUBG7I9/02c66c93-a237-436f-8a7d-43e8c49bc6a3.mp3', settings=None), Voice(voice_id='ZQe5CZNOzWyzPSCn5a3c', name='James', category='premade', description=None, labels={'accent': 'australian', 'description': 'calm ', 'age': 'old', 'gender': 'male', 'use case': 'news'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/ZQe5CZNOzWyzPSCn5a3c/35734112-7b72-48df-bc2f-64d5ab2f791b.mp3', settings=None), Voice(voice_id='Zlb1dXrM653N07WRdFW3', name='Joseph', category='premade', description=None, labels={'accent': 'british', 'age': 'middle aged', 'gender': 'male', 'use case': 'news', 'description ': 'ground reporter '}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/Zlb1dXrM653N07WRdFW3/daa22039-8b09-4c65-b59f-c79c48646a72.mp3', settings=None), Voice(voice_id='bVMeCyTHy58xNoL34h3p', name='Jeremy', category='premade', description=None, labels={'accent': 'american-irish', 'description': 'excited', 'age': 'young', 'gender': 'male', 'use case': 'narration'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/bVMeCyTHy58xNoL34h3p/66c47d58-26fd-4b30-8a06-07952116a72c.mp3', settings=None), Voice(voice_id='flq6f7yk4E4fJM5XTYuZ', name='Michael', category='premade', description=None, labels={'accent': 'american', 'age': 'old', 'gender': 'male', 'use case': 'audiobook', 'description ': 'orotund'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/flq6f7yk4E4fJM5XTYuZ/c6431a82-f7d2-4905-b8a4-a631960633d6.mp3', settings=None), Voice(voice_id='g5CIjZEefAph4nQFvHAz', name='Ethan', category='premade', description=None, labels={'accent': 'american', 'age': 'young', 'gender': 'male', 'use case': 'ASMR', 'description ': 'whisper'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/g5CIjZEefAph4nQFvHAz/26acfa99-fdec-43b8-b2ee-e49e75a3ac16.mp3', settings=None), Voice(voice_id='jBpfuIE2acCO8z3wKNLl', name='Gigi', category='premade', description=None, labels={'accent': 'american', 'description': 'childlish', 'age': 'young', 'gender': 'female', 'use case': 'animation'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/jBpfuIE2acCO8z3wKNLl/3a7e4339-78fa-404e-8d10-c3ef5587935b.mp3', settings=None), Voice(voice_id='jsCqWAovK2LkecY7zXl4', name='Freya', category='premade', description=None, labels={'accent': 'american', 'age': 'young', 'gender': 'female', 'description ': 'overhyped', 'usecase': 'video games'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/jsCqWAovK2LkecY7zXl4/8e1f5240-556e-4fd5-892c-25df9ea3b593.mp3', settings=None), Voice(voice_id='oWAxZDx7w5VEj9dCyTzz', name='Grace', category='premade', description=None, labels={'accent': 'american-southern', 'age': 'young', 'gender': 'female', 'use case': 'audiobook ', 'description ': 'gentle'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/oWAxZDx7w5VEj9dCyTzz/84a36d1c-e182-41a8-8c55-dbdd15cd6e72.mp3', settings=None), Voice(voice_id='onwK4e9ZLuTAKqWW03F9', name='Daniel', category='premade', description=None, labels={'accent': 'british', 'description': 'deep', 'age': 'middle aged', 'gender': 'male', 'use case': 'news presenter'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/onwK4e9ZLuTAKqWW03F9/7eee0236-1a72-4b86-b303-5dcadc007ba9.mp3', settings=None), Voice(voice_id='pMsXgVXv3BLzUgSXRplE', name='Serena', category='premade', description=None, labels={'accent': 'american', 'description': 'pleasant', 'age': 'middle aged', 'gender': 'female', 'use case': 'interactive'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/pMsXgVXv3BLzUgSXRplE/d61f18ed-e5b0-4d0b-a33c-5c6e7e33b053.mp3', settings=None), Voice(voice_id='pNInz6obpgDQGcFmaJgB', name='Adam', category='premade', description=None, labels={'accent': 'american', 'description': 'deep', 'age': 'middle aged', 'gender': 'male', 'use case': 'narration'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/pNInz6obpgDQGcFmaJgB/38a69695-2ca9-4b9e-b9ec-f07ced494a58.mp3', settings=None), Voice(voice_id='piTKgcLEGmPE4e6mEKli', name='Nicole', category='premade', description=None, labels={'accent': 'american', 'description': 'whisper', 'age': 'young', 'gender': 'female', 'use case': 'audiobook'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/piTKgcLEGmPE4e6mEKli/c269a54a-e2bc-44d0-bb46-4ed2666d6340.mp3', settings=None), Voice(voice_id='t0jbNlBVZ17f02VDIeMI', name='Jessie', category='premade', description=None, labels={'accent': 'american', 'description': 'raspy ', 'age': 'old', 'gender': 'male', 'use case': 'video games'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/t0jbNlBVZ17f02VDIeMI/e26939e3-61a4-4872-a41d-33922cfbdcdc.mp3', settings=None), Voice(voice_id='wViXBPUzp2ZZixB1xQuM', name='Ryan', category='premade', description=None, labels={'age': 'middle aged', 'description': 'soldier', 'accent': 'american', 'gender': 'male', 'use case': 'audiobook'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/wViXBPUzp2ZZixB1xQuM/4a82f749-889c-4097-85f0-a3826a28b1d8.mp3', settings=None), Voice(voice_id='yoZ06aMxZJJ28mfd3POQ', name='Sam', category='premade', description=None, labels={'accent': 'american', 'description': 'raspy', 'age': 'young', 'gender': 'male', 'use case': 'narration'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/yoZ06aMxZJJ28mfd3POQ/ac9d1c91-92ce-4b20-8cc2-3187a7da49ec.mp3', settings=None), Voice(voice_id='z9fAnlkpzviPz146aGWa', name='Glinda', category='premade', description=None, labels={'accent': 'american', 'description': 'witch', 'age': 'middle aged', 'gender': 'female', 'use case': 'video games'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/z9fAnlkpzviPz146aGWa/cbc60443-7b61-4ebb-b8e1-5c03237ea01d.mp3', settings=None), Voice(voice_id='zcAOhNBS3c14rBihAFp1', name='Giovanni', category='premade', description=None, labels={'accent': 'english-italian', 'description': 'foreigner', 'age': 'young', 'gender': 'male', 'use case': 'audiobook'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/zcAOhNBS3c14rBihAFp1/e7410f8f-4913-4cb8-8907-784abee5aff8.mp3', settings=None), Voice(voice_id='zrHiDhphv9ZnVXBqCLjz', name='Mimi', category='premade', description=None, labels={'accent': 'english-swedish', 'description': 'childish', 'age': 'young', 'gender': 'female', 'use case': 'animation'}, samples=None, design=None, preview_url='https://storage.googleapis.com/eleven-public-prod/premade/voices/zrHiDhphv9ZnVXBqCLjz/decbf20b-0f57-4fac-985b-a4f0290ebfc4.mp3', settings=None)]

# # Adam
# voice = Voice(voice_id="pNInz6obpgDQGcFmaJgB")

# audio = generate(
#     text="Eu ouço você sem o telefone.", 
#     voice=person,
#     model=model
#     )

# play(audio)

# history = History.from_api()
# print(history)




    