from sys import version_info, stderr

if version_info.major == 3:
	
	# imports
	from smart_input.smart_input import __Python_3_functions__
	
	# shortening
	smart_input = __Python_3_functions__.smart_input

elif version_info.major == 2:

	# imports
	from smart_input import __Python_2_functions__

	# shortening
	smart_input = __Python_2_functions__.smart_input
	raw_smart_input = __Python_2_functions__.raw_smart_input

else:
	stderr("Error: Unknown version of Python...")
	exit(1)