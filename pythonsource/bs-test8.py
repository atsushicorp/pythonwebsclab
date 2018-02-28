# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 13:57:46 2018

@author: user
"""

from bs4 import BeautifulSoup

fp = open("fruits-vegetables.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")
fp.close()

sel = lambda q: print(soup.select_one(q).string)
sel("#fr-list > .red.green")
    
fr_list = soup.select("#fr-list > .yellow")
for fr_name in fr_list:
    print("黄色カテゴリのフルーツは", fr_name)
    
"""
testwrite
"""