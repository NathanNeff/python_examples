#!/usr/local/bin/python3
import unittest
import pandas as pd
import numpy as np

class TestDFs(unittest.TestCase):
    """
    Basic DF
    """
 
    def test_simple_series(self):
        """
        Explore single time-series DataFrames
        """
        df = pd.Series([4, 7, -5, 3])
        np.testing.assert_array_equal([ 4, 7, -5, 3], df.values)

        self.assertEqual(4, df[0])

        df2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
        self.assertEqual(4, df2['d'])

        dfgte7 = df2[df2 >= 7]
        np.testing.assert_array_equal([ 7 ], dfgte7.values)

        # Apply operation to entire DF
        dfTimesTwo = df2 * 2
        self.assertEqual(8, dfTimesTwo['d'])
       
        return df

if __name__ == '__main__':
    unittest.main()
