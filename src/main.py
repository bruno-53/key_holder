import os
from getpass import getpass
from views.menu import main_menu

print("********************\n")
print("-key holder v 0.0.1-\n")
print("********************")

master_key = '123'

key = getpass(prompt='Insert your master key: ')


if key != master_key:
	print ('\n!!Wrong key!!\n')
	exit()

else:
	os.system('clear')
	main_menu()
