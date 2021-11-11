#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 10:32:19 2021

@author: gauravpatil
"""

import sqlite3


def connect():
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Contact (Contact_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Fname text, Mname text, Lname text)")
    conn.commit()
    conn.close()
    
def get_Cid(fname,mname,lname) :
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("SELECT Contact_id FROM Contact WHERE Fname = ? AND Mname = ? AND Lname = ?",(fname,mname,lname));
    curr_cid = cur.fetchone()
    conn.commit()
    conn.close()
    return curr_cid
    
def insert():
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO Contact VALUES(NULL,?,?,?)",("GAURAV","VIJAY","PATIL"))
    conn.commit()
    conn.close()

def display():
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Contact")
    rows=cur.fetchall()
    #print(rows)
    conn.commit()
    conn.close()
    
def delete():
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM Contact")
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("SELECT Contact_id, Fname, Mname, Lname FROM Contact ")
    rows=cur.fetchall()
    #print(rows)
    conn.commit()
    conn.close()
    return rows

def get_Address(cid):
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("SELECT Address_type, Address, City, State, Zip FROM Address a, Contact c WHERE c.Contact_id = ? AND c.Contact_id = a.Contact_id ",[str(cid)])
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_Address_Details(cid,atype):
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("SELECT Address, City, State, Zip FROM Address WHERE Contact_id = ? AND Address_type = ? ",(str(cid),atype))
    rows=cur.fetchone()
    conn.commit()
    conn.close()
    return rows

def get_Phone_Details(cid,ptype):
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("SELECT Area_code, Number FROM Phone WHERE Contact_id = ? AND Phone_type = ? ",(cid,ptype))
    rows=cur.fetchone()
    #print(rows)
    conn.commit()
    conn.close()
    return rows

def get_Date_Details(cid,dtype):
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("SELECT Date FROM Date WHERE Contact_id = ? AND Date_type = ? ",(cid,dtype))
    rows=cur.fetchone()
    #print(rows)
    conn.commit()
    conn.close()
    return rows

def get_Address_Type(cid):
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("SELECT Address_type FROM Address WHERE Contact_id = ? ",[str(cid)])
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_Phone_Type(cid):
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("SELECT Phone_type FROM Phone WHERE Contact_id = ? ",[str(cid)])
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_Date_Type(cid):
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("SELECT Date_type FROM Date WHERE Contact_id = ? ",[str(cid)])
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows
    
def get_Phone(cid):
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("SELECT Phone_type, Area_code, Number FROM Phone p, Contact c WHERE c.Contact_id = ? AND c.Contact_id = p.Contact_id ",[str(cid)])
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_phone_table():
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("SELECT * From Phone")
    rows=cur.fetchall()
    #print(rows)
    conn.commit()
    conn.close()  
    
def get_Date(cid): 
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("SELECT DISTINCT Date_type, Date FROM Date WHERE Contact_id = ? ",[str(cid)])
    rows=cur.fetchall()
    #print(rows)
    conn.commit()
    conn.close()
    return rows

def get_date_table():
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("SELECT * From Date")
    rows=cur.fetchall()
    #print(rows)
    conn.commit()
    conn.close() 

def update_Address(cid, oatype, atype, address, city, state, tzip):
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("UPDATE Address SET Address_type = ?, Address = ?, City = ?, State = ?, Zip = ? WHERE Contact_id = ? AND Address_type = ?",(atype, address, city, state, tzip, cid, oatype))
    conn.commit()
    conn.close()
    
def update_Date(cid, odtype, dtype, date):
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("UPDATE Date SET Date_type = ?, Date = ? WHERE Contact_id = ? AND Date_type = ?",(dtype, date, cid, odtype))
    conn.commit()
    conn.close()

def update_Number(cid, ontype, ntype, ncode, number):
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("UPDATE Phone SET Phone_type = ?, Area_code = ?, Number = ? WHERE Contact_id = ? AND Phone_type = ?",(ntype, ncode, number, cid, ontype))
    conn.commit()
    conn.close()
    
def update_Name(cid, fname, mname, lname):
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("UPDATE Contact SET Fname = ?, Mname = ?, Lname = ? WHERE Contact_id = ? ",(fname, mname, lname, str(cid)))
    conn.commit()
    conn.close()
    
def get_Name(cid):
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("SELECT Fname, Mname, Lname FROM Contact WHERE Contact_id = ?",[str(cid)])
    rows=cur.fetchone()
    conn.commit()
    conn.close()
    return rows

def insert_Newvalues(fname,mname,lname,user_address,user_phone,user_date):
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO Contact (Fname, Mname, Lname) VALUES (?,?,?)",(fname, mname, lname))
    conn.commit()
    cur.execute("SELECT Contact_id from Contact order by Contact_id DESC limit 1")
    cid = cur.fetchone()
    #print(cid)
    for each_addr in user_address:
        each_addr=each_addr[0:75]+str(cid[0])+each_addr[75:]
        cur.execute(each_addr)
        conn.commit()
    for each_phone in user_phone:
        each_phone=each_phone[0:65]+str(cid[0])+each_phone[65:]   
        cur.execute(each_phone) 
        conn.commit()
    for each_date in user_date:
        each_date=each_date[0:51]+str(cid[0])+each_date[51:]   
        cur.execute(each_date)
        conn.commit()
    conn.close()
    
def search(element):
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("SELECT DISTINCT c.Contact_id,c.Fname,c.Mname,c.Lname FROM Contact c JOIN Address a ON c.Contact_id=a.Contact_id JOIN Phone p on c.Contact_id=p.Contact_id JOIN Date d on c.Contact_id=d.Contact_id WHERE (c.Fname || c.Mname || c.Lname || a.Address_type || a.Address || a.City || a.State || a.Zip || p.Phone_type || p.Area_code || p.Number || d.Date_type || d.Date) LIKE '%"+element+"%';")
    rows = cur.fetchall()
    #print(rows)
    conn.commit()
    conn.close()
    return rows

def delete_address_table(cid):
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM Address WHERE Contact_id = ?",[str(cid)])
    conn.commit()
    conn.close()
    
def delete_phone_table(cid):
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM Phone WHERE Contact_id = ?",[str(cid)])
    conn.commit()
    conn.close()
    
def delete_date_table(cid):
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM Date WHERE Contact_id = ?",[str(cid)])
    conn.commit()
    conn.close()

def delete_contact_table(cid):
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM Contact WHERE Contact_id = ?",[str(cid)])
    conn.commit()
    conn.close()
    
def new_address(cid,atype, address, city, state, tzip):
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO Address (Contact_id, Address_type, Address, City, State, Zip) VALUES (?,?,?,?,?,?)",(str(cid),atype, address, city, state, tzip))
    conn.commit()                                                                                                            
    conn.close()
    
def new_phone(cid,n_type,area_code,number):
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO Phone (Contact_id, Phone_type, Area_code, Number) VALUES (?,?,?,?)",(str(cid),n_type, area_code, number))
    conn.commit()                                                                                                            
    conn.close()
    
def new_date(cid,dtype,date):
    conn=sqlite3.connect("cl.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO Date (Contact_id, Date_type, Date) VALUES (?,?,?)",(str(cid),dtype, date))
    conn.commit()                                                                                                            
    conn.close()
    
