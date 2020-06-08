from model.data_base import list_all
from controller.controller import add_new,chose_for,chose_key,make_password

# MAIN MENU OPITIONS AND CONDITIONS
def main_menu():
	from model.model import clear_cli
	option_list = [1,2,3,4,5,0]
	print(' ************************')
	print(' *      MAIN MENU       *')
	print(' *                      *')
	print(' *  [1] --- ADD KEY     *')
	print(' *  [2] --- EDIT KEY    *')
	print(' *  [3] --- CHECK KEY   *')
	print(' *  [4] --- REMOVE KEY  *')
	print(' *  [5] --- MAKE PASS   *')
	print(' *  [0] --- EXIT        *')
	print(' *                      *')
	print(' ************************')


	while True:
		try:
			option = int(input(' SELECT OPTION: '))
			if option not in option_list:
				print ('\n INVALID OPTION, train again')
			elif option == 1:
				clear_cli()
				add_new('')
			elif option == 2:
				clear_cli()
				edit_menu()
			elif option == 3:
				clear_cli()
				check_menu()
			elif option == 4:
				list_all()
				chose_key(2)
				main_menu()
			elif option == 5:
				clear_cli()
				make_password()
			elif option == 0:
				clear_cli()
				exit()
		except ValueError:
			print('\n Please insert ONLY NUMBERS')

# EDIT MENU AND OPITIONS
def edit_menu():
	from model.model import clear_cli

	option_list = [1,2,3,0]
	print(' **************************')
	print(' *       EDIT MENU        *')
	print(' *                        *')
	print(' *  [1] --- LIST ALL      *')
	print(' *  [2] --- EDIT KEY(ID)  *')
	print(' *  [3] --- BACK          *')
	print(' *  [0] --- EXIT          *')
	print(' *                        *')
	print(' **************************')

	while True:
		try:
			option = int(input(' SELECT OPTION: '))
			if option not in option_list:
				print ('\n INVALID OPTION train again')
			elif option == 1:
				clear_cli()
				list_all()
				edit_menu()
			elif option == 2:
				chose_key(1)
				edit_menu()
			elif option == 3:
				clear_cli()
				main_menu()
			elif option == 0:
				clear_cli()
				exit()
		except ValueError:
			print(' Please insert ONLY NUMBERS')

# CHECK MENU AND OPITIONS
def check_menu():
	from model.model import clear_cli

	option_list = [1,2,3,4,5,0]
	print(' **************************')
	print(' *      CHECK MENU        *')
	print(' *                        *')
	print(' *  [1] --- LIST ALL      *')
	print(' *  [2] --- LIST SERVICE  *')
	print(' *  [3] --- LIST CATEGORY *')
	print(' *  [4] --- PICK KEY(ID)  *')
	print(' *  [5] --- BACK          *')
	print(' *  [0] --- EXIT          *')
	print(' *                        *')
	print(' **************************')

	while True:
		try:
			option = int(input(' SELECT OPTION: '))
			if option not in option_list:
				print ('\n INVALID OPTION train again')
			elif option == 1:
				clear_cli()
				list_all()
				check_menu()
			elif option == 2:
				chose_for(1)
				check_menu()
			elif option == 3:
				chose_for(2)
				check_menu()
			elif option == 4:
				chose_key(0)
				check_menu()
			elif option == 5:
				clear_cli()
				main_menu()
			elif option == 0:
				clear_cli()
				exit()
		except ValueError:
			print(' Please insert ONLY NUMBERS')


