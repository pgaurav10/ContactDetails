#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 14:44:52 2021

@author: gauravpatil
"""

from datetime import date
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry

import backend

i=0
j=0
k=0
contacts_added=0
user_address=[]
user_phone=[]
user_date=[]

global selected_tuple
global selected_date_tuple
global selected_address_tuple
global selected_phone_tuple

selected_address_tuple = " "
selected_date_tuple = " "
selected_phone_tuple = " "

def view_command():
    refresh_address()
    refresh_phone()
    refresh_date()
    
    list1.delete(0,END)
    list2.delete(0,END)
    list3.delete(0,END)
    list4.delete(0,END)
    rows = backend.view()
    i_row = []
    print(rows)
    for row in rows:
        i_row.clear()
        i_cid = row[0]
        i_fname = row[1]
        i_mname = row[2]
        i_lname = row[3]
        
        i_row.append(i_cid)
        i_row.append(i_fname)
        if i_mname != ' ' and i_mname != '':
            i_row.append(i_mname)
        if i_lname != ' ' and i_lname != '':
            i_row.append(i_lname)
        
    
        list1.insert(END,i_row)
        
def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    list2.delete(0, END)
    list3.delete(0, END)
    list4.delete(0, END)
    global cid
    
    cid = selected_tuple[0]
    
    displayAddress(event)
    displayDate(event)
    displayPhone(event)
    displayName(event)
    
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    
    e11.delete(0,END)
    e12.delete(0,END)
    
    e21.delete(0,END)
    e22.delete(0,END)
    
def displayName(event):
    rows = backend.get_Name(cid)
    
    e31.delete(0,END)
    e32.delete(0,END)
    e33.delete(0,END)
    
    e31.insert(END, rows[0])
    e32.insert(END, rows[1])
    e33.insert(END, rows[2])
    
    
def get_selected_address_row(event):
    
    global selected_address_tuple
    address_index=list3.curselection()[0]
    selected_address_tuple=list3.get(address_index)
    
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    
    rows = backend.get_Address_Details(cid,selected_address_tuple)
    
    e1.insert(END,rows[0])
    e2.insert(END,rows[1])
    e3.insert(END,rows[2]) 
    e4.insert(END,rows[3])
    e5.insert(END,selected_address_tuple)
    
def displayAddress(event):
    rows = backend.get_Address(cid) 
    
    for row in rows:
        list3.insert(END, row[0])  
    
def get_selected_phone_row(event): 
    global selected_phone_tuple
    phone_index=list4.curselection()[0]
    selected_phone_tuple=list4.get(phone_index)
    
    rows = backend.get_Phone_Details(cid,selected_phone_tuple)
    
    #print(rows)
    e11.delete(0,END)
    e11.insert(END,str(rows[0]+"-"+rows[1]))
    
    e12.delete(0,END)
    e12.insert(END, selected_phone_tuple)
    
def displayPhone(event):
    rows = backend.get_Phone(cid)
    
    for row in rows:
        list4.insert(END, row[0])
    
def get_selected_date_row(event):
    global selected_date_tuple
    date_index=list2.curselection()[0]
    selected_date_tuple=list2.get(date_index)
    
    rows = backend.get_Date_Details(cid,selected_date_tuple)
    
    e21.delete(0,END)
    e22.delete(0,END)
    
    e21.insert(END,selected_date_tuple)
    e22.insert(END,rows)

def displayDate(event):
    rows = backend.get_Date(cid)
    
    for row in rows:
        list2.insert(END, row[0])
        
def search():
    refresh_address()
    refresh_phone()
    refresh_date()
    
    list1.delete(0,END)
    list2.delete(0,END)
    list3.delete(0,END)
    list4.delete(0,END)
    temp = search_entry.get()
    entries = temp.split(" ")
    
    #print(entries)
    result = []
    for entry in entries:
        temp = backend.search(entry)
        for t in temp:
            if t not in result:
                result.append(t)
    
    s_row = []
    for row in result :
        s_row.clear()
        s_cid = row[0]
        s_fname = row[1]
        s_mname = row[2]
        s_lname = row[3]
        
        s_row.append(s_cid)
        s_row.append(s_fname)
        if s_mname != ' ':
            s_row.append(s_mname)
        if s_lname != ' ':
            s_row.append(s_lname)
            
        list1.insert(END,s_row)
        
def update_command():
    
    address_type = address_type_text.get()
    address = address_text.get()
    city = city_text.get()
    zip_u = zip_text.get()
    state = state_text.get()
    
    date_type = type_text.get()
    date = date_text.get()
    
    number = number_text.get()
    n_type = number_type.get()
    
    fname = fname_text.get()
    mname = mname_text.get()
    lname = lname_text.get()
    
    if selected_address_tuple != " " :
        backend.update_Address(cid, selected_address_tuple, address_type, address, city, state, zip_u)
    
    if selected_date_tuple != " ":
        backend.update_Date(cid, selected_date_tuple, date_type, date);
    
    temp = str(number).split('-')
    area_code = temp[0]
    number = '-'.join(temp[1:])
    
    if selected_phone_tuple != " ":
        backend.update_Number(cid, selected_phone_tuple, n_type, area_code, number)
        
    backend.update_Name(cid, fname, mname, lname)

def new_address():
    address_type = address_type_text.get()
    address = address_text.get()
    city = city_text.get()
    zip_u = zip_text.get()
    state = state_text.get()
    
    types = backend.get_Address_Type(cid)
    
    curr_types = []
    for t in types:
        curr_types.append(t[0])
    
    #print(curr_types)
    if address_type not in curr_types:    
        backend.new_address(cid, address_type, address, city, state, zip_u)

def new_phone():
    number = number_text.get()
    n_type = number_type.get()
    
    types = backend.get_Phone_Type(cid)
    
    curr_types = []
    for t in types:
        curr_types.append(t[0])
    
    #print(curr_types)
    if n_type not in curr_types: 
        temp = str(number).split('-')
        area_code = temp[0]
        number = '-'.join(temp[1:])
        backend.new_phone(cid, n_type,area_code, number)

def new_date():
    date_type = type_text.get()
    date = date_text.get()
    
    types = backend.get_Date_Type(cid)
    
    curr_types = []
    for t in types:
        curr_types.append(t[0])
        
    if date_type not in curr_types:
        backend.new_date(cid,date_type,date)
    
def insert_command():
    insert_window = Toplevel(window)
    insert_window.title("Add Details")
    insert_window.geometry("750x400")
    
    details_frame = LabelFrame(insert_window, text=" User Details ",height=10,width = 20)
    details_frame.grid(row=0, column=0)

    fname_label= Label(details_frame ,text = "First Name").grid(row = 0,column = 0)
    mname_label= Label(details_frame ,text = "Middle Name").grid(row = 1,column = 0)
    mname_label= Label(details_frame ,text = "Last Name").grid(row = 2,column = 0)
    
    fname_text = Entry(details_frame)
    fname_text.grid(row = 0,column = 1)
    mname_text = Entry(details_frame)
    mname_text.grid(row = 1,column = 1)
    lname_text = Entry(details_frame)
    lname_text.grid(row = 2,column = 1)
    
    asthetic_gap=Label(insert_window,text=" ").grid(row=0,column=2)
    
    #Adddress Details
    iaddress_frame = LabelFrame(insert_window, text=" Add Address ",height=10,width = 20)
    iaddress_frame.grid(row=1, column=0)
    
    def add_addresses():
        global user_address
        global i
        i+=1
        t_addr_type="'"+addr_type.get()+"'"
        t_addr="'"+addr.get()+"'"
        t_city="'"+city.get()+"'"
        t_state="'"+state.get()+"'"
        t_zip="'"+addr_zip.get()+"'"
        if t_addr_type=="":t_addr_type="''"
        if t_addr=="":t_addr="''"
        if t_city=="":t_city="''"
        if t_state=="":t_state="''"
        if t_zip=="":t_zip="''"
        temp1="insert into Address(Contact_id,address_type,address,city,state,zip) values(,"+t_addr_type+","+t_addr+","+t_city+","+t_state+","+t_zip+");"
        user_address.append(temp1)
        address_count = Label(iaddress_frame,text=str(i)+" address(es) added",).grid(row=5,column=1)
        addr_type.delete(0,END)
        addr.delete(0,END)
        city.delete(0,END)
        state.delete(0,END)
        addr_zip.delete(0,END)
    
    
    addr_type_label=Label(iaddress_frame, text = "Address type").grid(row=0,column=0)
    addr_label= Label(iaddress_frame ,text = "Address").grid(row = 1,column = 0)
    city_label = Label(iaddress_frame ,text = "City").grid(row = 2,column = 0)
    state_label = Label(iaddress_frame ,text = "State").grid(row = 3,column = 0)
    zip_label = Label(iaddress_frame ,text = "Zip").grid(row = 4,column = 0)
    
    addr_type=Entry(iaddress_frame)
    addr_type.grid(row=0,column=1)
    addr = Entry(iaddress_frame)
    addr.grid(row = 1,column = 1)
    city = Entry(iaddress_frame)
    city.grid(row = 2,column = 1)
    state = Entry(iaddress_frame)
    state.grid(row = 3,column = 1)
    addr_zip = Entry(iaddress_frame)
    addr_zip.grid(row = 4,column = 1)
    addr_submit=Button(iaddress_frame,text="Add Address", command=lambda:add_addresses())
    addr_submit.grid(row=5,column=0)
    
    #Phone Details
    
    
    iphone_frame = LabelFrame(insert_window, text=" Add Phone ",height=10,width = 20)
    iphone_frame.grid(row=0, column=1)

    def add_phone():
        global user_phone
        global j
        j+=1
        temp_phone_type="'"+phone_type.get()+"'"
        #temp_area_code="'"+area_code.get()+"'"
        temp_phone="'"+phone.get()+"'"
        if temp_phone_type=="":temp_phone_type="''"
        #if temp_area_code=="":temp_area_code="''"
        if temp_phone=="":temp_phone="''"
        temp2="insert into Phone(Contact_id,Phone_type,Area_code,Number) values(,"+temp_phone_type+","+temp_phone[0:4]+"','"+temp_phone[5:]+");"
        #print(temp2)
        user_phone.append(temp2)
        #print(user_phone)
        phone_count = Label(iphone_frame,text=str(j)+" phone(s) added").grid(row=2,column=1)
        phone_type.delete(0,END)
        #area_code.delete(0,END)
        phone.delete(0,END)

    phone_type_lb=Label(iphone_frame, text = "Phone type").grid(row=0,column=0)
    
    phone_lb = Label(iphone_frame ,text = "Phone").grid(row = 1,column = 0)
    phone_type=Entry(iphone_frame)
    phone_type.grid(row=0,column=1)

    phone = Entry(iphone_frame)
    phone.grid(row = 1,column = 1)
    phone.insert(0,"xxx-xxx-xxxx")

    phone_submit=Button(iphone_frame,text="Add Number", command=lambda:add_phone())
    phone_submit.grid(row=2,column=0)

    #Add Date Details

    idate_frame = LabelFrame(insert_window, text=" Add Date ",height=20,width = 20)
    idate_frame.grid(row=1, column=1,rowspan=2)
    
    def add_date():
        global user_date
        global k
        k+=1
        temp_date_type="'"+date_type.get()+"'"
        temp_date="'"+str(date1.get_date())+"'"
        if temp_date_type=="":temp_date_type="''"
        if temp_date=="":temp_date="''"
        temp3="insert into Date(Contact_id,Date_type,Date) values(,"+temp_date_type+","+temp_date+");"
        user_date.append(temp3)
        #print(user_date)
        phone_count = Label(idate_frame,text=str(k)+" date(s) added").grid(row=2,column=1)
        date_type.delete(0,END)

    date_type_lb=Label(idate_frame, text = "Date type").grid(row=0,column=0)
    date_lb = Label(idate_frame ,text = "Date").grid(row =1 ,column = 0)
    date_type=Entry(idate_frame)
    date_type.grid(row=0,column=1)
    date1=DateEntry(idate_frame, locale='en_US', date_pattern='yyyy-mm-dd')
    date1.grid(row=1,column=1)
    date_submit=Button(idate_frame,text="Add date", command=lambda:add_date())
    date_submit.grid(row=2,column=0)
    
    def insert_into_database():
        global user_address,user_phone,user_date
        
        backend.insert_Newvalues(fname_text.get(), mname_text.get(), lname_text.get(), user_address, user_phone, user_date)
        
        global i,j,k
        i=0
        j=0
        k=0
        
        global contacts_added
        contacts_added=0
        
        user_address=[]
        user_phone=[]
        user_date=[]
        
        insert.destroy()
    
    submit_all=Button(insert_window,text="SUBMIT",padx=50,command=lambda:insert_into_database())
    submit_all.grid(row=2,column=1)

def refresh_address():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)

def refresh_phone():
    e11.delete(0,END)
    e12.delete(0,END)
    
def refresh_date():
    e21.delete(0,END)
    e22.delete(0,END)

def refresh():
    
    search_entry.delete(0,END)
    
    e31.delete(0,END)
    e32.delete(0,END)
    e33.delete(0,END)
    
    list1.delete(0,END)
    list2.delete(0,END)
    list3.delete(0,END)
    list4.delete(0,END)
    
    refresh_address()
    refresh_phone()
    refresh_date()

def delete_command():
    backend.delete_address_table(cid)
    backend.delete_date_table(cid)
    backend.delete_phone_table(cid)
    backend.delete_contact_table(cid)


        
window=Tk()


window.wm_title("Contact List")

contacts_frame = LabelFrame(window, text=" Contact Details ")
contacts_frame.grid(row=0, column = 0,rowspan=2)

b1=Button(contacts_frame,text="Display all",command=view_command)
b1.grid(row=1,column=0,columnspan = 2)

list1=Listbox(contacts_frame, height=20,width=30)
list1.grid(row=3,column=0,rowspan=9,columnspan=3)

list1.bind('<<ListboxSelect>>',get_selected_row)

l31=Label(contacts_frame,text="First Name")
l31.grid(row=13,column=0)

fname_text=StringVar()
e31=Entry(contacts_frame,textvariable=fname_text)
e31.grid(row=13,column=1)

l32=Label(contacts_frame,text="Middle Name")
l32.grid(row=14,column=0)

mname_text=StringVar()
e32=Entry(contacts_frame,textvariable=mname_text)
e32.grid(row=14,column=1)

l33=Label(contacts_frame,text="Last Name")
l33.grid(row=15,column=0)

lname_text=StringVar()
e33=Entry(contacts_frame,textvariable=lname_text)
e33.grid(row=15,column=1)

a_label = Label(window, text = "   ").grid(row=1,column=3)

address_frame = LabelFrame(window, text=" Address ",height=10,width = 20)
address_frame.grid(row=0, column = 1,columnspan=2)
  
list3=Listbox(address_frame,height=7,width=40)
list3.grid(row=0,column=1,columnspan=4)
      
list3.bind('<<ListboxSelect>>',get_selected_address_row)

l5=Label(address_frame,text="Address Type")
l5.grid(row=5,column=1)

address_type_text=StringVar()
e5=Entry(address_frame,textvariable=address_type_text)
e5.grid(row=5,column=2)

l1=Label(address_frame,text="Address")
l1.grid(row=5,column=3)

address_text=StringVar()
e1=Entry(address_frame,textvariable=address_text)
e1.grid(row=5,column=4)

l2=Label(address_frame,text="City")
l2.grid(row=6,column=1)

city_text=StringVar()
e2=Entry(address_frame,textvariable=city_text)
e2.grid(row=6,column=2)

l3=Label(address_frame,text="State")
l3.grid(row=6,column=3)

state_text=StringVar()
e3=Entry(address_frame,textvariable=state_text)
e3.grid(row=6,column=4)

l4=Label(address_frame,text="Zip")
l4.grid(row=7,column=1)

zip_text=StringVar()
e4=Entry(address_frame,textvariable=zip_text)
e4.grid(row=7,column=2)

baa=Button(address_frame,text="Add New", command=new_address)
baa.grid(row=7,column=3)

bar=Button(address_frame,text="Refresh", command=refresh_address)
bar.grid(row=7,column=4)

phone_frame = LabelFrame(window, text=" Phone ",height=10,width = 20)
phone_frame.grid(row=1, column = 1)

list4=Listbox(phone_frame, height=5,width=30)
list4.grid(row=0,column=0,columnspan=2)

list4.bind('<<ListboxSelect>>',get_selected_phone_row)

l11=Label(phone_frame,text="Number")
l11.grid(row=2,column=0)

number_text=StringVar()
e11=Entry(phone_frame,textvariable=number_text)
e11.grid(row=2,column=1)

l12=Label(phone_frame,text="Number Type")
l12.grid(row=1,column=0)

number_type=StringVar()
e12=Entry(phone_frame,textvariable=number_type)
e12.grid(row=1,column=1)

bpa=Button(phone_frame,text="Add New", command=new_phone)
bpa.grid(row=3,column=0)

bpr=Button(phone_frame,text="Refresh", command=refresh_phone)
bpr.grid(row=3,column=1)


calender_frame = LabelFrame(window, text=" Calendar ",height=10,width = 20)
calender_frame.grid(row=1, column = 2)

list2=Listbox(calender_frame, height=5,width=30)
list2.grid(row=0,column=0,rowspan=2,columnspan=2)

list2.bind('<<ListboxSelect>>',get_selected_date_row)

l21=Label(calender_frame,text="Date Type")
l21.grid(row=2,column=0)

type_text=StringVar()
e21=Entry(calender_frame,textvariable=type_text)
e21.grid(row=2,column=1)

l22=Label(calender_frame,text="Date")
l22.grid(row=3,column=0)

date_text=StringVar()
e22=Entry(calender_frame,textvariable=date_text)
e22.grid(row=3,column=1)

bca=Button(calender_frame,text="Add New", command=new_date)
bca.grid(row=4,column=0)

bcr=Button(calender_frame,text="Refresh", command=refresh_date)
bcr.grid(row=4,column=1)

#a_label = Label(window, text = "   ").grid(row=16,column=3)

methods_frame = LabelFrame(window, text=" Methods ",height=10,width = 20)
methods_frame.grid(row=2, column=1, columnspan = 2)

b4=Button(methods_frame,text="Refresh", command=refresh)
b4.grid(row=0,column=0)

b5=Button(methods_frame,text="Modify", command=update_command)
b5.grid(row=0,column=1)

b6=Button(methods_frame,text="Delete", command=delete_command)
b6.grid(row=0,column=2)

b7=Button(methods_frame,text="Insert", command=insert_command)
b7.grid(row=0,column=3)

search_frame = LabelFrame(window, text=" Search Details ",height=10,width = 20)
search_frame.grid(row=2, column=0)

search_text=StringVar()
search_entry= Entry(search_frame,textvariable=search_text)
search_entry.grid(row = 0,column = 1)

search_btn=Button(search_frame,text="Search", command=search)
search_btn.grid(row=0,column=2)

window.mainloop()