#!/bin/env python

def main():
    test_inserts_and_appends()
    test_basic()
    test_sort()

def test_inserts_and_appends():
    another_list = [None] * 5
    another_list[0] = "Zero"
    another_list[4] = "Four"
    assert another_list == [ "Zero", None , None, None, "Four" ]

    # Plus operator on lists (it ain't extend or append)
    first_list = [ "a", "b" ]
    second_list = [ "c", "d" ]
    assert [ "a", "b", "c", "d" ] == first_list + second_list

    extend_example = [ 1, 2 ]
    extend_example.extend([ 3, 4 ])
    assert [ 1, 2, 3, 4 ] == extend_example

    append_example = [ 1, 2 ]
    append_example.append([ 3, 4 ])
    assert [ 1, 2, [ 3, 4 ] ] == append_example

def test_basic():
    lst = [ 1, 2, 3 ]
    assert [ 2, 3 ] == lst[1:]
    assert 3 == len(lst) 

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
