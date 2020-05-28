import sqlite3

connection = sqlite3.connect('key_holder.db')
c = connection.cursor()

# CREATE TABLE HOLDER
def create_table():
	global connection
	global c
	c.execute('''
	CREATE TABLE IF NOT EXISTS holder(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		category TEXT NOT NULL,
		serviceName TEXT NOT NULL,
		userName TEXT NOT NULL,
		password TEXT NOT NULL,
		annotations TEXT NOT NULL
	);
	''')



def list_all():
	print(' ID    CATEGORY  SERVICE')
	print('----   --------  -------')
	global connection
	global c
	c.execute('''SELECT id,category,serviceName FROM holder;''')
	for row in c.fetchall():
		print(row)
	print()
	