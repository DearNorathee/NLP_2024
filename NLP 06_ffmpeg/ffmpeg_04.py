# -*- coding: utf-8 -*-
"""
Created on Sat May 11 10:07:29 2024

@author: Heng2020
"""
import video_toolkit as vt
from typing import List, Tuple, Literal, Union
from pathlib import Path

# Sub
def extract_audio_1file(
        video_path:     Union[str,Path],
        output_folder:  Union[str,Path],
        output_name:    Union[str,Path, None] = None, 
        file_extension: Union[str,list] = ".mp3",
        alarm_done_path: Union[str,bool] = False,
        overwrite_file: bool = True,
        one_output_per_lang: bool = True,
        languages: Union[List[str],None] = None,
        
                    ) -> None:
    # time spend 5 hr
    
    # medium tested
    
    #  tested Parameters:
        # all default parameters
        # when languages is str
    
    # untested Parameters
        # file_extension as list
        # overwrite_file = False
        # one_output_per_lang = False
        # languages as list
    # Not Done 
    # Next right now I got a name BigBang_FR_S06E01.mp3_EN which is wrong
    
    from langcodes import Language
    """
    Extract audio from a video file. If video has multiple audio in different languages,
    this function also support that

    Parameters
    ----------
    video_path : Union[str,Path]
        DESCRIPTION.
    output_folder : Union[str,Path]
        DESCRIPTION.
    output_name : Union[str,Path]
        DESCRIPTION.
    file_extension : Union[str,list], optional
        DESCRIPTION. The default is ".mp3".
    play_alarm : bool, optional
        DESCRIPTION. The default is True.
    overwrite_file : bool, optional
        DESCRIPTION. The default is True.
    
    one_output_per_lang : bool, optional
        If there are more than 1 audio files for each langauge, if True then it would one extract 1 file per
        language, if not it would extract all of them seperately.
        The default is True.
        False is still not in production because I have to create index suffix at the end
    Returns
    -------
    bool
        DESCRIPTION.

    """
    from tqdm import tqdm
    from langcodes import Language
    from pathlib import Path
    import subprocess
    from playsound import playsound
    import os
    
    codec_dict = {'.mp3': "libmp3lame",
                  'mp3' : "libmp3lame",
                  '.wav': "pcm_s24le",
                  'wav' : "pcm_s24le"
                  }
    
    codec = codec_dict[file_extension]
    
    output_folder_in = Path(output_folder)
    
    file_extension_in = [file_extension] if isinstance(file_extension, str) else list(file_extension)
    

    if output_name is None:
        output_name_in = Path(video_path).stem
    else:
        output_name_in = output_name
    
    filter_lang = [languages] if isinstance(languages,str) else languages
    
    if languages is None:
        filter_lang_3chr = None
    else:
        filter_lang_3chr = []
    
        for language in filter_lang:
            lang_obj =  vt.closest_language_obj(language)
            # variant = "B" would return fre for french
            filter_lang_3chr.append(lang_obj.to_alpha3(variant = "B"))
    
    alarm_done_path = r"H:\D_Music\Sound Effect positive-logo-opener.mp3"
    audio_index = vt.get_audio_index(video_path)
    metadata = vt.get_metadata(video_path,"audio",language=filter_lang_3chr)
    
    if one_output_per_lang:
        metadata_filter = metadata.drop_duplicates(subset=['language'], keep='first')
    else:
        metadata_filter = metadata.copy()
    
    audio_index = list(metadata_filter.index)
    video_lang_list = metadata_filter['language'].tolist()


    output_name_list = []
    output_path_list = []

    
    for i, language_3_str in tqdm(enumerate(video_lang_list),total=len(video_lang_list)):
        
        lang_obj =  Language.get(language_3_str)
        language_2_str = str(lang_obj).upper()
        lang_obj.to_alpha3()
        for j, curr_file_ext in enumerate(file_extension_in):
            
            if curr_file_ext not in output_name_in:
                if "." not in curr_file_ext:
                    file_extension_in[j] = "." + curr_file_ext
                else:
                    file_extension_in[j] = curr_file_ext
                curr_output_name = output_name_in + "_" + language_2_str + file_extension_in[j]
                output_name_list.append(curr_output_name)
                output_path = output_folder_in / curr_output_name
                output_path_list.append(output_path)
                
                command = [
                    "ffmpeg",
                    "-i", str(video_path),
                    "-map", f"0:{audio_index[i]}",
                    "-c:a", codec,
                    "-q:a", "0",
                    str(output_path)
                ]
                # keep command_line for debugging
                command_line = " ".join(command)
 
                if os.path.exists(str(output_path)):
                    if overwrite_file:
                        os.remove(str(output_path))
                    else:
                        print("\nThe output path is already existed. Please delete the file or set the overwrite parameter to TRUE")
                        return False
                result = subprocess.run(command, text=True, stderr=subprocess.PIPE)
                
                if result.returncode != 0:
                    print(f"\nError encountered: {curr_output_name}")
                    print(result.stderr)
                
                elif result.returncode == 0:
                    print(f"\nExtract audio successfully: {curr_output_name}!!!")
                    
                    if alarm_done_path:
                        playsound(alarm_done_path)

def test_extract_audio_1file():
    folder_FR_bigbang = Path(r"H:\D_Download\Video 01\[ Torrent911.io ] The.Big.Bang.Theory.2007-2019.Integrale.Multi.WEB-DL.1080p.AVC-Ducks\Saison 6")
    chosen_video_name = "The Big Bang Theory_S06E01.mkv"
    chosen_video_path = folder_FR_bigbang / chosen_video_name
    alarm_done_path = r"H:\D_Music\Sound Effect positive-logo-opener.mp3"
    
    output_folder01 = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 01\OutputData\extract_audio_1file\test_01_all"
    output_folder02 = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 01\OutputData\extract_audio_1file\test_02_only_French"
    output_name = "BigBang_FR_S06E01"
    
    
    
    matrix_video_path = r"G:/My Drive/G_Videos/Polyglot/The Matrix Resurrections 2021.mkv"
    extract_audio_1file(video_path = chosen_video_path,
                        output_folder = output_folder01,
                        output_name = output_name,
                        alarm_done_path = alarm_done_path)
    
    extract_audio_1file(video_path = chosen_video_path,
                        output_folder = output_folder02,
                        alarm_done_path = alarm_done_path,
                        languages="french"
                        )
    

def main():
    test_extract_audio_1file()

if __name__ == "__main__":
    main()
    