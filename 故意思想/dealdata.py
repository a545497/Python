# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 19:01:05 2019

@author: pc

額外用來寫資料庫的程式碼
"""

import sqlite3 
import os

with open('mean.txt') as f:
    data = f.readlines()
    datas = []
    for i in data:
        a = i.strip()
        print(a)
        if a != '':
            datas.append(a)
    print(datas)



createsql = '''CREATE TABLE "{}" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"type"	TEXT,
	"sentence"	TEXT NOT NULL
);'''

intosql = ''' insert into {} values {}'''

type1 = "'myrecord'"

#os.remove('sentences.db')

if not os.path.exists('sentences.db'):
    conn = sqlite3.connect('sentences.db')
    try:
        conn.execute(createsql.format('record'))
        conn.commit()
    except Exception as e:
        print(e)
    else:
        print('had create record data table')

else:
    conn = sqlite3.connect('sentences.db')





"""
#conn.execute(createsql.format('test'))

for i in range(5):
    conn.execute(intosql.format('test(type,sentence)', '({}, "{}")'.format(
            type1, datas[i])))
    conn.commit()
"""

"""
for i in range(len(datas)):
    conn.execute(intosql.format('record(type,sentence)', '({}, \'{}\')'.format(
            type1, datas[i])))
    conn.commit()
"""



conn.close()


