# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:14:39 2019

@author: pc
"""
import requests
import os
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

#資料來源
url = 'https://movies.yahoo.com.tw/chart.html?guccounter=1&guce_referrer=aHR0cHM6Ly9tb3ZpZXMueWFob28uY29tLnR3Lw&guce_referrer_sig=AQAAAKC0YIM61mJwn8yQtQlFLbKWiPpXRom64qWRQlWNMJ-z31RUCIlExv-GdFvSvMafgvbRrn0MPLXjDG9yxmwPS5ZTlFa3WTKVqe6kUHAvhG9WYjEo8k14gW5_bsyQM3S2sZq6MihUDec2uPu3mYjlx0kPeLhxGR337dptRcS5KV51'

# find the movie rank page
def getdata(x):
    r = requests.get(x)
    r.encoding = 'utf-8'
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        return soup
    return 'miss'




#find the movie rank link
def fmlist():
    a = getdata(url)
    if a == 'miss':
        print(a)
        return a
    
    lista = a.find('div', class_ = 'rank_list table rankstyle1')
    lista = lista.find_all('div', class_ = 'tr')
    
    mlink = []
    for i in lista:
        if i.find('a') != None:
            mlink.append(i.find('a')['href'])
        
    return mlink



# create image
def cimg():
    a = fmlist()
    
    l1 = []
    
    for i in a:
        l1.append(getdata(i))
    
    for t,i in enumerate(l1):
        if i == 'miss':
            a[t] == i
        #print(i.find('h1').text)
            
    
    if not os.path.isdir('img'):
        os.mkdir('img')
    
    nl = []
    for t,i in enumerate(l1):
        if i == 'miss':
            continue
        
        
        name = i.find('h1').text
        nl.append(name)
        #print(name)
        igsrc = i.find('div', class_ = 'movie_intro_foto')
        img = igsrc.find('img')['src']
        #print(img)
        subname = img.split('.')[-1]
        #print(subname)
        urlretrieve(img, 'img/'+name+'.'+subname)
        #print(t,'ok')
        
    
    #print('done')
    
    for t,i in enumerate(a):
        a[t] = [i, nl[t]]
    
    #回傳排行、連結、名字給畫面取用
    return a





