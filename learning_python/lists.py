L = [ 123, 'spam', 1.23 ]
assert 3 == len(L), "Huh?"
assert 123 == L[0]
assert 1.23 == L[-1]
# : ranges 
assert [ 123, 'spam' ] == L[:2]

# comprehension
M = [
        [ 1, 2, 3],
        [ 4, 5, 6],
        [ 7, 8, 9]
]

assert [ 1, 2, 3 ] == M[0] 
assert 5 == M[1][1]

# List comprehension
assert [ 2, 5, 8 ] == [ blerk[1] for blerk in M ]
# Get diagonals
assert [ 1, 5, 9 ] == [ M[i][i] for i in [ 0, 1, 2 ] ]
