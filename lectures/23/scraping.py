#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 15:31:53 2018

@author: jlopes
"""

import urllib.request

url = "https://www.ietf.org/rfc/rfc793.txt"
destination_filename = "rfc793.txt"

# using module urllib
urllib.request.urlretrieve(url, destination_filename)

print("\nWritten in", destination_filename)

# now with requests
import requests

response = requests.get(url)

#print()
#print(response.text)

# we may as well do
#for line in response:
#    print(line)
