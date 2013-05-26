#!/bin/env python

def main():
    test_inserts()
    test_basic()
    test_sort()

def test_inserts():
    another_list = [None] * 5
    another_list[0] = "Zero"
    another_list[4] = "Four"
    assert another_list == [ "Zero", None , None, None, "Four" ]

def test_basic():
    lst = [ 1, 2, 3 ]
    assert [ 2, 3 ] == lst[1:]

    greeting_words = ["Hello", "world", "jamaica", "Mon"]
    assert "Hello-world-jamaica-Mon" == '-'.join(greeting_words)

def test_sort():
    unsorted_list = [ 1, 100, 2, "A", "z", "a", '2', '22', "Z", 200, -1, '100', '-1', '1', '10']
    assert [-1, 1, 2, 100, 200,
         '-1',
         '1',
         '10',
         '100',
         '2',
         '22',
         'A', 'Z',
         'a', 'z'] == sorted(unsorted_list)


if __name__ == '__main__':
    main()
