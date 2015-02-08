import unittest
import re

class ListTest(unittest.TestCase):

    def testDate(self):
        ""
        self.assertEqual("2015.02.07", "2015.02.07")


    def testDate2(self):
        ""
        self.assertEqual("2015.02.07", "2015.02.07")

    def test_inserts_and_appends(self):
        another_list = [None] * 5
        another_list[0] = "Zero"
        another_list[4] = "Four"
        self.assertEquals(another_list, [ "Zero", None , None, None, "Four" ])

    def test_plus(self):
        # Plus operator on lists (it ain't extend or append)
        first_list = [ "a", "b" ]
        second_list = [ "c", "d" ]
        self.assertEquals([ "a", "b", "c", "d" ] , first_list + second_list)

    def test_extend(self):
        extend_example = [ 1, 2 ]
        extend_example.extend([ 3, 4 ])
        self.assertEquals( [ 1, 2, 3, 4 ] , extend_example)

    def test_append_nested(self):
        append_example = [ 1, 2 ]
        append_example.append([ 3, 4 ])
        self.assertEquals([ 1, 2, [ 3, 4 ] ], append_example)

    def test_slice(self):
        lst = [ 1, 2, 3 ]
        self.assertEquals([ 2, 3 ] , lst[1:])

    def test_len(self):
        self.assertEquals(3, len([1,2,3]))

    def test_join(self):
        greeting_words = ["Hello", "world", "jamaica", "Mon"]
        self.assertEquals("Hello-world-jamaica-Mon",'-'.join(greeting_words))

    def test_sort(self):
        unsorted_list = [ 1, 100, 2, "A", "z", "a", '2', '22', "Z", 200, -1, '100', '-1', '1', '10']
        self.assertEquals([-1, 1, 2, 100, 200,
             '-1',
             '1',
             '10',
             '100',
             '2',
             '22',
             'A', 'Z',
             'a', 'z'] , sorted(unsorted_list))

if __name__ == "__main__":
    main()
