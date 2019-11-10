#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 21:55:15 2018

@author: jlopes
"""


def fib_recur(n):
    """ assumes n an int >= 0 """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2)


print()
print(fib_recur(7))
print(fib_recur(35))
# Worst case O(2^n)
