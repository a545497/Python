# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 14:30:06 2019

This is the main window for the system

@author: Qing
"""

import tkinter as tk
import wts

win = tk.Tk()

w = 1280
h = 720

win.geometry('{}x{}'.format(w,h))

win.title('Flower_Shop_System')

wf = tk.Frame(win, width = w, height = h, bg = 'bisque')
wf.pack(fill = 'both')
wfbg = tk.Frame(win, width = w, height = h, bg = 'bisque')
wfbg.pack(fill = 'both')

f1 = tk.Frame(wf, width = 100, height = h, bg = 'bisque')
f1.pack(side = 'left', fill = 'both')

f2 = tk.Frame(wf, width = w - 100, height = h, bg = 'bisque')
f2.pack( fill = 'both')

####################介面####################

entry = ''
entry1 = ''
entry2 = ''
t = tk.StringVar()
t1 = tk.StringVar()
t2 = tk.StringVar()

def interface(x,f):
    global entry 
    global entry1 
    global entry2 
    textlist = ['{}品項','{}數量','{}單價']
    for i in range(len(textlist)):
        textlist[i] = textlist[i].format(x)
    
    label = tk.Label(f, text = textlist[0], font = ('Arial', 18))
    label.pack(pady = 5)
    entry = tk.Entry(f, font = ('Arial', 18), textvariable = t)
    entry.pack(pady = 5)
    label = tk.Label(f, text = textlist[1], font = ('Arial', 18))
    label.pack(pady = 5)
    entry1 = tk.Entry(f, font = ('Arial', 18), textvariable = t1)
    entry1.pack(pady = 5)
    label = tk.Label(f, text = textlist[2], font = ('Arial', 18))
    label.pack(pady = 5)
    entry2 = tk.Entry(f, font = ('Arial', 18), textvariable = t2)
    entry2.pack(pady = 5)
    






####################買進的介面功能####################
def bclick(a,b,c):
    global lb
    string = wts.wbuy(a,b,c)
    lb.config(text = string)
    
lb = ''   
def buyin():
    '''
    進貨的介面
    '''
    global lb
    for i in f2.winfo_children():
        i.destroy()
    
    t.set('')
    t1.set('')
    t2.set('')
    
    interface('買入', f2)
    button = tk.Button(f2, text = '寫入', font = ('Arial', 18),
    command = lambda :bclick(entry.get(), entry1.get(), entry2.get()))
    button.pack(pady = 5)
    lb = tk.Label(f2, text = '', font = ('Arial', 18))
    lb.pack(pady = 5)
    


####################賣出的介面功能####################   
def sclick(a,b,c):
    global ls
    string = wts.wsale(a,b,c)
    ls.config(text = string)

ls = ''
def saleout():
    global ls
    
    for i in f2.winfo_children():
        i.destroy()
    
    t.set('')
    t1.set('')
    t2.set('')
    
    interface('賣出', f2)
    button = tk.Button(f2, text = '寫入', font = ('Arial', 18),
    command = lambda :sclick(entry.get(), entry1.get(), entry2.get()))
    button.pack(pady = 5)
    ls = tk.Label(f2, text = '', font = ('Arial', 18))
    ls.pack(pady = 5)



####################編輯的介面功能####################
def editdata(d,a,b,c):
    global tb
    #print(d,a,b,c)
    if datafrom == 'b':
        s = wts.wedit('buy',a,b,c,d)
    else:
        s = wts.wedit('sale',a,b,c,d)
    tb.config(text = s)

def dedit(x):
    global tb
    global datas
    if datafrom == 'b':
        string = wts.dedit('buy',x)
        datas = wts.gdata('buy')
    else:
        string = wts.dedit('sale',x)
        datas = wts.gdata('sale')
    tb.config(text = string)
    edit()

def eclick(x):
    global tlist
    global tliststr
    global page
    global datas
    global datafrom
    global tb
    
    
    if x == etext[0]:
        #print('buy')
        page = 0
        datas = wts.gdata('buy')
        
        data = []
        for i in range(page*10, page*10 + 10):
            if i<len(datas):
                data.append(datas[i])
            else:
                break
        tliststr.set(data)
        datafrom = 'b'
        
    elif x == etext[1]:
        datas = wts.gdata('sale')
        data = []
        for i in range(page*10, page*10 + 10):
            if i<len(datas):
                data.append(datas[i])
            else:
                break
        tliststr.set(data)
        datafrom = 's'
        
    elif x == etext[2]:
        
        if page > 0:
            page -= 1
            data = []
            for i in range(page*10, page*10 + 10):
                if i<len(datas):
                    data.append(datas[i])
                else:
                    break
            tliststr.set(data)
    
        
    elif x == etext[3]:
        try:
            elistdata = datas[tlist.curselection()[0] + page*10 ]
            #print(elistdata)
        except:
            return
        
        for i in f3.winfo_children():
            i.destroy()
        
        
        t.set(elistdata[2])
        t1.set(elistdata[3])
        t2.set(elistdata[4])
        
        if datafrom == 'b':
            interface('買入', f3)
            button = tk.Button(f3, text = '寫入', font = ('Arial', 18),
            command = lambda :editdata(elistdata[0],entry.get(), entry1.get(), entry2.get())).pack(pady = 5)
            tb=tk.Label(f3, text = '', font = ('Arial', 18))
            tb.pack(pady = 5)
            
        else:
            interface('賣出', f3)
            button = tk.Button(f3, text = '寫入', font = ('Arial', 18),
            command = lambda :editdata(elistdata[0],entry.get(), entry1.get(), entry2.get()))
            button.pack(pady = 5)
            tb = tk.Label(f3, text = '', font = ('Arial', 18))
            tb.pack(pady = 5)
        button = tk.Button(f3, text = '刪除',font = ('Arial', 18),
                           command = lambda : dedit(elistdata[0])).pack(pady = 5)
        
        button = tk.Button(f3, text = '返回', font = ('Arial', 18),
        command = lambda :edit()).pack(pady = 5)
        
        
        
    elif x == etext[4]:
        if len(datas) % 10 != 0:
            if len(datas)// 10 == 0:
                return
            if page < len(datas)// 10 :
                page += 1
                data = []
                for i in range(page*10, page*10 + 10):
                    if i<len(datas):
                        data.append(datas[i])
                    else:
                        break
                tliststr.set(data)
                
                
        else:
            if page < len(datas)//10:
                page += 1
                data = []
                for i in range(page*10, page*10 + 10):
                    if i<len(datas):
                        data.append(datas[i])
                    else:
                        break
                tliststr.set(data)
                
tb = ''    
page = 0
datas = []
f3 = ''
tlist = ''
tliststr = ''
etext = ['買入','銷售','上一頁','選取','下一頁']
datafrom = ''
def edit():
    global f3
    global tlist
    global tliststr
    
    for i in f2.winfo_children():
        i.destroy()
    
    f3 = tk.Frame(f2, bg = 'bisque')
    f3.pack()
    
    tliststr = tk.StringVar()
    
    if datafrom != '':
        tliststr.set(datas)
    else:
        tliststr.set('')
    
    tlist = tk.Listbox(f3,listvariable = tliststr, font = ('Arial', 18),
                       width = 30, height = 15)
    
    for t,i in enumerate(etext[:2]):
        string = i
        button = tk.Button(f3, text = string, font = ('Arial', 18),
        command = lambda string = string : eclick(string))
        button.grid(row = 0, column = t)
    
    tlist.grid(row = 1, column = 0, columnspan = 6)
    
    for t,i in enumerate(etext[2:]):
        string = i
        button = tk.Button(f3, text = string, font = ('Arial', 18),
        command = lambda string = string : eclick(string))
        button.grid(row = 3, column = t)



####################花語的編輯功能####################
def fifclick():
    global faid
    global faentry
    global faentry1
    if faid == '':
        write = wts.wfdata(faentry.get(), faentry1.get())
        fiftxt.config(text = write)
    else:
        write = wts.efdata(faentry.get(), faentry1.get(), faid)
        fiftxt.config(text = write)

fiftxt = ''
def finterface():
    global faentry
    global faentry1
    global fiftxt
    
    label = tk.Label(f2, text = '花名', font = ('Arial', 18))
    label.pack(pady= 5)
    faentry = tk.Entry(f2, font = ('Arial', 18), textvariable = fat1)
    faentry.pack(pady = 5)
    label = tk.Label(f2, text = '花語', font = ('Arial', 18))
    label.pack(pady= 5)
    faentry1 = tk.Entry(f2, font = ('Arial', 18), textvariable = fat2)
    faentry1.pack(pady = 5)
    button = tk.Button(f2, text = '寫入', font = ('Arial', 18),
                       command = fifclick)
    button.pack(pady = 5)
    fiftxt = tk.Label(f2, text = '', font = ('Arial', 18))
    fiftxt.pack(pady = 5)
    
faentry = ''
faentry1 = ''
fat1 = tk.StringVar()
fat2 = tk.StringVar()
def fwadd():
    for i in f2.winfo_children():
        i.destroy()
    
    fat1.set('')
    fat2.set('')
    finterface()
    button = tk.Button(f2, text = '返回', font = ('Arial', 18),
                       command = fedit)
    button.pack(pady = 5)

falist = ''
faltxt = tk.StringVar()
faid = ''
def dfedit():
    global faid
    global falistdata
    global faltxt
    write = wts.dfdata(faid)
    fiftxt.config(text = write)
    falistdata = ''
    fwedit()
    
def fweclick(x, y = ''):
    global f2
    global falist
    global falistdata
    global faid
    global sk
    sk = y
    if x == '搜索':
        if y != '':
            data = []
            for i in fadata:
                if y in i[1] or y in i[2]:
                    data.append(i)
            falistdata = data
            faltxt.set(falistdata)
        else:
            falistdata = fadata
            faltxt.set(falistdata)
    elif x == '選擇':
        for i in f2.winfo_children():
            i.destroy()
        
        data = falistdata[y]
        #print(data)
        faid = data[0]
        fat1.set(data[1])
        fat2.set(data[2])
        finterface()
        button = tk.Button(f2, text = '刪除', font = ('Arial', 18),
                       command = dfedit )
        button.pack(pady = 5)
        button = tk.Button(f2, text = '返回', font = ('Arial', 18),
                       command = fwedit)
        button.pack(pady = 5)

fadata = ''
falistdata = ''  
sk = '' 
def fwedit():
    global f3
    global falist
    global falistdata
    global fadata

    for i in f2.winfo_children():
        i.destroy()
        
    f3 = tk.Frame(f2, bg = 'bisque')
    f3.pack()
    
    entry = tk.Entry(f3, font = ('Arial', 18))
    entry.grid(row = 0, column = 0)
    button = tk.Button(f3, text = '搜索', font = ('Arial', 18),
                       command = lambda: fweclick(x = '搜索', y = entry.get()))
    button.grid(row = 0, column =1)
    
    fadata = wts.rfdata() 
    if falistdata == '':
        falistdata = fadata
    faltxt.set(falistdata)
    falist = tk.Listbox(f3, listvariable = faltxt, font = ('Arial', 18),
                        width = 50, height = 20)
    falist.grid(row = 1, column  = 0, columnspan = 2)
    button = tk.Button(f3, text = '選擇', font = ('Arial', 18),
                       command = lambda : fweclick(x = '選擇', y = falist.curselection()[0]))
    button.grid(row = 2, column = 0)
    button1 = tk.Button(f3, text = '返回', font = ('Arial', 18),
                        command = fedit)
    button1.grid(row = 2, column = 1)


def fedit():
    global faid
    global falistdata
    for i in f2.winfo_children():
        i.destroy()
        
    faid = ''
    falistdata = ''
    button = tk.Button(f2, text = '新增', font = ('Arial', 18),
                       command = fwadd)
    button.pack(pady = 5)
    button = tk.Button(f2, text = '編輯', font = ('Arial', 18),
                       command = fwedit)
    button.pack(pady = 5)




####################花語的查詢功能####################
def flowerpage(x):
    global fpage
    global fdata
    
    if x == '上一頁':
        if fpage > 0:
            fpage -= 1
            data = []
            for i in range(fpage*10, fpage*10 + 10):
                if i<len(fdata):
                    data.append(fdata[i])
                else:
                    break
            fstr.set(data)
            
    elif x == '下一頁':
        if len(fdata) % 10 != 0:
            if len(fdata)// 10 == 0:
                return
            if fpage < len(fdata)// 10 :
                fpage += 1
                data = []
                for i in range(fpage*10, fpage*10 + 10):
                    if i<len(fdata):
                        data.append(fdata[i])
                    else:
                        break
                fstr.set(data)
          
        else:
            if fpage < len(fdata)//10:
                fpage += 1
                data = []
                for i in range(fpage*10, fpage*10 + 10):
                    if i<len(fdata):
                        data.append(fdata[i])
                    else:
                        break
                fstr.set(data)
    elif x == fwtext[0]:
        data = []
        for i in fdata:
            if fentry.get() in i[1] or fentry.get() in i[2]:
                data.append(i)
        fstr.set(data)
            

fentry = ''
fpage = 0
fdata = []
fstr = tk.StringVar()

def fclick(x):
    global fdata
    global fentry
    
    for i in f3.winfo_children():
        i.destroy()
    
    fdata = wts.rfdata()
    
    if x == fwtext[0]:
        fstr.set('')
        fentry = tk.Entry(f3, font = ('Arial', 18),)
        fentry.grid(row = 0, column = 0)
        button = tk.Button(f3, text = x, font = ('Arial', 18),
                           command = lambda x = x: flowerpage(x))
        button.grid(row = 0, column = 1)
        flist = tk.Listbox(f3, listvariable = fstr, font = ('Arial', 18),
                       width = 50, height = 20)
        flist.grid(row = 1, column = 0, columnspan = 6)
    else:
        label = tk.Label(f3, text = '', font = ('Arial', 18),bg = 'bisque')
        label.grid(row = 0, column = 1)
        if x == fwtext[1]:
            data = []
            for i in range(fpage*10, fpage*10 + 10):
                if i<len(fdata):
                    data.append(fdata[i])
                else:
                    break
            fstr.set(data)
    
        flist = tk.Listbox(f3, listvariable = fstr, font = ('Arial', 18),
                           width = 50, height = 10)
        flist.grid(row = 1, column = 0, columnspan = 6)
        
        button = tk.Button(f3, text = '上一頁', font = ('Arial', 18),
                command = lambda :flowerpage('上一頁'))
        button.grid(row = 2, column = 0)
        button = tk.Button(f3, text = '下一頁', font = ('Arial', 18),
                    command = lambda :flowerpage('下一頁'))
        button.grid(row = 2, column = 1)
        


fwtext = ['搜索','全部']

def flowerword():
    global f3
    global fpage
    
    fpage = 0
    
    for i in f2.winfo_children():
        i.destroy()
    
    f3 = tk.Frame(f2, bg = 'bisque')
    f3.pack()
    
    for i in fwtext:
        string = i
        button = tk.Button(f3, text = string, font = ('Arial', 18),
        command = lambda string = string:fclick(string))
        button.pack(pady = 5)
    
    





####################左側的功能####################
def click(x):
    global datafrom
    if x == btext[0]:
        buyin()
    elif x == btext[1]:
        saleout()
    elif x == btext[2]:
        datafrom = ''
        edit()
    elif x == btext[3]:
        fedit()
    else:
        flowerword()
            



btext = ['進貨', '賣出', '編輯', '花語編輯', '花語']

for i in btext:
    s = i
    button = tk.Button(f1, text = s,
                       bg = 'dark green', fg = 'yellow',
                       font = ('Arial', 18), 
                       command = lambda s = s:click(s))
    button.pack(padx = 2, pady = 2, fill = 'x')



win.mainloop()
