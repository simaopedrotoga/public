"""
Created on Fri Dec  7 15:18:46 2018

@author: jlopes
"""

def filter(oldfile, newfile):
    with open(oldfile, "r") as infile, open(newfile, "w") as outfile:
        for line in infile:
            # Put any processing logic here
            if not line.startswith('#'):
                outfile.write(line)

filter("filter.py", "filter.pyx")

print("\nDone.")
