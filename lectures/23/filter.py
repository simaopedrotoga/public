#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 15:18:46 2018

@author: jlopes
"""

# define filter function
def filter(oldfile, newfile):
    with open(oldfile, "r") as infile, open(newfile, "w") as outfile:
        for line in infile:
            
            # Put any processing logic here
            if not line.startswith('#'):  # removes comment lines
                outfile.write(line)

# process file
filter("filter.py", "files/filter.txt")

print("\nDone.")
