# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 11:45:19 2018

@author: user
"""

from bs4 import BeautifulSoup
import urllib.request as req

url ="http://www.aozora.gr.jp/index_pages/person148.html#sakuhin_list_2"

res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

li_list = soup.select("ol > li")
for li in li_list:
    a = li.a
    if a != None:
        name = a.string
        href = a.attrs["href"]
        print(name, ">", href)