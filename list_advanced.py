#!/usr/bin/env python

grid = [ None ] * 3
grid[0] = [ 1 ]
grid[0].extend([2])
grid[1] = [ 3 ]
grid[1].extend([4])
print grid

assert 3 == len(grid)
assert 2 == len(grid[0])
assert 1 == len(grid[2])
