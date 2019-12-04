# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 21:35:11 2018

@author: jlopes

Compare pop() with pop(0) in a list.

The list gets bigger by 10^6 each cicle and there's 10^3 executions for
each measurement for more accuracy.
"""

import timeit

# print the header
print("\n{:>9s} {:>9s} {:>10s}".format("len(x)", "pop()", "pop(0)"))

# get those values in miliseconds (10^⁻3)
for size in range(10**6, 12*10**6+1, 10**6):

    # pop()
    pe_init = "x.pop()"                                 # the list gets bigger
    pe_step = "x = list(range(" + str(size) + "))"        # the operation
    pe = timeit.timeit(pe_init, pe_step, number=10**3)  # timeit for 1000 pops

    # pop(0)
    pz_init = "x.pop(0)"                                # the list gets bigger
    pz_step = "x = list(range(" + str(size) + "))"        # the operation
    pz = timeit.timeit(pz_init, pz_step, number=10**3)  # timeit for 1000 pops

    # print the results
    print("{:9d} {:9.5f} {:10.5f}".format(size, pe, pz))

print("The Winter is coming!")
