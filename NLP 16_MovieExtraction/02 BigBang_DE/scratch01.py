# -*- coding: utf-8 -*-
"""
Created on Tue Jun  3 10:15:36 2025

@author: Norat
"""

from pathlib import Path
from typing import Type,Union

import py_string_tool as pst
import os_toolkit as ost    

ost.auto_rename_series(
    folder_path = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 01\Season 01 Audio\German"
    , prefix = "BigBang DE")

def test_get_num():
    input01 = ['S01', 'S02', 'S03', 'S04', 'S05', 'S06', 'S07', 'S08', 'S09', 'S10', 'S11', 'S12']
    actual01 = pst.get_num(input01)
    expect01 = [1,2,3,4,5,6,7,8,9,10,11,12]
    assert actual01 == expect01

test_get_num()