import os
from .data_base import insert_key

# MAIN MENU OPITIONS AND CONDITIONS
def main_menu():
	select = (""" -__MAIN MENU__-
	\n[1] --- ADD Password
	\n[2] --- EDIT Password
	\n[3] --- CHECK Password
	\n[4] --- REMOVE Password
	\n[5] --- EXIT """)

	option_list = [1,2,3,4,5]
	print (select)
		
	print()

	while True:
		try:
			option = int(input('\nSelect option: '))
			if option not in option_list:
				print ('\nINVALID OPTION train again')
				#ADD OPITION
			elif option == 1:
				os.system('cls' if os.name == 'nt' else 'clear')
				add_new()
			elif option == 5:
				exit()
		except ValueError:
			print("\nPlease insert ONLY NUMBERS")

def add_new():
	print('-__ADD MENU__-')
	category = input('\nCategory: ').upper()
	service = input('\nService name: ').upper()
	username = input('\nUser name: ')
	password = input('\nPassword: ')
	annotations = input('\nAnnotations: ')
	print(f'\nCATEGORY: [{category}]\nSERVICE: [{service}]\
	\nUSERNAME: [{username}]\nPASSWORD: [{password}]\nANNOTATIONS: [{annotations}]')
	
	while True:		
		save = input('\nInclude changes? [Y/N]:').upper()
		if save not in 'YN':
					print ('\nINVALID OPTION')	
		elif save == 'Y':
			insert_key(category,service,username,password,annotations)
			print('\n\n***__-SAVING SUCCESS-__***\n\n')
			main_menu()
		elif save == 'N':
			print('\n\n***__-CANCEL SAVING-__***\n\n')
			main_menu()
