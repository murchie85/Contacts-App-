import sqlite3
import random
import string
from tkinter import	 *
import tkinter as tk

'''
Please write a small web application that models an address book. Your solution should present a simple user--interface
and should persist the data, so that it is available after restarting any processes.
Your address book should list organisations and people. It should allow the user to see the names and contact details of
people in organisations, and to manage the people who are in an organisation. It should store a name and contact details for
each organisation.
Your address book should allow organisations and people to be created, edited and deleted.
The address book is for use by a single person;; there is no need to build authentication and authorization in your submission.



name
organisation
TEL
EMAIL
MOBILE
'''

#define DB connection
conn = sqlite3.connect('contactsdb.db')
c = conn.cursor()


#define the table, ensure it creates only once 
def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS allContacts(name TEXT, org TEXT, tel TEXT, email TEXT, mob TEXT)')

# prototype function will be redundant
def input_test():
	c.execute("INSERT INTO allContacts VALUES('Adam McMurchie', 'Administrate', '01382 625789', 'murchie85@gmail.com', '07832141785' )")
	conn.commit()
	c.close()
	conn.close()

# allows for inserting based upon parameratization 
def dynamic_data_entry(name='Adam', org='Administrate', tel='01382765412', email='adam@hotmail.com', mob='0778965432'):
	c.execute("INSERT INTO allContacts (name, org, tel, email, mob) VALUES (?, ?, ?, ?, ?)",
	(name, org, tel, email, mob)) # note for going to server MYSQL will use %s instead of ?
	conn.commit() # no need to close after commit, especially if doing multiple inserts



#Read data from our contacts 
def read_from_db():
	c.execute('SELECT * FROM allContacts')
	global data
	data = c.fetchall()

	# should become redundant 
def update():
	c.execute('SELECT * FROM allContacts')
	[print(row) for row in c.fetchall()]

	c.execute("UPDATE allContacts SET name = 'John' WHERE name = 'Adam' ")
	conn.commit()
	print(50 * '#')

	c.execute('SELECT * FROM allContacts')
	[print(row) for row in c.fetchall()]

	# should become redundant 
def delete():
	c.execute('SELECT * FROM allContacts')
	[print(row) for row in c.fetchall()]

	c.execute('DELETE FROM allContacts WHERE tel = 2') # LIMIT exists for sql
	conn.commit()
	print(50 * '#')

	c.execute('SELECT * FROM allContacts')
	[print(row) for row in c.fetchall()]





# event handler 
def contactselect(event):
	if contactList.curselection():
		selectedcontact = contactList.get(contactList.curselection())
		print(selectedcontact)














#basic window 
root = Tk()   # blank window
root.title("Contact List")
root.geometry("800x600+450+150")
# A Label and a Listbox
headerlabel = Label(root, text="All Contacts")

headerlabel.place(relx=0.01, rely=0.01, relheight=0.03, relwidth=0.64)
# Now the listbox
contactList = Listbox(root)

# Bind an event <<>> is tkinter stuff, param2 the def Name
contactList.bind("<<ListboxSelect>>", contactselect)


contactList.place(relx=0.01, rely=0.04, relheight=0.98, relwidth=0.64)



create_table()
dynamic_data_entry()
dynamic_data_entry('Mr DaTa', 'S74RF1337', '622-1701-(3)', 'lt.cmdr.data@enterprise.starfleet.alpha.mil.wa', '07010101101')
read_from_db()

for i in range (len(data)):
	contactList.insert(END, data[i])


root.mainloop() #need to have this window continuously running 