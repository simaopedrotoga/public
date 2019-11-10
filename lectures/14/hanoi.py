#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 16:26:44 2018

@author: jlopes

Recursive Python function to solve tower of Hanoi

Adapted from:
    https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/
"""

def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        # move n-1 disks from source to auxiliary, so they are out of the wa
        moveTower(height-1, fromPole, withPole, toPole)
        # move the nth disk from source to target
        moveDisk(height, fromPole, toPole)
        # move the n-1 disks that we left on auxiliary onto target
        moveTower(height-1, withPole, toPole, fromPole)

# Display our progress
def moveDisk(n, fp, tp):
    print("moving disk", n, "from", fp, "to", tp)

print()
# initiate call from source A to target C with auxiliary B
moveTower(4, "A", "C", "B")
