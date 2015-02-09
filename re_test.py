#!/usr/bin/env python
import unittest
import re

class SomeTester(unittest.TestCase):
    def test_something(self):
        pgn = "1. e4 e5 2. Nf3 Nf6"

        self.assertIsNotNone(re.search("1.", pgn))
        self.assertIsNotNone(re.search("\s+2.", pgn))

if __name__ == "__main__":
    unittest.main()
