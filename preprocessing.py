#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 17:52:01 2021

@author: gauravpatil
"""

import sqlite3
import uuid
import pandas as pd

data = pd.read_csv (r'/Users/gauravpatil/Fall 2021/Python/Contact Details/Contacts.cvs.csv')   
df = pd.DataFrame(data)

df.fillna(" ",inplace=True)

print(df)

conn=sqlite3.connect("cl.db")
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Contact (Contact_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Fname text, Mname text, Lname text)")
conn.commit()
conn.close()

conn=sqlite3.connect("cl.db")
cur=conn.cursor()

for row in df.itertuples():
    cur.execute(
                '''
                INSERT INTO Contact (Contact_id, Fname, Mname, Lname)
                VALUES (?,?,?,?)
                '''
                ,
                (row.contact_id, 
                row.first_name,
                row.middle_name,
                row.last_name)
                )
conn.commit()


conn=sqlite3.connect("cl.db")
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Address (Address_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Contact_id Integer, Address_type text, Address text, City text, State text, Zip text, FOREIGN KEY(Contact_id) REFERENCES Contact(Conatct_id))")
conn.commit()
conn.close()

conn=sqlite3.connect("cl.db")
cur=conn.cursor()

for row in df.itertuples():
    if row.home_address != "" and row.home_city != "" and row.home_state != "" and row.home_zip != "" :
        cur.execute(
                    '''
                    INSERT INTO Address (Contact_id, Address_type, Address, City, State, Zip)
                    VALUES (?,?,?,?,?,?)
                    '''
                    ,
                    (
                    row.contact_id, 
                    "home",
                    row.home_address,
                    row.home_city,
                    row.home_state,
                    row.home_zip)
                    )
    if row.work_address != "" and row.work_city != "" and row.work_state != "" and row.work_zip != "" :
        cur.execute(
                    '''
                    INSERT INTO Address (Contact_id, Address_type, Address, City, State, Zip)
                    VALUES (?,?,?,?,?,?)
                    '''
                    ,
                    (
                    row.contact_id, 
                    "work",
                    row.work_address,
                    row.work_city,
                    row.work_state,
                    row.work_zip)
                    )
conn.commit()

conn=sqlite3.connect("cl.db")
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Date (Date_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Contact_id Integer, Date_type text, Date text, FOREIGN KEY(Contact_id) REFERENCES Contact(Conatct_id))")
conn.commit()
conn.close()

conn=sqlite3.connect("cl.db")
cur=conn.cursor()

for row in df.itertuples():
    cur.execute(
                '''
                INSERT INTO Date (Contact_id, Date_type, Date)
                VALUES (?,?,?)
                '''
                ,
                (
                row.contact_id, 
                "Birth",
                row.birth_date)
                )
conn.commit()

conn=sqlite3.connect("cl.db")
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Phone (Phone_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Contact_id Integer, Phone_type text, Area_code text, Number text, FOREIGN KEY(Contact_id) REFERENCES Contact(Conatct_id))")
conn.commit()
conn.close()

conn=sqlite3.connect("cl.db")
cur=conn.cursor()

query = '''
        INSERT INTO Phone (Contact_id, Phone_type, Area_code, Number)
        VALUES (?,?,?,?)
        '''
        
        
for row in df.itertuples():
    if str(row.cell_phone) != '':
        temp = str(row.cell_phone).split('-')
        area_code = temp[0]
        number = '-'.join(temp[1:])
        #print("Cell",area_code,number)
        cur.execute(query,(row.contact_id,"Cell",area_code,number))
        
    if str(row.home_phone) != '':
        temp = str(row.home_phone).split('-')
        area_code = temp[0]
        number = '-'.join(temp[1:])
        #print("Home",area_code,number)
        cur.execute(query,(row.contact_id,"Home",area_code,number))
                    
    if str(row.work_phone) != '':
        temp = str(row.work_phone).split('-')
        area_code = temp[0]
        number = '-'.join(temp[1:])
        #print("Work",area_code,number)
        cur.execute(query,(row.contact_id,"Work",area_code,number))

conn.commit()
conn.close()

conn=sqlite3.connect("cl.db")
cur=conn.cursor()
cur.execute("SELECT Fname, Address_type, Zip FROM Address a, Contact c WHERE  a.Contact_id = c.Contact_id")
rows = cur.fetchall()
#print(rows)
conn.commit()
conn.close()
