from model.key import Key


def add_new():

	from model.model import clear_cli
	from views.menu import main_menu

	print(' ************************')
	print(' *       ADD KEY        *')
	print(' ************************')
	category = input(' Category: ').upper()
	while True:
		service = input(' Service name: ').upper()
		if service == '':
			print(' [!!!] REQUIRED FIELD [!!!]')
		else:
			break

	while True:
		username = input(' User name: ')
		if username == '':
			print(' [!!!] REQUIRED FIELD [!!!]' )
		else:
			break

	while True:
		password = input(' Password: ')
		if password == '':
			print(' [!!!] REQUIRED FIELD [!!!]')
		else:
			break

	annotations = input(' Annotations: ')

	if annotations == '':
		annotations = 'EMPTY'
	if category == '':
		category = 'EMPTY'

	print('\n ************************')
	print(f' CATEGORY:[{category}]')
	print(f' SERVICE:[{service}]')
	print(f' USERNAME:[{username}]')
	print(f' PASSWORD:[{password}]')
	print(f' ANNOTATIONS:[{annotations}]')
	print(' ************************')
	
	while True:		
		save = input('\n INCLUDE KEY? [Y/N]:').upper()
		if save not in 'YN':
					print ('\nINVALID OPTION')	
		elif save == 'Y':
			key_temp = Key('NULL',category,service,username,password,annotations)
			key_temp.insert_key()
			clear_cli()
			print('    ******************')
			print('    * SAVING SUCCESS *')
			print('    ******************')			
			print()
			main_menu()
		elif save == 'N':
			clear_cli()
			print('    *****************')
			print('    * CANCEL SAVING *')
			print('    *****************')			
			print()
			main_menu()