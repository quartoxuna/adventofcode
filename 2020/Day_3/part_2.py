#!/usr/bin/env python3

"""
Your puzzle answer was 268.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.

In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?
"""

import copy
import functools

# Read input
terrain = []

with open('input.txt') as file_handle:
    for line in file_handle.readlines():        
        terrain.append([c for c in line if c != '\n'])

def print_terrain(depth):
    for y in range(depth-5, depth+5):
        if y >= 0 and y < len(curr_terrain):
            print("".join([x for x in curr_terrain[y]]))
    print("")

# Set start position
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
tree_hits = []


for slope in slopes:
    pos_x = 0
    pos_y = 0
    trees = 0
    curr_terrain = copy.deepcopy(terrain)
    print_terrain(pos_y)
    while pos_y < len(curr_terrain):
        if curr_terrain[pos_y][pos_x] == '#':
            curr_terrain[pos_y][pos_x] = 'X'
            trees += 1
        else:
            curr_terrain[pos_y][pos_x] = 'O'
    
        # Move right, reset position if out of bounds
        pos_x += slope[0]
        if pos_x >= len(curr_terrain[pos_y]):
                pos_x -= len(curr_terrain[pos_y])
    
        # Move down
        pos_y += slope[1]
        print_terrain(pos_y)

    print("Hit %d trees" % trees)
    tree_hits.append(trees)

print("Hit {} trees: {}".format("*".join([str(h) for h in tree_hits]), functools.reduce(lambda x,y: x*y, tree_hits)))
