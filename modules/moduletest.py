import unittest
import natemod

class Something(unittest.TestCase):
    def testSomething(self):
        "This is the description of this function?"
        self.assertEqual("Foo",natemod.natefunc("Foo"))

if __name__ == "__main__":
    unittest.main()
