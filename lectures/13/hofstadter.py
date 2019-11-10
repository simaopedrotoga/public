#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 19:09:14 2018

@author: Shantanu Sharma

Python program to implement Hofstader Sequence using mutual recursion

https://www.geeksforgeeks.org/mutual-recursion-example-hofstadter-female-male-sequences/
"""

# Female function
def hofstaderFemale(n):
    if n < 0:
        return
    else:
        val = 1 if n == 0 else (n - hofstaderFemale(n - 1))
        return val

# Male function
def hofstaderMale(n):
    if n < 0:
        return
    else:
        val = 0 if n == 0 else (n - hofstaderMale(n - 1))
        return val

# Driver code
print()
print("F:", end = " ")
for i in range(0, 20):
    print(hofstaderFemale(i), end = " ")
print()
print("M:", end = " ")
for i in range(0, 20):
    print(hofstaderMale(i), end = " ")
print()
