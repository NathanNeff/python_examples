#!/usr/bin/env python
import unittest
import re

class SomeTester(unittest.TestCase):
    def test_something(self):
        pgn = "1. e4 e5 2. Nf3 Nf6"

        self.assertIsNotNone(re.search("1.", pgn))
        self.assertIsNotNone(re.search("\s+2.", pgn))

    def test_another(self):
        self.assertIsNotNone(re.search(".png", "foo.PNG", flags=re.IGNORECASE),
                                      "Should be case-insensitive")
        self.assertIsNone(re.search(".png$", "foo.PNG.txt", flags=re.IGNORECASE), 
                                    "Should be case-insensitive")
        self.assertIsNotNone(re.search(".png$", "foo.png.txtpng", flags=re.IGNORECASE), 
                ".png should have period and be last")
        self.assertIsNone(re.search("\.png$", "foo.png.txtpng", flags=re.IGNORECASE), 
                ".png should have period and be last")
        self.assertIsNone(re.search("\.png$", "foopng", flags=re.IGNORECASE), 
                ".png should have period and be last")

if __name__ == "__main__":
    unittest.main()
