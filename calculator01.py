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


bt0 = tk.Button(window,
                text = btext[0],
                font = 30,
                command = lambda: bthit(btext[0]))
bt0.place(x = btx[0], y = bty[0],
          width = bwid, height = bhei)
bt1 = tk.Button(window,
                text = btext[1],
                font = 30,
                command = lambda: bthit(btext[1]))
bt1.place(x = btx[1], y = bty[1],
          width = bwid, height = bhei)
bt2 = tk.Button(window,
                text = btext[2],
                font = 30,
                command = lambda: bthit(btext[2]))
bt2.place(x = btx[2], y = bty[2],
          width = bwid, height = bhei)
bt3 = tk.Button(window,
                text = btext[3],
                font = 30,
                command = lambda: bthit(btext[3]))
bt3.place(x = btx[3], y = bty[3],
          width = bwid, height = bhei)
bt4 = tk.Button(window,
                text = btext[4],
                font = 30,
                command = lambda: bthit(btext[4]))
bt4.place(x = btx[4], y = bty[4],
          width = bwid, height = bhei)
bt5 = tk.Button(window,
                text = btext[5],
                font = 30,
                command = lambda: bthit(btext[5]))
bt5.place(x = btx[5], y = bty[5],
          width = bwid, height = bhei)
bt6 = tk.Button(window,
              text = btext[6],
              font = 30,
              command = lambda: bthit(btext[6]))
bt6.place(x = btx[6], y = bty[6],
          width = bwid, height = bhei)
bt7 = tk.Button(window,
              text = btext[7],
              font = 30,
              command = lambda: bthit(btext[7]))
bt7.place(x = btx[7], y = bty[7],
          width = bwid, height = bhei)
bt8 = tk.Button(window,
              text = btext[8],
              font = 30,
              command = lambda: bthit(btext[8]))
bt8.place(x = btx[8], y = bty[8],
          width = bwid, height = bhei)
bt9 = tk.Button(window,
              text = btext[9],
              font = 30,
              command = lambda: bthit(btext[9]))
bt9.place(x = btx[9], y = bty[9],
          width = bwid, height = bhei)
bt10 = tk.Button(window,
              text = btext[10],
              font = 30,
              command = lambda: bthit(btext[10]))
bt10.place(x = btx[10], y = bty[10],
          width = bwid, height = bhei)
bt11 = tk.Button(window,
              text = btext[11],
              font = 30,
              command = lambda: bthit(btext[11]))
bt11.place(x = btx[11], y = bty[11],
          width = bwid, height = bhei)
def clrw():
    global numStr
    numStr = ''
    number.set(numStr)
bt12 = tk.Button(window,
              text = btext[12],
              font = 30,
              command = lambda: clrw())
bt12.place(x = btx[12], y = bty[12],
          width = bwid, height = bhei)
bt13 = tk.Button(window,
              text = btext[13],
              font = 30,
              command = lambda: bthit(btext[13]))
bt13.place(x = btx[13], y = bty[13],
          width = bwid, height = bhei)
def eqw():
    global numStr
    numStr = eval(numStr)
    number.set(numStr)
    numStr = ''
bt14 = tk.Button(window,
              text = btext[14],
              font = 30,
              command = lambda: eqw())
bt14.place(x = btx[14], y = bty[14],
          width = bwid, height = bhei)
bt15 = tk.Button(window,
              text = btext[15],
              font = 30,
              command = lambda: bthit(btext[15]))
bt15.place(x = btx[15], y = bty[15],
          width = bwid, height = bhei)





window.mainloop()
