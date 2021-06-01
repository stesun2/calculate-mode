# Write your own unit tests here!
import unittest
from calculate_mode import calculate_mode

class CalculateModeTestCase(unittest.TestCase):
    """Test for calculate_mode.py"""

    def test_returns_empty_list(self):
        """Calls calculate_mode.py, returns an empty list"""
        self.assertEqual(len(calculate_mode()), 0)
    
    def test_returns_length_list(self):
        """Calls calculate_mode.py, returns the length of array """
        self.assertEqual(len(calculate_mode([1,2,3,4])), 4)

    def test_returns_mode_list(self):
        """Calls calculate_mode.py, returns list mode"""
        self.assertEqual(type(calculate_mode([1,2,3,4,4,4])), [3])

    def test_returns_non_int_list(self):
        """Calls calculate_mode.py, returns non-int mode"""
        self.assertEqual(type(calculate_mode(['dog','cat','dogs','cat','cat'])), ['cat'])

    def test_returns_equal_mod_list(self):
        """Calls calculate_mode.py, returns list of equal frequency"""
        self.assertEqual(type(calculate_mode([1,2,3,4])), [1,2,3,4])


if __name__ == '__main__':
    unittest.main()
    
    