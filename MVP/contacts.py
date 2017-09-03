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


#*************************************DATABASE ********************************************


#define DB connection
conn = sqlite3.connect('contactsdb.db')
c = conn.cursor()


#define the table, ensure it creates only once 
def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS allContacts(name TEXT, org TEXT, tel TEXT, email TEXT, mob TEXT)')

# prototype function will be redundant
def input_test():
	c.execute("INSERT INTO allContacts VALUES('Jack Oneill', 'SG1', '01382 625789', 'JONEILL@gmail.com', '07832141785' )")
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


#END**********************************************************************************#







#*****************************USER INTERFACE FUNCTIONS *********************************#

# event handler 
def contactselect(event):
	if contactList.curselection():
		selectedcontact = contactList.get(contactList.curselection())
		print(selectedcontact)

def addcontact():
	global addname, addorg, addtel, addemail, addmob
	print("Adding " + addname.get() + " to Contact List")
	dynamic_data_entry(addname.get(), addorg.get(), addtel.get(), addemail.get(), addmob.get())
	# Clear vars and consequently textboxes as they are linked.
	addname.set("")
	addorg.set("")
	addtel.set("")
	addemail.set("")
	addmob.set("")
	refreshlist()


# Delete single record (Button command doesn't need event)
def deletesingle():
	if contactList.curselection():
		contactitems = contactList.get(contactList.curselection())
		name = contactitems[0]
		org = contactitems[1]
		tel = contactitems[2]
		email = contactitems[3]
		mob = contactitems[4]
		c.execute('DELETE FROM allContacts WHERE name=\'' + name + '\' AND tel=\'' + tel + '\'')
		print('Deleted Contact: ' + name + ' from: ' + org + ' email: ' + email + ' tel: ' + tel + ' mob: ' + mob)
		conn.commit()
		refreshlist()
	else:
		print("No Contact Selected!")


def deleteorg():
	if contactList.curselection():
		contactitems = contactList.get(contactList.curselection())
		name = contactitems[0]
		org = contactitems[1]
		tel = contactitems[2]
		email = contactitems[3]
		mob = contactitems[4]
		c.execute('DELETE FROM allContacts WHERE org=\'' + org + '\'')
		print('Deleted All Contacts from: ' + org)
		conn.commit()
		refreshlist()
	else:
		print("No Contact Selected!")


def refreshlist():
	read_from_db()
	contactList.delete(0, END)
	for i in range(len(data)):
		contactList.insert(END, data[i])

#END**********************************************************************************#



#*****************************TKINTER AND GUI STUFF *********************************#




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


# A Label frame to group the add contact form.
addcontactframe = LabelFrame(root, text="Add Contact")
addcontactframe.place(relx=0.66, rely=0.01, relheight=0.25, relwidth=0.33)
lblname = Label(addcontactframe, text="Name: ")
lblname.place(relx=0.01, rely=0.01, relwidth=0.35, relheight=0.15)
lblorg = Label(addcontactframe, text="Organisation: ")
lblorg.place(relx=0.01, rely=0.15, relwidth=0.35, relheight=0.15)
lbltel = Label(addcontactframe, text="Tel: ")
lbltel.place(relx=0.01, rely=0.30, relwidth=0.35, relheight=0.15)
lblemail = Label(addcontactframe, text="eMail: ")
lblemail.place(relx=0.01, rely=0.45, relwidth=0.35, relheight=0.15)
lblmob = Label(addcontactframe, text="Mobile: ")
lblmob.place(relx=0.01, rely=0.60, relwidth=0.35, relheight=0.15)


# Pre assign stringVars for our Entry boxes
addname = tk.StringVar()
addorg = tk.StringVar()
addtel = tk.StringVar()
addemail = tk.StringVar()
addmob = tk.StringVar()
inputname = Entry(addcontactframe, textvariable=addname)
inputname.place(relx=0.36, rely=0.01, relwidth=0.60, relheight=0.15)
inputorg = Entry(addcontactframe, textvariable=addorg)
inputorg.place(relx=0.36, rely=0.15, relwidth=0.60, relheight=0.15)
inputtel = Entry(addcontactframe, textvariable=addtel)
inputtel.place(relx=0.36, rely=0.30, relwidth=0.60, relheight=0.15)
inputemail = Entry(addcontactframe, textvariable=addemail)
inputemail.place(relx=0.36, rely=0.45, relwidth=0.60, relheight=0.15)
inputmob = Entry(addcontactframe, textvariable=addmob)
inputmob.place(relx=0.36, rely=0.60, relwidth=0.60, relheight=0.15)
addcontactbutton = Button(addcontactframe, text="Add Contact", command=addcontact)
addcontactbutton.place(relx=0.01, rely=0.76, height=24, width=250)



# Labelframe for delete buttons
deletelabelframe = LabelFrame(root, text="Delete Entries")
deletelabelframe.place(relx=0.66, rely=0.26, relheight=0.70, relwidth=0.33)
deletebutton = Button(deletelabelframe, text="Delete Contact", command=deletesingle)
deletebutton.place(relx=0.01, rely=0.01, height=24, width=250)
deleteorgbutton = Button(deletelabelframe, text="Delete Organisation", command=deleteorg)
deleteorgbutton.place(relx=0.01, rely=0.10, height=24, width=250)


#END**********************************************************************************#










#*************************************RUNTIME STUFF *****************************#


create_table()
#populate a couple of rows, dynamically and with default
dynamic_data_entry()
dynamic_data_entry('DaTa', 'S74RF1337', '622-1701-(3)', 'lt.cmdr.data@enterprise.starfleet.alpha.mil.wa', '07010101101')
read_from_db()


#tidying up 
def on_closing():
	c.close()
	conn.close()
	root.destroy()


for i in range (len(data)):
	contactList.insert(END, data[i])

# This line gives the form an on_close event.
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop() #need to have this window continuously running 