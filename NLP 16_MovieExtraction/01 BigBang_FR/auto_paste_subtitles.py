# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 10:12:17 2025

@author: Norat
"""

import excel_toolkit as xt
import excel_toolkit.workbook as wbx
import excel_toolkit.worksheet as wsx
import xlwings as xw
import py_string_tool as pst
import video_toolkit as vt
import datetime as dt
from tqdm import trange
from pathlib import Path

# took about 1.5 hr for the main process

bigbang_excel_path = r'C:\Users\Norat\OneDrive\D_Documents\_Learn Languages\Portuguese\_LearnLanguages 04 BigBang PT_2025\BigBang Season 6_PT_QC.xlsm'

template_sheet_name:str = "S06E01"

sub_01_Template_path = r'C:\C_Video_Python\The Big Bang Theory\The Big Bang Theory Season 06\Season 06 Subtitle\Portuguese Amazon\The Big Bang Theory_{}_4_por.srt'
sub_02_Template_path = r'C:\C_Video_Python\The Big Bang Theory\The Big Bang Theory Season 06\Season 06 Subtitle\English Amazon\The Big Bang Theory_{}_15_eng.srt'

# medium tested
def paste_sub_1season_to_excel(
        excel_path:str|Path
        ,template_sheet_name:str
        , sub_01_Template_path:str
        ,sub_02_Template_path:str
        ,start_ep_num:int 
        ,end_ep_num:int) -> None:

    sub_01_Template = pst.TString(sub_01_Template_path)
    sub_02_Template = pst.TString(sub_02_Template_path)
    
    book_obj = wbx.return_as_wb(excel_path)
    
    for i in trange(start_ep_num, end_ep_num+1, colour="#FFC000"):
        episode_str = str(i).zfill(2)
        curr_episode_name = f"S06E{episode_str}"
        if curr_episode_name in wsx.sheet_names(book_obj):
            print(f"\n{curr_episode_name} already in the sheet name. Skip for this sheet.")
        else:
            wsx.copy_sheet(book_obj, from_sheet_name = template_sheet_name, to_sheet_names = curr_episode_name)
            sub_01_path = sub_01_Template.fill_values(curr_episode_name)
            sub_02_path = sub_02_Template.fill_values(curr_episode_name)
            
            sub_01_df = vt.sub_to_df(sub_01_path)
            sub_02_df = vt.sub_to_df(sub_02_path)
            curr_ws = book_obj.sheets[curr_episode_name]
            
            # convert datetime columns to the right format for Excel pasting
            for c in sub_01_df.columns:
                sub_01_df[c] = sub_01_df[c].map(
                    lambda x: dt.datetime.combine(dt.date(1899, 12, 30), x)
                    if isinstance(x, dt.time) else x
                )
    
            for c in sub_02_df.columns:
                sub_02_df[c] = sub_02_df[c].map(
                    lambda x: dt.datetime.combine(dt.date(1899, 12, 30), x)
                    if isinstance(x, dt.time) else x
                )
                
                
            curr_ws.range("C2:H5000").clear_contents()
            
            curr_ws.range("AC1:AN5000").clear_contents()
            curr_ws.range("AC1").options(index=True).value = sub_01_df
            curr_ws.range("AK1").options(index=True).value = sub_02_df
            
            
            # paste sub on the right side
            curr_ws.range("C2:C3001").value = curr_ws.range("AD2:AD3000").options(ndim=2).value
            curr_ws.range("E2:E3000").value = curr_ws.range("AE2:AE3000").options(ndim=2).value
            curr_ws.range("F2:F3000").value = curr_ws.range("AF2:AF3000").options(ndim=2).value
    print('\nDone successfully!!! ✅')
    
paste_sub_1season_to_excel(
    excel_path = bigbang_excel_path
    ,template_sheet_name = template_sheet_name
    ,sub_01_Template_path = sub_01_Template_path
    ,sub_02_Template_path = sub_02_Template_path
    ,start_ep_num  =1
    ,end_ep_num = 24
    )
