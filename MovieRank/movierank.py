# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:40:43 2019

@author: pc
"""

import os, webbrowser
import tkinter as tk
from PIL import Image, ImageTk
import moviedata as md

#取得爬蟲結果
rl = md.cimg()

#設定好按鈕要用圖檔
def setimg(x):
    name = x.split('.')[0]
    x = openimg(x)
    
    w = 1280//5
    
    iw, ih = x.size
    
    r = w/iw
    
    h = ih*r
    w = iw*r
    
    if not os.path.isdir('btimg'):
        os.mkdir('btimg')
    
    x = x.resize((int(w), int(h)), Image.ANTIALIAS)
    
    x.save('btimg/{}.png'.format(name)) 
    
def openimg(x):
    x = Image.open('img/'+x)
    return x


#確定圖檔的存在
if not os.path.isdir('img'):
    imglist = 'miss'
else:
    imglist = os.listdir('img')


#清理按鈕圖檔資料夾
if os.path.isdir('btimg'):
    cl = os.listdir('btimg')
    for i in cl:
        os.remove('btimg/'+i)


#把圖檔中符合旁行榜的塗改成按鈕用圖檔
r = []
for i in rl:
    r.append(i[1])

for i in imglist:
    n = i.split('.')[0]
    
    if n in r:
        #print('ok')
        setimg(i)


#設定視窗
win = tk.Tk()

win.title('Movie Rank')
#win.geometry('1280x720')


#f1,f2是上下層的容器
f1 = tk.Frame(win, bg = 'light cyan', width = 1280, height = 500)
f2 = tk.Frame(win, bg = 'light cyan', width = 1280, height = 220)

f1.pack(fill = 'both')
f2.pack(fill = 'both')


#把按鈕要用的圖檔都抓出來
img = []
for i in range(len(rl)):
    img1 = Image.open('btimg/{}.png'.format(rl[i][1]))
    img.append(ImageTk.PhotoImage(img1))


#按鈕的功能，rbl是按鈕的連結
rbl = []

for i in rl:
    rbl.append(i[0])
        
def bclick(x):
    webbrowser.open(rbl[x])





#頁數切換的功能，先清畫面，然後排按鈕，顯示排行跟名字
def pclick(x):
    
    for i in f1.winfo_children():
        i.destroy()
        
    
    
    for i in range(5):
        rank = x*5 + i
        
        button = tk.Button(f1, image = img[rank], bg = 'light cyan',
                           command = lambda x = rank:bclick(x))
        button.grid(row = 0, column = i)
        
        label = tk.Label(f1, text = rank+1, bg = 'light cyan',
                         font = ('Arial', 15))
        label.grid(row = 1, column = i)
        
        label2 = tk.Label(f1, text = rl[rank][1],
                          bg = 'light cyan',font = ('Arial', 15))
        label2.grid(row = 2, column = i)

#初始畫面
pclick(0)


#頁數的按鈕
for i in range(4):
    button = tk.Button(f2, text = i+1, 
                       bg = 'blue4', font = ('Arial', 15),
                       fg = 'yellow', command = lambda i = i:pclick(i))
    button.grid(row = 0, column = i)



win.mainloop()

