from re import search

__version__ = 0.1
__author__ = 'Surrerstry'


class __Python_2_functions__(object):

	@staticmethod
	def smart_input(message='', repeat_until_success=None, regex=None, tries=0, type_restriction=None, action_when_success=None, action_when_fail=None, action_on_the_end=None, conditioning_call=None):
		"""
		Import:
		from smart_input import smart_input

		List of parameters:

		message = str or repr,
		repeat_until_success = bool,
		regex = str or bytes,
		tries = int,
		type_restriction = type,
		action_when_success = callable,
		action_when_fail = callable,
		action_on_the_end = callable
		conditioning_call = callable

		Some examples of usage:
	
		# works the same like standard function.
		smart_input('')

		# Function will be repeated until passed data become convertible into specified type, maxium 3 times.
		smart_input('', type_restriction=int, tries=3)

		# In this case we specify function to call on each incorrect input
		smart_input('', type_restriction=int, tries=3, action_when_fail=lambda: stdout.write('Please pass integer.\n'))

		# We can define also action on correct input
		smart_input('', type_restriction=int, tries=3, action_when_success=lambda: stdout.write('Great your input is correct\n'))

		# Both actions together
		smart_input('', type_restriction=int, tries=3, action_when_fail=lambda: stdout.write('Please pass integer.\n'), action_when_success=lambda: stdout.write('Great your input is correct\n'))

		# In parameter action_on_the_end we set function that will be called always on the end :)
		smart_input('', type_restriction=int, tries=3, action_on_the_end=lambda: stdout.write("I'm called always on the end\n"))

		# It will be asking forver until input is correct
		smart_input('', repeat_until_success=True, type_restriction=int)

		# It this way we can use regex as condition
		smart_input('', repeat_until_success=True, regex=r"\d")

		# We can mix type_restriction and regex
		smart_input('', repeat_until_success=True, regex=r"\d\.\d", type_restriction=float)
		# Warning: in above case in python input: 1. is expanded to 1.0

		# We can base success or fail on results from our function
		smart_input('', repeat_until_success=True, conditioning_call=lambda: randint(0,1))

		# We can also pass to this function input passed by user
		# For that we have to name one of our parameters as 'user_input'
		smart_input('', repeat_until_success=True, conditioning_call=lambda user_input: 1 if user_input == 'a' else 0)

		# When we have more conditions conditioning_call is called on the end 
		smart_input('', repeat_until_success=True, type_restriction=float, conditioning_call=lambda user_input: 1 if user_input == '1.5' else 0)

		In general you can mix parameters together like you want until it's reasonable.
		For example you cannot mix repeat_until_success and tries...
		
		"""

		if message == '' and repeat_until_success == None and regex == None and tries == 0 and type_restriction == None and action_when_success == None and action_when_fail == None and action_on_the_end == None:
			return input()

		if tries != 0 and regex == None and type_restriction == None:
			raise ValueError("Parameter: 'tries' have to be connected with 'type_restriction' or 'regex'")

		if repeat_until_success != None and tries != 0:
			raise ValueError("You cannot use 'repeat_until_success' and 'tries' together.")

		if repeat_until_success == True and regex == None and type_restriction == None and conditioning_call == None:
			raise ValueError("Parameter: 'repeat_until_success' have to be connected with regex or type_restriction")

		__Python_2_functions__.check_types_smart_input(message=message, repeat_until_success=repeat_until_success, regex=regex, tries=tries, type_restriction=type_restriction, action_when_success=action_when_success, action_when_fail=action_when_fail, action_on_the_end=action_on_the_end, conditioning_call=conditioning_call)

		result = None
		tries_counter = 0 if tries else -1

		while (True and tries_counter < tries) or repeat_until_success:

			try:
				data = input(message)
			except:
				if action_when_fail != None:
					action_when_fail()
				tries_counter += 1
				continue

			result = data
			tries_counter += 1

			if type_restriction != None and regex == None and conditioning_call == None:
				try:
					type_restriction(data)
				except:
					if action_when_fail != None:
						action_when_fail()
					continue
				else:
					result = data
					if action_when_success != None:
						action_when_success()
					break

			if regex != None and type_restriction == None and conditioning_call == None:
				tmp_res = search(regex, data)
				if tmp_res is not None:
					result = data
					if action_when_success != None:
						action_when_success()
					break
				else:
					if action_when_fail != None:
						action_when_fail()
					continue

			if regex != None and type_restriction != None and conditioning_call == None:
				
				cond_reg = False
				cond_type = False
				
				try:
					type_restriction(data)
				except:
					if action_when_fail != None:
						action_when_fail()
					continue
				else:
					cond_type = True

				tmp_res = search(regex, data)
				if tmp_res is not None:
					cond_reg = True
				else:
					if action_when_fail != None:
						action_when_fail()
					continue

				if cond_type and cond_reg:
					result = data
					if action_when_success != None:
						action_when_success()
					break

			if regex != None and type_restriction != None and conditioning_call != None:
				cond_reg = False
				cond_type = False
				cond_call = False
				
				try:
					type_restriction(data)
				except:
					if action_when_fail != None:
						action_when_fail()
					continue
				else:
					cond_type = True

				tmp_res = search(regex, data)
				if tmp_res is not None:
					cond_reg = True
				else:
					if action_when_fail != None:
						action_when_fail()
					continue

				if 'user_input' not in conditioning_call.__code__.co_varnames:
					if conditioning_call():
						cond_call = True
				else:
					if conditioning_call(user_input=result):
						cond_call = True

				if cond_type and cond_reg and cond_call:
					result = data
					if action_when_success != None:
						action_when_success()
					break

			if regex == None and type_restriction != None and conditioning_call != None:
				cond_type = False
				cond_call = False
				
				try:
					type_restriction(data)
				except:
					if action_when_fail != None:
						action_when_fail()
					continue
				else:
					cond_type = True

				if 'user_input' not in conditioning_call.__code__.co_varnames:
					if conditioning_call():
						cond_call = True
				else:
					if conditioning_call(user_input=result):
						cond_call = True

				if cond_type and cond_call:
					result = data
					if action_when_success != None:
						action_when_success()
					break

			if regex != None and type_restriction == None and conditioning_call != None:
				cond_reg = False
				cond_call = False

				tmp_res = search(regex, data)
				if tmp_res is not None:
					cond_reg = True
				else:
					if action_when_fail != None:
						action_when_fail()
					continue

				if 'user_input' not in conditioning_call.__code__.co_varnames:
					if conditioning_call():
						cond_call = True
				else:
					if conditioning_call(user_input=result):
						cond_call = True

				if cond_reg and cond_call:
					result = data
					if action_when_success != None:
						action_when_success()
					break

			if regex == None and type_restriction == None and conditioning_call != None:
				cond_call = False

				if 'user_input' not in conditioning_call.__code__.co_varnames:
					if conditioning_call():
						cond_call = True
				else:
					if conditioning_call(user_input=result):
						cond_call = True

				if cond_call:
					result = data
					if action_when_success != None:
						action_when_success()
					break

		try:
			type_restriction(result)
		except TypeError:
			if type_restriction != None:
				if action_on_the_end != None:
					action_on_the_end()
				return None
		except ValueError:
			if action_on_the_end != None:
				action_on_the_end()
			return None

		if action_on_the_end != None:
			action_on_the_end()

		return result


	@staticmethod
	def check_types_smart_input(message, repeat_until_success, regex, tries, type_restriction, action_when_success, action_when_fail, action_on_the_end, conditioning_call):
		
		if repeat_until_success != None and not isinstance(repeat_until_success, bool):
			raise TypeError("repeat_until_success has to be boolean")

		if regex != None and not isinstance(regex, (str, bytes)):
			raise TypeError("regex has to be str or bytes")

		if tries != None and not isinstance(tries, int):
			raise TypeError("tries has to be an int")

		if action_when_success != None and not callable(action_when_success):
			raise TypeError("action_when_success has to callable")

		if action_when_fail != None and not callable(action_when_fail):
			raise TypeError("action_when_fail has to be callable")

		if action_on_the_end != None and not callable(action_on_the_end):
			raise TypeError("action_on_the_end has to be callable")

		if type_restriction != None and not callable(type_restriction):
			raise TypeError('type_restriction has to be callable')

		if conditioning_call != None and not callable(conditioning_call):
			raise TypeError('conditioning_call has to be callable')


	@staticmethod
	def raw_smart_input(message='', repeat_until_success=None, regex=None, tries=0, type_restriction=None, return_converted=None, action_when_success=None, action_when_fail=None, action_on_the_end=None, conditioning_call=None):
		"""
		Import:
		from smart_input import raw_smart_input

		List of parameters:

		message = str or repr,
		repeat_until_success = bool,
		regex = str or bytes,
		tries = int,
		type_restriction = type,
		return_converted = bool,
		action_when_success = callable,
		action_when_fail = callable,
		action_on_the_end = callable
		conditioning_call = callable

		Some examples of usage:
	
		# works the same like standard function.
		raw_smart_input('')

		# Function will be repeated until passed data become convertible into specified type, maxium 3 times.
		raw_smart_input('', type_restriction=int, tries=3)

		# we will get as result our definied type_restriction
		raw_smart_input('', type_restriction=int, tries=3, return_converted=True)

		# In this case we specify function to call on each incorrect input
		raw_smart_input('', type_restriction=int, tries=3, action_when_fail=lambda: stdout.write('Please pass integer.\n'))

		# We can define also action on correct input
		raw_smart_input('', type_restriction=int, tries=3, action_when_success=lambda: stdout.write('Great your input is correct\n'))

		# Both actions together
		raw_smart_input('', type_restriction=int, tries=3, action_when_fail=lambda: stdout.write('Please pass integer.\n'), action_when_success=lambda: stdout.write('Great your input is correct\n'))

		# In parameter action_on_the_end we set function that will be called always on the end :)
		raw_smart_input('', type_restriction=int, tries=3, action_on_the_end=lambda: stdout.write("I'm called always on the end\n"))

		# It will be asking forver until input is correct
		raw_smart_input('', repeat_until_success=True, type_restriction=int)

		# It this way we can use regex as condition
		raw_smart_input('', repeat_until_success=True, regex=r"\d")

		# We can mix type_restriction and regex
		raw_smart_input('', repeat_until_success=True, regex=r"\d\.\d", type_restriction=float)

		# We can base success or fail on results from our function
		raw_smart_input('', repeat_until_success=True, conditioning_call=lambda: randint(0,1))

		# We can also pass to this function input passed by user
		# For that we have to name one of our parameters as 'user_input'
		raw_smart_input('', repeat_until_success=True, conditioning_call=lambda user_input: 1 if user_input == 'a' else 0)

		# When we have more conditions conditioning_call is called on the end 
		raw_smart_input('', repeat_until_success=True, type_restriction=float, conditioning_call=lambda user_input: 1 if user_input == '1.5' else 0)

		In general you can mix parameters together like you want until it's reasonable.
		For example you cannot mix repeat_until_success and tries...
		
		"""

		if message == '' and repeat_until_success == None and regex == None and tries == 0 and type_restriction == None and return_converted == None and action_when_success == None and action_when_fail == None and action_on_the_end == None:
			return raw_input()

		if tries != 0 and regex == None and type_restriction == None:
			raise ValueError("Parameter: 'tries' have to be connected with 'type_restriction' or 'regex'")

		if repeat_until_success != None and tries != 0:
			raise ValueError("You cannot use 'repeat_until_success' and 'tries' together.")

		if repeat_until_success == True and regex == None and type_restriction == None and conditioning_call == None:
			raise ValueError("Parameter: 'repeat_until_success' have to be connected with regex or type_restriction or conditioning_call")

		__Python_2_functions__.check_types_raw_smart_input(message=message, repeat_until_success=repeat_until_success, regex=regex, tries=tries, type_restriction=type_restriction, return_converted=return_converted, action_when_success=action_when_success, action_when_fail=action_when_fail, action_on_the_end=action_on_the_end, conditioning_call=conditioning_call)

		result = None
		tries_counter = 0 if tries else -1

		while (True and tries_counter < tries) or repeat_until_success:

			data = raw_input(message)
			result = data
			tries_counter += 1

			if type_restriction != None and regex == None and conditioning_call == None:
				try:
					type_restriction(data)
				except:
					if action_when_fail != None:
						action_when_fail()
					continue
				else:
					result = data
					if action_when_success != None:
						action_when_success()
					break

			if regex != None and type_restriction == None and conditioning_call == None:
				tmp_res = search(regex, data)
				if tmp_res is not None:
					result = data
					if action_when_success != None:
						action_when_success()
					break
				else:
					if action_when_fail != None:
						action_when_fail()
					continue

			if regex != None and type_restriction != None and conditioning_call == None:
				
				cond_reg = False
				cond_type = False
				
				try:
					type_restriction(data)
				except:
					if action_when_fail != None:
						action_when_fail()
					continue
				else:
					cond_type = True

				tmp_res = search(regex, data)
				if tmp_res is not None:
					cond_reg = True
				else:
					if action_when_fail != None:
						action_when_fail()
					continue

				if cond_type and cond_reg:
					result = data
					if action_when_success != None:
						action_when_success()
					break

			if regex != None and type_restriction != None and conditioning_call != None:
				cond_reg = False
				cond_type = False
				cond_call = False
				
				try:
					type_restriction(data)
				except:
					if action_when_fail != None:
						action_when_fail()
					continue
				else:
					cond_type = True

				tmp_res = search(regex, data)
				if tmp_res is not None:
					cond_reg = True
				else:
					if action_when_fail != None:
						action_when_fail()
					continue

				if 'user_input' not in conditioning_call.__code__.co_varnames:
					if conditioning_call():
						cond_call = True
				else:
					if conditioning_call(user_input=result):
						cond_call = True

				if cond_type and cond_reg and cond_call:
					result = data
					if action_when_success != None:
						action_when_success()
					break

			if regex == None and type_restriction != None and conditioning_call != None:
				cond_type = False
				cond_call = False
				
				try:
					type_restriction(data)
				except:
					if action_when_fail != None:
						action_when_fail()
					continue
				else:
					cond_type = True

				if 'user_input' not in conditioning_call.__code__.co_varnames:
					if conditioning_call():
						cond_call = True
				else:
					if conditioning_call(user_input=result):
						cond_call = True

				if cond_type and cond_call:
					result = data
					if action_when_success != None:
						action_when_success()
					break

			if regex != None and type_restriction == None and conditioning_call != None:
				cond_reg = False
				cond_call = False

				tmp_res = search(regex, data)
				if tmp_res is not None:
					cond_reg = True
				else:
					if action_when_fail != None:
						action_when_fail()
					continue

				if 'user_input' not in conditioning_call.__code__.co_varnames:
					if conditioning_call():
						cond_call = True
				else:
					if conditioning_call(user_input=result):
						cond_call = True

				if cond_reg and cond_call:
					result = data
					if action_when_success != None:
						action_when_success()
					break

			if regex == None and type_restriction == None and conditioning_call != None:
				cond_call = False

				if 'user_input' not in conditioning_call.__code__.co_varnames:
					if conditioning_call():
						cond_call = True
				else:
					if conditioning_call(user_input=result):
						cond_call = True

				if cond_call:
					result = data
					if action_when_success != None:
						action_when_success()
					break

		try:
			type_restriction(result)
		except TypeError:
			if type_restriction != None:
				if action_on_the_end != None:
					action_on_the_end()
				return None
		except ValueError:
			if action_on_the_end != None:
				action_on_the_end()
			return None

		if return_converted == True and type_restriction == None:
			raise ValueError("return_converted illegal without type_restriction")
		
		if return_converted == True:
			result = type_restriction(result)

		if action_on_the_end != None:
			action_on_the_end()

		return result


	@staticmethod
	def check_types_raw_smart_input(message, repeat_until_success, regex, tries, type_restriction, return_converted, action_when_success, action_when_fail, action_on_the_end, conditioning_call):
		
		if repeat_until_success != None and not isinstance(repeat_until_success, bool):
			raise TypeError("repeat_until_success has to be boolean")

		if regex != None and not isinstance(regex, (str, bytes)):
			raise TypeError("regex has to be str or bytes")

		if tries != None and not isinstance(tries, int):
			raise TypeError("tries has to be an int")

		if return_converted != None and not isinstance(return_converted, bool):
			raise TypeError("return_converted has to be an int")			

		if action_when_success != None and not callable(action_when_success):
			raise TypeError("action_when_success has to callable")

		if action_when_fail != None and not callable(action_when_fail):
			raise TypeError("action_when_fail has to be callable")

		if action_on_the_end != None and not callable(action_on_the_end):
			raise TypeError("action_on_the_end has to be callable")

		if type_restriction != None and not callable(type_restriction):
			raise TypeError('type_restriction has to be callable')

		if conditioning_call != None and not callable(conditioning_call):
			raise TypeError('conditioning_call has to be callable')


class __Python_3_functions__(object):

	@staticmethod
	def smart_input(message='', repeat_until_success=None, regex=None, tries=0, type_restriction=None, return_converted=None, action_when_success=None, action_when_fail=None, action_on_the_end=None, conditioning_call=None):
		"""
		Import:
		from smart_input import smart_input

		List of parameters:

		message = str or repr,
		repeat_until_success = bool,
		regex = str or bytes,
		tries = int,
		type_restriction = type,
		return_converted = bool,
		action_when_success = callable,
		action_when_fail = callable,
		action_on_the_end = callable
		conditioning_call = callable

		Some examples of usage:
	
		# works the same like standard function.
		smart_input('')

		# Function will be repeated until passed data become convertible into specified type, maxium 3 times.
		smart_input('', type_restriction=int, tries=3)

		# we will get as result our definied type_restriction
		smart_input('', type_restriction=int, tries=3, return_converted=True)

		# In this case we specify function to call on each incorrect input
		smart_input('', type_restriction=int, tries=3, action_when_fail=lambda: print('Please pass integer.'))

		# We can define also action on correct input
		smart_input('', type_restriction=int, tries=3, action_when_success=lambda: print('Great your input is correct'))

		# Both actions together
		smart_input('', type_restriction=int, tries=3, action_when_fail=lambda: print('Please pass integer.'), action_when_success=lambda: print('Great your input is correct'))

		# In parameter action_on_the_end we set function that will be called always on the end :)
		smart_input('', type_restriction=int, tries=3, action_on_the_end=lambda: print("I'm called always on the end"))

		# It will be asking forver until input is correct
		smart_input('', repeat_until_success=True, type_restriction=int)

		# It this way we can use regex as condition
		smart_input('', repeat_until_success=True, regex=r"\d")

		# We can mix type_restriction and regex
		smart_input('', repeat_until_success=True, regex=r"\d\.\d", type_restriction=float)
		
		# We can base success or fail on results from our function
		smart_input('', repeat_until_success=True, conditioning_call=lambda: randint(0,1))

		# We can also pass to this function input passed by user
		# For that we have to name one of our parameters as 'user_input'
		smart_input('', repeat_until_success=True, conditioning_call=lambda user_input: 1 if user_input == 'a' else 0)

		# When we have more conditions conditioning_call is called on the end 
		smart_input('', repeat_until_success=True, type_restriction=float, conditioning_call=lambda user_input: 1 if user_input == '1.5' else 0)

		In general you can mix parameters together like you want until it's reasonable.
		For example you cannot mix repeat_until_success and tries...
		
		"""

		if message == '' and repeat_until_success == None and regex == None and tries == 0 and type_restriction == None and return_converted == None and action_when_success == None and action_when_fail == None and action_on_the_end == None:
			return input()

		if tries != 0 and regex == None and type_restriction == None:
			raise ValueError("Parameter: 'tries' have to be connected with 'type_restriction' or 'regex'")

		if repeat_until_success != None and tries != 0:
			raise ValueError("You cannot use 'repeat_until_success' and 'tries' together.")

		if repeat_until_success == True and regex == None and type_restriction == None and conditioning_call == None:
			raise ValueError("Parameter: 'repeat_until_success' have to be connected with regex or type_restriction or conditioning_call")

		__Python_3_functions__.check_types(message=message, repeat_until_success=repeat_until_success, regex=regex, tries=tries, type_restriction=type_restriction, return_converted=return_converted, action_when_success=action_when_success, action_when_fail=action_when_fail, action_on_the_end=action_on_the_end, conditioning_call=conditioning_call)

		result = None
		tries_counter = 0 if tries else -1

		while (True and tries_counter < tries) or repeat_until_success:

			data = input(message)
			result = data
			tries_counter += 1

			if type_restriction != None and regex == None and conditioning_call == None:
				try:
					type_restriction(data)
				except:
					if action_when_fail != None:
						action_when_fail()
					continue
				else:
					result = data
					if action_when_success != None:
						action_when_success()
					break

			if regex != None and type_restriction == None and conditioning_call == None:
				tmp_res = search(regex, data)
				if tmp_res is not None:
					result = data
					if action_when_success != None:
						action_when_success()
					break
				else:
					if action_when_fail != None:
						action_when_fail()
					continue

			if regex != None and type_restriction != None and conditioning_call == None:
				
				cond_reg = False
				cond_type = False
				
				try:
					type_restriction(data)
				except:
					if action_when_fail != None:
						action_when_fail()
					continue
				else:
					cond_type = True

				tmp_res = search(regex, data)
				if tmp_res is not None:
					cond_reg = True
				else:
					if action_when_fail != None:
						action_when_fail()
					continue

				if cond_type and cond_reg:
					result = data
					if action_when_success != None:
						action_when_success()
					break

			if regex != None and type_restriction != None and conditioning_call != None:
				cond_reg = False
				cond_type = False
				cond_call = False
				
				try:
					type_restriction(data)
				except:
					if action_when_fail != None:
						action_when_fail()
					continue
				else:
					cond_type = True

				tmp_res = search(regex, data)
				if tmp_res is not None:
					cond_reg = True
				else:
					if action_when_fail != None:
						action_when_fail()
					continue

				if 'user_input' not in conditioning_call.__code__.co_varnames:
					if conditioning_call():
						cond_call = True
				else:
					if conditioning_call(user_input=result):
						cond_call = True

				if cond_type and cond_reg and cond_call:
					result = data
					if action_when_success != None:
						action_when_success()
					break

			if regex == None and type_restriction != None and conditioning_call != None:
				cond_type = False
				cond_call = False
				
				try:
					type_restriction(data)
				except:
					if action_when_fail != None:
						action_when_fail()
					continue
				else:
					cond_type = True

				if 'user_input' not in conditioning_call.__code__.co_varnames:
					if conditioning_call():
						cond_call = True
				else:
					if conditioning_call(user_input=result):
						cond_call = True

				if cond_type and cond_call:
					result = data
					if action_when_success != None:
						action_when_success()
					break

			if regex != None and type_restriction == None and conditioning_call != None:
				cond_reg = False
				cond_call = False

				tmp_res = search(regex, data)
				if tmp_res is not None:
					cond_reg = True
				else:
					if action_when_fail != None:
						action_when_fail()
					continue

				if 'user_input' not in conditioning_call.__code__.co_varnames:
					if conditioning_call():
						cond_call = True
				else:
					if conditioning_call(user_input=result):
						cond_call = True

				if cond_reg and cond_call:
					result = data
					if action_when_success != None:
						action_when_success()
					break

			if regex == None and type_restriction == None and conditioning_call != None:
				cond_call = False

				if 'user_input' not in conditioning_call.__code__.co_varnames:
					if conditioning_call():
						cond_call = True
				else:
					if conditioning_call(user_input=result):
						cond_call = True

				if cond_call:
					result = data
					if action_when_success != None:
						action_when_success()
					break

		try:
			type_restriction(result)
		except TypeError:
			if type_restriction != None:
				if action_on_the_end != None:
					action_on_the_end()
				return None
		except ValueError:
			if action_on_the_end != None:
				action_on_the_end()
			return None

		if return_converted == True and type_restriction == None:
			raise ValueError("return_converted illegal without type_restriction")
		
		if return_converted == True:
			result = type_restriction(result)

		if action_on_the_end != None:
			action_on_the_end()

		return result


	@staticmethod
	def check_types(message, repeat_until_success, regex, tries, type_restriction, return_converted, action_when_success, action_when_fail, action_on_the_end, conditioning_call):
		
		if repeat_until_success != None and not isinstance(repeat_until_success, bool):
			raise TypeError("repeat_until_success has to be boolean")

		if regex != None and not isinstance(regex, (str, bytes)):
			raise TypeError("regex has to be str or bytes")

		if tries != None and not isinstance(tries, int):
			raise TypeError("tries has to be an int")

		if return_converted != None and not isinstance(return_converted, bool):
			raise TypeError("return_converted has to be an int")			

		if action_when_success != None and not callable(action_when_success):
			raise TypeError("action_when_success has to callable")

		if action_when_fail != None and not callable(action_when_fail):
			raise TypeError("action_when_fail has to be callable")

		if action_on_the_end != None and not callable(action_on_the_end):
			raise TypeError("action_on_the_end has to be callable")

		if type_restriction != None and not callable(type_restriction):
			raise TypeError('type_restriction has to be callable')

		if conditioning_call != None and not callable(conditioning_call):
			raise TypeError('conditioning_call has to be callable')
