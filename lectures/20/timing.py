# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 21:35:11 2018

@author: jlopes

Time and compare pop() with pop(0).
The list get's bigger by 10^6 each cicle and there's 10^3 executions for 
each measurement for more accuracy.
"""

import timeit

# popping from the end
popend = timeit.Timer("x.pop()",                 # Python statement to time
                      "from __main__ import x")  # runs once to setup

# popping from the beginning 
popzero = timeit.Timer("x.pop(0)",
                       "from __main__ import x")

# header
print("\n{:>9s} {:>9s} {:>10s}".format("len(x)", "pop()", "pop(0)"))

# get those values in miliseconds (10^⁻3)
for i in range(1000000, 100000001, 1000000):

    x = list(range(i))  # the list get's bigger
    pe = popend.timeit(number=1000)   # timeit for 1000 pops

    x = list(range(i))  # the list get's bigger
    pz = popzero.timeit(number=1000)  # timeit for 1000 pops

    # ptint the results
    print("{:9d} {:9.5f} {:10.5f}".format(i, pe, pz))

print("The Winter is coming!")
