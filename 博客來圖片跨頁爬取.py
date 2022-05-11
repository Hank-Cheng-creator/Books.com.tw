#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup
import shutil

for page in range(1, 3):
    url = 'https://www.books.com.tw/web/sys_bbotm/books/020806/?o=1&v=1&page=x'
    url = url.replace('x', str(page))
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

for pictures in soup.select('.cover'):
    fname = pictures['src'].split('/')[-1].split('&')[0] #取得圖檔名稱
    res2 = requests.get(pictures['src'].split('i=')[1].split('&')[0], stream=True)
    pics = open(fname, 'wb') #將取得的圖檔名稱寫入電腦資料夾
    shutil.copyfileobj(res2.raw, pics)
    pics.close()

