# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 12:10:41 2022

@author: IT
"""

import pandas as pd


df = pd.read_excel('dummy_data.xlsx')
for i in range(len(df['Origin'])):
    val = df['Origin'][i]
    print(val)
    def make_clickable(val):
        return f'<a target="_blank" href="{val}">{val}</a>'

    df.style.format({'url':make_clickable})
    
df.to_excel('test1.xlsx')

print(df)