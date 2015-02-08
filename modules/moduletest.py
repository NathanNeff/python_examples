import unittest
import natemod

class Something(unittest.TestCase):
    def testSomething(self):
        self.assertEqual("Foo",natemod.natefunc("Foo"))

if __name__ == "__main__":
    unittest.main()
