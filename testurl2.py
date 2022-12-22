# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 17:27:07 2022

@author: IT
"""
import pandas as pd

df = pd.DataFrame(['http://google.com', 'http://duckduckgo.com'])

def make_clickable(val):
    return '<a href="{}">{}</a>'.format(val,val)

df.style.format(make_clickable)
print(df)