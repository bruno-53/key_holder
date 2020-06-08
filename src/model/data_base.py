import sqlite3
from model.key import Key

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


# LIST ALL KEYS IN HOLDER DATABASE
def pick_key(chose_id,op):
	import re
	global connection
	global c
	flag = False
	c.execute(f'''SELECT category FROM holder WHERE id = '{chose_id}';''')
	for row in c.fetchall():
		row = str(row)
		row = re.sub(r'[\',)(]','',row)
		category = row
		flag = True
	c.execute(f'''SELECT serviceName FROM holder WHERE id = '{chose_id}';''')
	for row in c.fetchall():
		row = str(row)
		row = re.sub(r'[\',)(]','',row)
		service = row
	c.execute(f'''SELECT userName FROM holder WHERE id = '{chose_id}';''')
	for row in c.fetchall():
		row = str(row)
		row = re.sub(r'[\',)(]','',row)
		username = row
	c.execute(f'''SELECT password FROM holder WHERE id = '{chose_id}';''')
	for row in c.fetchall():
		row = str(row)
		row = re.sub(r'[\',)(]','',row)
		password = row
	c.execute(f'''SELECT annotations FROM holder WHERE id = '{chose_id}';''')
	for row in c.fetchall():
		row = str(row)
		row = re.sub(r'[\',)(]','',row)
		annotations = row
	if flag == True:
		key_temp = Key(chose_id,category,service,username,password,annotations)
		#SHOW KEY
		if op == 0:
			key_temp.show_key()
			while True:		
				copy = input(' COPY PASSWORD FOR TRANSFER AREA? [Y/N]:').upper()
				if copy not in 'YN':
							print (' INVALID OPTION')	
				elif copy == 'Y':
					key_temp.copy_password()
					print(' ******************************')
					print(' *  PASSWORD IN TRANSFER AREA *')
					print(' *   PRESS  CTRL+V TO PASTE   *')
					print(' ******************************')
					break
				else:
					print(' ***************************')
					break
		#EDIT KEY
		if op == 1:
			key_temp.show_key()
			while True:	
				print(' *******************************')
				print(' * PRESS ENTER FOR NOT CHANGES *')
				print(' ******************************')
				new_category = input(' NEW CATEGORY: ').upper()
				new_service = input(' NEW SERVICE NAME: ').upper()
				new_username = input(' NEW USER NAME: ')
				new_password = input(' NEW PASSWORD: ')
				new_annotations = input(' NEW ANNOTATION: ')
				if new_category == '':
					new_category = category
				if new_service == '':
					new_service = service
				if new_username == '':
					new_username = username
				if new_password == '':
					new_password = password
				if new_annotations == '':
					new_annotations = annotations
				key_temp = Key(chose_id,new_category,new_service,new_username,new_password,new_annotations)
				key_temp.show_key()
				copy = input(' SAVE CHANGES? [Y/N]:').upper()
				if copy not in 'YN':
							print (' INVALID OPTION')	
				elif copy == 'Y':
					key_temp.edit_key(chose_id)
					print(' ******************************')
					print(' *       CHANGES SAVED        *')
					print(' ******************************')
					break
				else:
					print(' ******************************')
					print(' *     CHANGES NOT SAVED      *')
					print(' ******************************')
					break
		#DELETE KEY
		if op == 2:
			key_temp.show_key()
			while True:	
				copy = input(' DELETE KEY? [Y/N]:').upper()
				if copy not in 'YN':
							print (' INVALID OPTION')	
				elif copy == 'Y':
					key_temp.delete_key(chose_id)
					print(' ******************************')
					print(f' *         KEY ERASE         *')
					print(' ******************************')
					break
				else:
					print(' ******************************')
					break
	else:
		print(' **************************')
		print(' [!!!] INVALID KEY ID [!!!]')
		print(' **************************')
		print()