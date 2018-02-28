# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 12:26:34 2018

@author: user
"""

from bs4 import BeautifulSoup

fp = open("book.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")
fp.close()

#CSSセレクタで検索する方法
sel = lambda q: print(soup.select_one(q).string)
sel("#nu") #id属性をオーソドックスに取り出す
sel("li#nu") #liタグのid属性でセレクタ選択
sel("ul > li#nu") #一階層上のulタグからの指定
sel("#bible #nu") #id属性を1つ書いて、その下のidがnuを選択
sel("#bible > #nu") #タグが直接親子関係になっていることを明示
sel("ul#bible > li#nu")  #idがbibleであるulタグと、その直下にあるliタグのnu属性について明確な指示を示している。
sel("li[id='nu']") #属性検索を利用し、idがnuであるliタグを指定
sel("li:nth-of-type(4)") #4つ目のliタグの要素を取り出す指定

#その他の方法
print(soup.select("li")[3].string) #すべてのliタグを取得した上で、その「３」番目の要素を取得/指定
print(soup.find_all("li")[3].string)

