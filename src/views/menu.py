def main_menu():
	option = 0
	select = "[1] --- Check Password \n[2] --- Add Password \n"
	
	while option != 2:
		print (select)
		option=input('Select your option: ')
		int(option)
	print()

	return None
