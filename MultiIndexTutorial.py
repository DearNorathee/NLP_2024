# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 11:48:19 2023

@author: Heng2020
"""
import pandas as pd
stocks = pd.read_csv('http://bit.ly/smallstocks')


ser = stocks.groupby(['Symbol','Date']).Close.mean()
ser.unstack()
