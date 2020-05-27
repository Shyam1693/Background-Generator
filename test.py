import unittest
import main

class TestMain(unittest.TestCase):
	def setUp(self):
		print('About to test function')

	def test_do_stuff(self):
		''' Test 1 passed '''
		test_param = 10
		result = main.do_stuff(test_param)
		self.assertEqual(result, 15)

	def test_do_stuff2(self):
		''' Test 2 passed '''
		test_param = 'shkshks'
		result = main.do_stuff(test_param)
		self.assertEqual(result, ValueError)
	#	self.assertTrue(isinstance(result, ValueError))
	#	self.assertIsInstance(result, ValueError)

	def test_do_stuff3(self):
		''' Test 3 passed '''
		test_param = None
		result = main.do_stuff(test_param)
		self.assertEqual(result, 'Please enter a number')
	#	self.assertTrue(isinstance(result, ValueError))
	#	self.assertIsInstance(result, ValueError)

	def tearDown(self):
		print('Cleaning up')

if __name__ == '__main__':
unittest.main()