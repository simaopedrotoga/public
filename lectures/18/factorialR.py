#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 09:36:12 2018

@author: jlopes
"""

def factorialR(N):
    "Recursive factorial function"
    assert isinstance(N, int) and N >= 1
    return 1 if N <= 1 else N * factorialR(N-1)

print()
print(factorialR(5))
print(factorialR(0))
print(factorialR('a'))
