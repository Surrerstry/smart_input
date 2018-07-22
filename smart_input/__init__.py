from sys import version_info, stderr

if version_info.major == 3:
	
	# imports
	from smart_input.smart_input import __Python_3_functions__
	
	# shortening
	smart_input = __Python_3_functions__.smart_input
	menu = __Python_3_functions__.menu

elif version_info.major == 2:

	# imports
	from smart_input import __Python_2_functions__

	# shortening
	smart_input = __Python_2_functions__.smart_input
	raw_smart_input = __Python_2_functions__.raw_smart_input
	menu = __Python_2_functions__.menu

else:
	stderr("Error: Unknown version of Python...")
	exit(1)