# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:06:14 2019

@author: pc
"""

import tkinter as tk
import random as rd


win = tk.Tk()
win.geometry('500x500')
win.title('Have A Good Think')


with open('mean.txt') as f:
    data = f.readlines()
    datas = []
    for i in data:
        if i != '\n':
            a = i.strip()
            datas.append(a)
            
    
    #print(datas)


def nlcontrol():
    global string
    
    string = ''
    
    a = rd.randrange(0, len(datas))
    
    clist = [',',':','。',';','，','？']
    
    for i in range(len(datas[a])):
        if datas[a][i] in clist:
            string += '\n'
        else:
            string += datas[a][i]
    #print(string)





def click():
    global string
    
    nlcontrol()
    
    label.config(text = string)




f1 = tk.Frame(win, bg = 'palegreen',
              width = 500, height = 500)
f2 = tk.Frame(win, bg = 'palegreen', 
              width = 500, height = 500)
f1.pack(fill = 'both')
f2.pack(fill = 'both')


string = '故意思想美的事\n'
label = tk.Label(f1, text = string, bg = 'palegreen',
                 font = ('Arial', 16))
label.pack(fill = 'x', pady = 15)

button = tk.Button(f1, text = '來一句',
                   bg = 'DeepSkyBlue4', fg = 'yellow',
                   font = ('Arial', 16), width = 10, height = 1,
                   command = click)
button.pack(pady = 2)




win.mainloop()