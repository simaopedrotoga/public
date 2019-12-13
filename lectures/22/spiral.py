#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 17:34:01 2019

@author: jlopes
"""

# Don't do this at home!
def h2(t, size):
    """ Draw the next step of a spiral on each call. """
    # global size      # FIXME
    t.stamp()        # Leave an impression on the canva
    size += 3        # Increase the size on every iteration
    t.right(24)      # Move tess along
    t.forward(size)  # ... and turn her


import turtle

# have a turtle
ww = turtle.Screen()
ww.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

# setup
tess.penup()
size = 20            # Initial size

# draw it!
for _ in range(30):
    # h2(tess)         # Draw the next step
    h2(tess, size)
    size += 3        # Increase the size on every iteration

# close down
ww.mainloop()
turtle.bye()
