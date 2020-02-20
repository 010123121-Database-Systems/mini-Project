import psycopg2
import re
# conn = psycopg2.connect("dbname=pgtest1 user=postgres password=123456")\
import json
import time
from datetime import date
import os
import ast
os.remove("db_book.json")
conn = psycopg2.connect(host="localhost",database="book1", user="postgres", password="123456")
conn.set_client_encoding('UTF8')
cur = conn.cursor() 
sqlText = 'SELECT b_id , b_name, b_page From book  LIMIT 5;'
# sqlText += 'From book'
ax1 = cur.execute(sqlText)
# print(cur.fetchone())
aa = {}
ri = []
count = 0
for i in cur.fetchall():
    aa = {'id':i[0],'name':i[1],'page':i[2]}
    ri.append(aa)
    count += 1
    with open('db_book.json', 'a') as f:
        json.dump(aa , f)
        f.write('\n')
print(ri)
# data_log = []
# r1 = {}
# f1= open("db_book.json","r")
# r1 = f1.read()
# print(type(r1))
# print(r1)
a=[]
if a is None:
    print('null')
else:
    print(a)
    
