import unittest

from sys import version_info
from sys import stdout
from random import randint

if version_info.major == 2:
	try:
		from mock import patch
		import __builtin__
	except ImportError:
		exit("To run unittest on Python2 please install mock library.")
else:
	from unittest.mock import patch

from smart_input import __Python_2_functions__
smart_input2 = __Python_2_functions__.smart_input
raw_smart_input2 = __Python_2_functions__.raw_smart_input

from smart_input import __Python_3_functions__
smart_input3 = __Python_3_functions__.smart_input

"""
Python3
smart_input.smart_input()

Python2
smart_input.smart_input()
smart_input.raw_smart_input()
"""

class TestsSmartInput_Python2(unittest.TestCase if version_info.major == 2 else object):

	########## INPUT ##########
	@patch('__builtin__.input', return_value='')
	def test_smart_input2(self, input):
		self.assertEqual(smart_input2(), '')

	@patch('__builtin__.input', return_value='123')
	def test_smart_input2_parameter_tries(self, input):
		self.assertEqual(smart_input2('', type_restriction=int, tries=3), '123')

	@patch('__builtin__.input', return_value='123')
	def test_smart_input2_parameter_action_when_fail(self, input):
		self.assertEqual(smart_input2('', type_restriction=int, tries=3, action_when_fail=lambda: stdout.write('Please pass integer.\n')), '123')

	@patch('__builtin__.input', return_value='123')
	def test_smart_input2_parameter_action_when_success(self, input):
		self.assertEqual(smart_input2('', type_restriction=int, tries=3, action_when_success=lambda: stdout.write('Great your input is correct\n')), '123')

	@patch('__builtin__.input', return_value='123')
	def test_smart_input2_parameter_action_when_fail_and_action_when_success(self, input):
		self.assertEqual(smart_input2('', type_restriction=int, tries=3, action_when_fail=lambda: stdout.write('Please pass integer.\n'), action_when_success=lambda: stdout.write('Great your input is correct\n')), '123')

	@patch('__builtin__.input', return_value='123')
	def test_smart_input2_parameter_action_on_the_end(self, input):
		self.assertEqual(smart_input2('', type_restriction=int, tries=3, action_on_the_end=lambda: stdout.write("I'm called always on the end\n")), '123')

	@patch('__builtin__.input', return_value='123')
	def test_smart_input2_parameter_repeat_until_success(self, input):
		self.assertEqual(smart_input2('', repeat_until_success=True, type_restriction=int), '123')

	@patch('__builtin__.input', return_value='1.123')
	def test_smart_input2_parameter_regex(self, input):
		self.assertEqual(smart_input2('', repeat_until_success=True, regex=r"\d"), '1.123')

	@patch('__builtin__.input', return_value='1.1')
	def test_smart_input2_parameter_regex_and_type_restriction(self, input):
		self.assertEqual(smart_input2('', repeat_until_success=True, regex=r"\d\.\d", type_restriction=float), '1.1')

	@patch('__builtin__.input', return_value='a')
	def test_smart_input2_parameter_conditioning_call(self, input):
		self.assertEqual(smart_input2('', repeat_until_success=True, conditioning_call=lambda: randint(0,1)), 'a')

	@patch('__builtin__.input', return_value='a')
	def test_smart_input2_parameter_conditioning_call_with_parameter_user_input(self, input):
		self.assertEqual(smart_input2('', repeat_until_success=True, conditioning_call=lambda user_input: 1 if user_input == 'a' else 0), 'a')

	@patch('__builtin__.input', return_value='1.5')
	def test_smart_input2_parameter_conditioning_call_with_parameter_user_input_and_type_restriction(self, input):
		self.assertEqual(smart_input2('', repeat_until_success=True, type_restriction=float, conditioning_call=lambda user_input: 1 if user_input == '1.5' else 0), '1.5')


	########## RAW_INPUT ##########
	@patch('__builtin__.raw_input', return_value='1')
	def test_raw_smart_input(self, raw_input):
		self.assertEqual(raw_smart_input2(), '1')

	@patch('__builtin__.raw_input', return_value='123')
	def test_raw_smart_input_parameter_tries(self, raw_input):
		self.assertEqual(raw_smart_input2('', type_restriction=int, tries=3), '123')

	@patch('__builtin__.raw_input', return_value='123')
	def test_raw_smart_input_parameter_return_converted(self, raw_input):
		self.assertEqual(raw_smart_input2('', type_restriction=int, tries=3, return_converted=True), 123)

	@patch('__builtin__.raw_input', return_value='123')
	def test_raw_smart_input_parameter_action_when_fail(self, raw_input):
		self.assertEqual(raw_smart_input2('', type_restriction=int, tries=3, action_when_fail=lambda: stdout.write('Please pass integer.\n')), '123')

	@patch('__builtin__.raw_input', return_value='123')
	def test_raw_smart_input_parameter_action_when_success(self, raw_input):
		self.assertEqual(raw_smart_input2('', type_restriction=int, tries=3, action_when_success=lambda: stdout.write('Great your input is correct\n')), '123')

	@patch('__builtin__.raw_input', return_value='123')
	def test_raw_smart_input_parameter_action_when_fail_and_action_when_success(self, raw_input):
		self.assertEqual(raw_smart_input2('', type_restriction=int, tries=3, action_when_fail=lambda: stdout.write('Please pass integer.\n'), action_when_success=lambda: stdout.write('Great your input is correct\n')), '123')

	@patch('__builtin__.raw_input', return_value='123')
	def test_raw_smart_input_parameter_action_on_the_end(self, raw_input):
		self.assertEqual(raw_smart_input2('', type_restriction=int, tries=3, action_on_the_end=lambda: stdout.write("I'm called always on the end\n")), '123')

	@patch('__builtin__.raw_input', return_value='123')
	def test_raw_smart_input_parameter_repeat_until_success(self, raw_input):
		self.assertEqual(raw_smart_input2('', repeat_until_success=True, type_restriction=int), '123')

	@patch('__builtin__.raw_input', return_value='1.123')
	def test_raw_smart_input_parameter_regex(self, raw_input):
		self.assertEqual(raw_smart_input2('', repeat_until_success=True, regex=r"\d"), '1.123')

	@patch('__builtin__.raw_input', return_value='1.1')
	def test_raw_smart_input_parameter_regex_and_type_restriction(self, raw_input):
		self.assertEqual(raw_smart_input2('', repeat_until_success=True, regex=r"\d\.\d", type_restriction=float), '1.1')

	@patch('__builtin__.raw_input', return_value='a')
	def test_raw_smart_input_parameter_conditioning_call(self, raw_input):
		self.assertEqual(raw_smart_input2('', repeat_until_success=True, conditioning_call=lambda: randint(0,1)), 'a')

	@patch('__builtin__.raw_input', return_value='a')
	def test_raw_smart_input_parameter_conditioning_call_with_parameter_user_input(self, raw_input):
		self.assertEqual(raw_smart_input2('', repeat_until_success=True, conditioning_call=lambda user_input: 1 if user_input == 'a' else 0), 'a')

	@patch('__builtin__.raw_input', return_value='1.5')
	def test_raw_smart_input_parameter_conditioning_call_with_parameter_user_input_and_type_restriction(self, raw_input):
		self.assertEqual(raw_smart_input2('', repeat_until_success=True, type_restriction=float, conditioning_call=lambda user_input: 1 if user_input == '1.5' else 0), '1.5')


class TestsSmartInput_Python3(unittest.TestCase if version_info.major == 3 else object):

	# if no special parameters -> call standard function
	@patch('builtins.input', return_value='')
	def test_smart_input3(self, input):
		self.assertEqual(smart_input3(), '')

	@patch('builtins.input', return_value='123')
	def test_smart_input3_parameter_tries(self, input):
		self.assertEqual(smart_input3('', type_restriction=int, tries=3), '123')

	@patch('builtins.input', return_value='123')
	def test_smart_input3_parameter_return_converted(self, input):
		self.assertEqual(smart_input3('', type_restriction=int, tries=3, return_converted=True), 123)

	@patch('builtins.input', return_value='123')
	def test_smart_input3_parameter_action_when_fail(self, input):
		self.assertEqual(smart_input3('', type_restriction=int, tries=3, action_when_fail=lambda: stdout.write('Please pass integer.\n')), '123')

	@patch('builtins.input', return_value='123')
	def test_smart_input3_parameter_action_when_success(self, input):
		self.assertEqual(smart_input3('', type_restriction=int, tries=3, action_when_success=lambda: stdout.write('Great your input is correct\n')), '123')

	@patch('builtins.input', return_value='123')
	def test_smart_input3_parameter_action_when_fail_and_action_when_success(self, input):
		self.assertEqual(smart_input3('', type_restriction=int, tries=3, action_when_fail=lambda: stdout.write('Please pass integer.\n'), action_when_success=lambda: stdout.write('Great your input is correct\n')), '123')

	@patch('builtins.input', return_value='123')
	def test_smart_input3_parameter_action_on_the_end(self, input):
		self.assertEqual(smart_input3('', type_restriction=int, tries=3, action_on_the_end=lambda: stdout.write("I'm called always on the end\n")), '123')

	@patch('builtins.input', return_value='123')
	def test_smart_input3_parameter_repeat_until_success(self, input):
		self.assertEqual(smart_input3('', repeat_until_success=True, type_restriction=int), '123')

	@patch('builtins.input', return_value='1.123')
	def test_smart_input3_parameter_regex(self, input):
		self.assertEqual(smart_input3('', repeat_until_success=True, regex=r"\d"), '1.123')

	@patch('builtins.input', return_value='1.1')
	def test_smart_input3_parameter_regex_and_type_restriction(self, input):
		self.assertEqual(smart_input3('', repeat_until_success=True, regex=r"\d\.\d", type_restriction=float), '1.1')

	@patch('builtins.input', return_value='a')
	def test_smart_input3_parameter_conditioning_call(self, input):
		self.assertEqual(smart_input3('', repeat_until_success=True, conditioning_call=lambda: randint(0,1)), 'a')

	@patch('builtins.input', return_value='a')
	def test_smart_input3_parameter_conditioning_call_with_parameter_user_input(self, input):
		self.assertEqual(smart_input3('', repeat_until_success=True, conditioning_call=lambda user_input: 1 if user_input == 'a' else 0), 'a')

	@patch('builtins.input', return_value='1.5')
	def test_smart_input3_parameter_conditioning_call_with_parameter_user_input_and_type_restriction(self, input):
		self.assertEqual(smart_input3('', repeat_until_success=True, type_restriction=float, conditioning_call=lambda user_input: 1 if user_input == '1.5' else 0), '1.5')


if __name__ == '__main__':
	unittest.main()
