import sqlite3

connection = sqlite3.connect('key_holder.db')
c = connection.cursor()

# CREATE TABLE HOLDER
def create_table():
	global connection
	global c
	c.execute('''
	CREATE TABLE IF NOT EXISTS holder(
		category TEXT NOT NULL,
		serviceName TEXT NOT NULL,
		userName TEXT NOT NULL,
		password TEXT NOT NULL,
		annotations TEXT NOT NULL
	);
	''')

# INSERT DATA IN TABLE HOLDER
def insert_key(category,service,username,password,annotations):
	global connection
	global c
	c.execute(f'''
	INSERT INTO holder (category,serviceName,userName,password,annotations)
	VALUES ('{category}','{service}','{username}','{password}','{annotations}')
	''')
	connection.commit()


def list_all():
	print('(CATEGORY --- SERVICE)')
	print()
	global connection
	global c
	c.execute('''SELECT category, " --- ",serviceName FROM holder;''')
	for service in c.fetchall():
		print(service)
	print()
	