#!/usr/bin/env python
import unittest

class SomeTest(unittest.TestCase):
    def test_basic(self):
        words = {}
        self.assertFalse('foo' in words)
        self.assertNotIn('foo', words)

        words['foo'] = 1
        self.assertIn('foo', words)
        self.assertNotIn('FOO', words)

        sumz = 0
        for k in words.keys():
            sumz += words[k]

        words['bar'] = 2
        self.assertEquals(2, len(words.keys()))

if __name__ == '__main__':
    unittest.main()

