from model.data_base import list_all
from controller.controller import add_new

# MAIN MENU OPITIONS AND CONDITIONS
def main_menu():
	from model.model import clear_cli
	option_list = [1,2,3,4,0]
	print(' ************************')
	print(' *      MAIN MENU       *')
	print(' *                      *')
	print(' *  [1] --- ADD KEY     *')
	print(' *  [2] --- EDIT KEY    *')
	print(' *  [3] --- CHECK KEY   *')
	print(' *  [4] --- REMOVE KEY  *')
	print(' *  [0] --- EXIT        *')
	print(' *                      *')
	print(' ************************')


	while True:
		try:
			option = int(input(' SELECT OPTION: '))
			if option not in option_list:
				print ('\n INVALID OPTION, train again')
				#ADD OPITION
			elif option == 1:
				clear_cli()
				add_new()
				#CHECK OPTION
			elif option == 3:
				clear_cli()
				check_pass()
			elif option == 0:
				clear_cli()
				exit()
		except ValueError:
			print('\n Please insert ONLY NUMBERS')


def check_pass():
	from model.model import clear_cli
	select = (''' -__CHECK MENU__-
	\n[1] --- LIST ALL
	\n[2] --- LIST CATEGORY
	\n[3] --- SEARCH for Service
	\n[4] --- BACK ''')

	option_list = [1,2,3,4,5,0]
	print(' **************************')
	print(' *      CHECK MENU        *')
	print(' *                        *')
	print(' *  [1] --- LIST ALL      *')
	print(' *  [2] --- FIND SERVICE  *')
	print(' *  [3] --- FIND CATEGORY *')
	print(' *  [4] --- FIND ID       *')
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
				check_pass()
			elif option == 3:
				clear_cli()
			elif option == 4:
				clear_cli()
				main_menu()
			elif option == 0:
				clear_cli()
				exit()
		except ValueError:
			print(' Please insert ONLY NUMBERS')