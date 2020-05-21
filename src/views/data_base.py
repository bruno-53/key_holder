import sqlite3

connection = sqlite3.connect('key_holder.db')
c = connection.cursor()

# CREATE TABLE HOLDER
def create_table():
	global connection
	global c
	c.execute('''
	CREATE TABLE IF NOT EXISTS holder(
		serviceName TEXT NOT NULL,
		userName TEXT NOT NULL,
		password TEXT NOT NULL
	);
	''')

# INSERT DATA IN TABLE HOLDER
def insert_key(service,username,password):
	global connection
	global c
	c.execute(f'''
	INSERT INTO holder (serviceName,userName,password)
	VALUES ('{service}','{username}','{password}')
	''')
	connection.commit()