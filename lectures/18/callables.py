#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:41:47 2018

@author: jlopes

David Mertz, Functional Programming in Python
"""

def hello1(name):
    print("Hello", name)

hello2 = lambda name: print("Hello", name)

print()
hello1('John')
hello2('John')

hello3 = hello2   # can bind func to other names
hello3('John')

print()
print(hello3.__qualname__)
print(hello2.__qualname__)
print(hello1.__qualname__)
