# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 13:06:23 2019

@author: pc
"""

import sqlite3, os, datetime

def opendb():
    if os.path.exists('FS.db'):
        return True
    else :
        return False

def wbuy(a,b,c):
    if opendb():
        string = ''
        try:
            t = datetime.datetime.now().date()
            
            conn = sqlite3.connect('FS.db')
            cursor = conn.cursor()
            
            s = ''' insert into buy(date, name, number, price) 
            values ('{}', '{}', '{}', '{}');
            '''.format(t,a,b,c)
            
            cursor.execute(s)
            conn.commit()
        except:
            string = 'error'
        else:
            string = '寫入完成'
        finally:
            conn.close()
            return string
    else :
        return '找不到資料庫'


def wsale(a,b,c):
    if opendb():
        string = ''
        try:
            t = datetime.datetime.now().date()
            
            conn = sqlite3.connect('FS.db')
            cursor = conn.cursor()
            
            s = ''' insert into sale(date, name, number, price) 
            values ('{}', '{}', '{}', '{}');
            '''.format(t, a, b, c)
            
            cursor.execute(s)
            conn.commit()
        except:
            string = 'error'
        else:
            string = '寫入完成'
        finally:
            conn.close()
            return string
    else :
        return '找不到資料庫'


def gdata(x):
    if opendb():
        string = ''
        try:
            
            conn = sqlite3.connect('FS.db')
            cursor = conn.cursor()
            
            s = ''' select * from {};
            '''.format(x)
            
            string = list(cursor.execute(s))
            
        except:
            string = 'error'
        
        finally:
            conn.close()
            return string
    else :
        return '找不到資料庫'



def wedit(a,b,c,d,e):
    if opendb():
        string = ''
        try:
            
            conn = sqlite3.connect('FS.db')
            cursor = conn.cursor()
            
            s = ''' update {} set name = '{}',
            number = {},
            price = {}
            where id = {};
            '''.format(a,b,c,d,e)
            
            cursor.execute(s)
            conn.commit()
            
        except:
            string = 'error'
        else:
            string = '修改成功'
        finally:
            conn.close()
            return string
    else :
        return '找不到資料庫'


def dedit(a,b):
    if opendb():
        string = ''
        try:
            
            conn = sqlite3.connect('FS.db')
            cursor = conn.cursor()
            
            s ='''delete from {} 
            where id = {};
            '''.format(a,b)
            
            cursor.execute(s)
            conn.commit()
            
        except:
            string = 'error'
        else:
            string = '刪除成功'
        finally:
            conn.close()
            return string
    else :
        return '找不到資料庫'

def rfdata():
    if opendb():
        string = ''
        try:
            
            conn = sqlite3.connect('FS.db')
            cursor = conn.cursor()
            
            s = ''' select * from flowersentence;
            '''
            
            string = list(cursor.execute(s))
            
        except:
            string = 'error'
        
        finally:
            conn.close()
            return string
    else :
        return '找不到資料庫'


def wfdata(a,b):
    if opendb():
        string = ''
        try:
            
            conn = sqlite3.connect('FS.db')
            cursor = conn.cursor()
            
            s = '''insert into flowersentence(name, sentence) 
            values ('{}', '{}');
            '''
            
            cursor.execute(s.format(a,b))
            conn.commit()
            string = '寫入成功'
            
        except:
            string = 'error'
        
        finally:
            conn.close()
            return string
    else :
        return '找不到資料庫'

def efdata(a,b,c):
    if opendb():
        string = ''
        try:
            
            conn = sqlite3.connect('FS.db')
            cursor = conn.cursor()
            
            s = '''update flowersentence set name = '{}',
            sentence = '{}'
            where id = {};
            '''
            
            cursor.execute(s.format(a,b,c))
            conn.commit()
            string = '寫入成功'
            
        except:
            string = 'error'
        
        finally:
            conn.close()
            return string
    else :
        return '找不到資料庫'

def dfdata(a):
    if opendb():
        string = ''
        try:
            
            conn = sqlite3.connect('FS.db')
            cursor = conn.cursor()
            
            s = '''delete from flowersentence 
            where id = {};
            '''
            
            cursor.execute(s.format(a))
            conn.commit()
            string = '刪除成功'
            
        except:
            string = 'error'
        
        finally:
            conn.close()
            return string
    else :
        return '找不到資料庫'



