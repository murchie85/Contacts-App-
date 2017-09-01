import sqlite3
import random
import string

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
# for populating random name
def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))
# make a random tel number
def random_tel(y):
	for x in range(y):
		num = num + random.randrange(0,9)
		return num

# allows for inserting based upon parameratization 
def dynamic_data_entry():
	value = random.randrange(0,15)
	name = random_char(value)
	org = random_char(value)
	tel = random_tel(value)
	email = random_char(value) + '@' + random_char(value) + '.com'
	mob = random_tel(value)
	c.execute("INSERT INTO allContacts (name, org, tel, email, mob) VALUES (?, ?, ?, ?, ?)",
	(name, org, tel, email, mob)) #MYSQL will use %s instead of ?
	conn.commit() # no need to close after commit, especially if doing multiple inserts



create_table()
#input_test()

# add 10 rows randomised 
for i in range(10):
	dynamic_data_entry()

c.close()
conn.close()