import unittest

class IQTest(unittest.TestCase):
    def test_odd_one_out(self):
        self.assertEqual(3, iq_test("2 4 7 8 10"))
