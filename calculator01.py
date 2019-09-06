# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 13:16:30 2019

@author: pc
"""

import tkinter as tk

window = tk.Tk()
window.geometry('500x500')
window.title('CalCuLaTor')

numStr = ''
number = tk.StringVar(value = numStr)
numberlb = tk.Label(window,
                    textvariable = number,
                    font = 30,
                    bg = 'white')
numberlb.place(x = 0, y = 0,
               width = 500, height = 50)

def mbw():
    global numStr
    global number
    if len(numStr) > 0:
        if len(numStr) > 1:
            numStr = numStr[0:-1]
        else:
            numStr = ''
    number.set(numStr)
minb = tk.Button(window,
                 text = '<',
                 command = lambda: mbw())
minb.place(x = 450, y = 0,
           width = 50, height = 50)

def bthit(a):
    global numStr
    if a == 'C':
        numStr = ''
    elif a == '=':
        numStr = str(eval(numStr))
    else:
        numStr += a
    number.set(numStr)


btext = ['7','8','9','+','4','5','6','-','1','2','3','*','C','0','=','/']

bwid = 500//4
bhei = 450//4
bx = (500%4)//2
by = 50+((450%4)//2)
btx = []
bty = []
for i in range(16):
    if (i+1) % 4 == 0:
        btx.append(bx)
        bty.append(by)
        bx = (500%4)//2
        by += bhei
    else:
        btx.append(bx)
        bty.append(by)
        bx += bwid

btlist = [0]*16

for i in range(16):
    btstring = btext[i]
    btlist[i]= tk.Button(window,
          text = btstring,
          font = 30,
          command = lambda btstring = btstring: bthit(btstring))
    
    btlist[i].place(x = btx[i], y = bty[i],
          width = bwid, height = bhei)



window.mainloop()
