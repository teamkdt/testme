# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 09:49:09 2022

@author: IT
"""

from flask import *
import pandas as pd
app = Flask(__name__)

def gen_dict(df, title):
    return {'title': title,
            'table': df.head().to_html(classes='tbl',render_links=True,index=False)
            }

@app.route("/tables")
def show_tables():
    
    
    df = pd.read_excel('dummy_data.xlsx')
    for i in range(len(df['url'])):
        val = df['url'][i]
        print(val)
        def make_clickable(val):
            return '<a href="{}">{}</a>'.format(val,val)

        df.style.format({'url':make_clickable})
    
    #===========================================================
    #for i in range(len(df['url'])):
     #   df['url'][i] = '<a href="' + df['url'][i] + '" target="_blank">' + df['url'][i] + '</a>'
     #print(df['url'][i])
    df.to_excel('test1.xlsx')
    
    data = pd.read_excel('test1.xlsx')
    data2 = pd.read_excel('test_sp_powergame_final3.xlsx')
    data3 = data2[['title', 'link','date']]
    data4 = pd.read_excel('mikrometoxos_final.xlsx')
    data5 = data4[['title', 'url','date']]
    data6 = pd.read_excel('test_sp_hellasjournal.xlsx')
    data7 = data6[['title', 'url','date']]
    data8 = pd.read_excel('test_sp_hellasjournal.xlsx')
    data9 = data8[['title', 'url','date']]
    data.set_index(['Name'], inplace=True)
    data.index.name=None
    females = data.loc[data.Gender=='f']
    males = data.loc[data.Gender=='m']
    tbl = data.iloc[:]
    
    k = [females.to_html(classes='female',render_links=True), tbl.to_html(classes='tbl'),males.to_html(classes='male',render_links=True),tbl.to_html(classes='tbl')]
    d= {'df1': gen_dict(data5, 'First Dataframe'),'df2' : gen_dict(data7, 'Second Dataframe'),'df3' : gen_dict(data3, 'Third Datarame'),'df4' : gen_dict(data9, 'Fourth Datarame')}
    return render_template('view.html',**d,
    titles = ['na', 'Female surfers', 'All data1','Male Surfers1','All data2'])
   
        
    #HTML(df.to_html(render_links=True, escape=False))
    

if __name__ == "__main__":
    app.run(host="192.168.132.135", port=8081,debug=True)