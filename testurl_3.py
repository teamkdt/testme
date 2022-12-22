# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 15:41:16 2022

@author: IT
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 09:49:09 2022

@author: IT
"""

from flask import *
import pandas as pd
from IPython.core.display import display, HTML
import numpy as np
app = Flask(__name__)

#@app.route("/tables")
#def show_tables():
    
    
 #   df = pd.read_excel('dummy_data.xlsx')
  #  for i in range(len(df['url'])):
   #     val = df['url'][i]
    #    print(val)
     #   def make_clickable(val):
      #      return '<a href="{}">{}</a>'.format(val,val)

        #df.style.format({'url':make_clickable})
    
    #===========================================================
    #for i in range(len(df['url'])):
     #   df['url'][i] = '<a href="' + df['url'][i] + '" target="_blank">' + df['url'][i] + '</a>'
     #print(df['url'][i])
    #df.to_excel('test1.xlsx')
    
   # data = pd.read_excel('test1.xlsx')
    
    #data.set_index(['Name'], inplace=True)
    #data.index.name=None
    #females = data.loc[data.Gender=='f']
    #males = data.loc[data.Gender=='m']
    #tbl = data.iloc[:]
    
    #return render_template('view.html',tables=[tbl.to_html(classes='tbl')],
    #titles = ['na', 'Female surfers', 'Male surfers','All data'])
   
        
    #HTML(df.to_html(render_links=True, escape=False))
  
@app.route('/test2')
def test_app2():
    url = 'https://www.sport24.gr'
    return render_template('test4.html',name = 'url')
    
@app.route('/')
def test_app():

    # create a table with a url column
    df = pd.DataFrame({"url": ["http://www.google.com", "http://duckduckgo.com"]})
    #df2 = pd.DataFrame()
    # create the column clickable_url based on the url column
    #df["clickable_url"] = df.apply(lambda row: "<a href='{}' target='_blank'>{}</a>".format(row.url, row.url.split("/")[2]), axis=1)
    HTML(df.to_html(render_links=True, escape=False))
    url = 'https://www.sport24.gr'
    # display the table as HTML. Note, only the clickable_url is being selected here
    #display(HTML(df[["clickable_url"]].to_html(escape=False)))
    return render_template('simple.html',  tables=[df.to_html(classes='data',render_links=True)], titles=df.columns.values,name = 'url')

if __name__ == "__main__":
    app.run(host="192.168.1.74", port=8081,debug=True)