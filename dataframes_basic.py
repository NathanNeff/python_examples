#!/usr/local/bin/python3
import unittest
import pandas as pd

class TestDFs(unittest.TestCase):
    """
    Basic DF
    """
 
    def test_series(self):
        """
	Test number one
        """
        obj = pd.Series([4, 7, -5, 3])
        self.assertEqual(4,4)

if __name__ == '__main__':
    unittest.main()
