from model.data_base import insert_key

def add_new():
	from model.model import clear_cli
	from views.menu import main_menu
	print('-__ADD MENU__-')
	category = input('\nCategory: ').upper()
	while True:
		service = input('\nService name: ').upper()
		if service == '':
			print('\nRequired field, please try again')
			print()
		else:
			break

	while True:
		username = input('\nUser name: ')
		if username == '':
			print('\nRequired field, please try again')
			print()
		else:
			break

	while True:
		password = input('\nPassword: ')
		if password == '':
			print('\nRequired field, please try again')
			print()
		else:
			break

	annotations = input('\nAnnotations: ')

	if annotations == '':
		annotations = "EMPTY"
	if category == '':
		category = "NOT CATEGORIZED"
		
	print(f'\nCATEGORY: [{category}]\nSERVICE: [{service}]\
	\nUSERNAME: [{username}]\nPASSWORD: [{password}]\nANNOTATIONS: [{annotations}]')
	
	while True:		
		save = input('\nInclude changes? [Y/N]:').upper()
		if save not in 'YN':
					print ('\nINVALID OPTION')	
		elif save == 'Y':
			insert_key(category,service,username,password,annotations)
			print('\n\n***__-SAVING SUCCESS-__***\n\n')
			clear_cli()
			main_menu()
		elif save == 'N':
			print('\n\n***__-CANCEL SAVING-__***\n\n')
			main_menu()