
def do_stuff(num):
	try:
		return num + 5
	except ValueError as err:
		return err