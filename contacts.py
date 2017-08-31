import sqlite3
import random

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


def input_test():
	c.execute("INSERT INTO allContacts VALUES('Adam McMurchie', 'Administrate', '01382 625789', 'murchie85@gmail.com', '07832141785' )")
	conn.commit()
	c.close()
	conn.close()


create_table()
input_test()