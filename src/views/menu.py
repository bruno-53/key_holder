from model.data_base import list_all
from controller.controller import add_new

# MAIN MENU OPITIONS AND CONDITIONS
def main_menu():
	from model.model import clear_cli
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
				clear_cli()
				add_new()
				#CHECK OPTION
			elif option == 3:
				clear_cli()
				check_pass()
			elif option == 5:
				exit()
		except ValueError:
			print("\nPlease insert ONLY NUMBERS")


def check_pass():
	from model.model import clear_cli
	select = (""" -__CHECK MENU__-
	\n[1] --- LIST ALL
	\n[2] --- LIST CATEGORY
	\n[3] --- SEARCH for Service
	\n[4] --- BACK """)

	option_list = [1,2,3,4]
	print (select)
		
	print()

	while True:
		try:
			option = int(input('\nSelect option: '))
			if option not in option_list:
				print ('\nINVALID OPTION train again')
			elif option == 1:
				clear_cli()
				list_all()
				check_pass()
			elif option == 3:
				clear_cli()
			elif option == 4:
				clear_cli()
				main_menu()
		except ValueError:
			print("\nPlease insert ONLY NUMBERS")