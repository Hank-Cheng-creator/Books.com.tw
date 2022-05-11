#!/usr/bin/env python
# coding: utf-8

# In[2]:


articles


# In[3]:


price


# In[4]:


len(articles)


# In[1]:


import requests
from bs4 import BeautifulSoup

for page in range(1, 4):
    url = 'https://www.books.com.tw/web/sys_bbotm/books/020806/?o=1&v=1&page=x'
    url = url.replace('x', str(page))
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    articles = soup.select('.msg h4 a')
    price = soup.select('.price_box li')
    for items in range(len(articles)):
        print(articles[items].text, price[items].text)

