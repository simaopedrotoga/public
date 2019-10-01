#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 16:37:53 2019

@author: jlopes
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 16:31:08 2018
@author: jlopes
Code adapted from the book:
Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers, 
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

############
# A example with 2 turtles
############

import turtle

window = turtle.Screen()   # Set up the window and its attributes
window.bgcolor("lightgreen")
window.title("Tess & Alex")

tess = turtle.Turtle()     # Create tess and set some attributes
tess.color("Pink")
tess.pensize(5)

alex = turtle.Turtle()     # Create alex and set some attributes
alex.color("Navy")

tess.forward(160)          # Make tess draw equilateral triangle
tess.left(120)
tess.forward(160)
tess.left(120)
tess.forward(160)
tess.left(120)             # Complete the triangle

tess.right(180)            # Turn tess around
tess.forward(160)          # Move her away from the origin

alex.forward(100)          # Make alex draw a square
alex.left(90)
alex.forward(100)
alex.left(90)
alex.forward(100)
alex.left(90)
alex.forward(100)
alex.left(90)

window.mainloop()
turtle.bye()
