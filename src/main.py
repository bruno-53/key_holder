import os
from getpass import getpass
from views.menu import main_menu
from views.data_base import create_table

create_table()

print("********************\n")
print("-KEY HOLDER v 0.0.1-\n")
print("********************")

master_key = '123'

# GETTING KEY IN HIDDEN MODE
key = getpass(prompt='Insert your master key: ')


# MASTER KEY VALIDATION
if key != master_key:
	print ('\n!!Wrong key!!\n')
	exit()

else:
	os.system('cls' if os.name == 'nt' else 'clear')
	main_menu()
