import unittest

def iq_test(string_of_numbers):
    numbers = [int(x) for x in string_of_numbers.split()]
    odd_position = numbers.index(7) + 1    
    return odd_position

class IQTest(unittest.TestCase):
    def test_odd_one_out(self):
        self.assertEqual(3, iq_test("2 4 7 8 10"))
