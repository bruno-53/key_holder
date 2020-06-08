import sqlite3
from tkinter import Tk

connection = sqlite3.connect('key_holder.db')
c = connection.cursor()

# CREATE OBJECT KEY
class Key:

	# KEY FEATURES
	def __init__(self,id,category,service,username,password,annotations):
		self.id = id
		self.category = category
		self.service = service
		self.username = username
		self.password = password
		self.annotations = annotations


	# INSERT DATA IN TABLE HOLDER
	def insert_key(self):
		global connection
		global c
		c.execute(f'''
		INSERT INTO holder (id,category,serviceName,userName,password,annotations)
		VALUES (NULL,'{self.category}','{self.service}','{self.username}','{self.password}','{self.annotations}')
		''')
		connection.commit()
	
	def show_key(self):
		print('\n ************************')
		print(f' CATEGORY:[{self.category}]')
		print(f' SERVICE:[{self.service}]')
		print(f' USERNAME:[{self.username}]')
		print(f' PASSWORD:[{self.password}]')
		print(f' ANNOTATIONS:[{self.annotations}]')
		print(' ************************')

	def copy_password(self):
		r = Tk()
		r.withdraw()
		r.clipboard_clear()
		r.clipboard_append(f'{self.password}')
		r.update()

	def edit_key(self,chose_id):
		global connection
		global c
		c.execute(f'''
		UPDATE holder
		SET category = '{self.category}',serviceName = '{self.service}',userName = '{self.username}',password = '{self.password}',annotations = '{self.annotations}'
		WHERE id = '{chose_id}'
		''')
		connection.commit()

	def delete_key(self,chose_id):
		global connection
		global c
		c.execute(f'''
		DELETE FROM holder
		WHERE id = '{chose_id}'
		''')
		connection.commit()