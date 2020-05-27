import os
from getpass import getpass
from views.menu import main_menu

def clear_cli():
	os.system('cls' if os.name == 'nt' else 'clear')

def first_autentication():

	master_key = '123'

	# GETTING KEY IN HIDDEN MODE
	key = getpass(prompt='Insert your master key: ')


	# MASTER KEY VALIDATION
	if key != master_key:
		print ('\n!!Wrong key!!\n')
		exit()

	else:
		clear_cli()
		main_menu()