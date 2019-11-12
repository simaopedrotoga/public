#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 16:26:44 2018

@author: jlopes

Recursive Python function to solve tower of Hanoi

Adapted from:
    https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/
"""

def move_tower(height, from_pole, to_pole, with_pole):
    if height >= 1:
        # move n-1 disks from source to auxiliary, so they are out of the wa
        move_tower(height-1, from_pole, with_pole, to_pole)
        # move the nth disk from source to target
        moveDisk(height, from_pole, to_pole)
        # move the n-1 disks that we left on auxiliary onto target
        move_tower(height-1, with_pole, to_pole, from_pole)

# Display our progress
def moveDisk(n, fp, tp):
    print("moving disk", n, "from", fp, "to", tp)

print()
# initiate call from source A to target C with auxiliary B
move_tower(4, "A", "C", "B")
