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



# LIST ALL KEYS IN HOLDER DATABASE
def list_all():
	import re
	print(' ID    CATEGORY  SERVICE')
	print('----   --------  -------')
	global connection
	global c
	c.execute('''SELECT id,'--',category,'--',serviceName FROM holder;''')
	for row in c.fetchall():
		row = str(row)
		row = re.sub(r'[\'*,)(]','',row)
		print(f' {row}')
	print()


# LIST FILTER BY SERVICE OR CATEGORY
def list_chose(chose_temp,op):
	import re
	global connection
	global c

	if op == 1:
		print(' ID    SERVICE  ')
		print('----   -------- ')
		c.execute(f'''SELECT id,'--',serviceName FROM holder WHERE serviceName = '{chose_temp}';''')
		for row in c.fetchall():
			row = str(row)
			row = re.sub(r'[\',)(]','',row)
			print(f' {row}')
		print()

	if op == 2:
		print(' ID    CATEGORY  ')
		print('----   -------- ')
		c.execute(f'''SELECT id,'--',category FROM holder WHERE category = '{chose_temp}';''')
		for row in c.fetchall():
			row = str(row)
			row = re.sub(r'[\',)(]','',row)
			print(f' {row}')
		print()

