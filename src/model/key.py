import sqlite3

connection = sqlite3.connect('key_holder.db')
c = connection.cursor()

class Key:

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
