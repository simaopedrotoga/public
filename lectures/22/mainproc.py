# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 19:43:50 2018

@author: jlopes
"""

import turtle


def drawSquare(t, sz):
    """
    Make turtle t draw a square of with side sz.
    """
    for i in range(4):
        t.forward(sz)
        t.left(90)

### without main()
#wn = turtle.Screen()          # Set up the window and its attributes
#wn.bgcolor("lightgreen")
#
#alex = turtle.Turtle()        # create alex
#drawSquare(alex, 50)          # Call the function to draw the square
#
#wn.exitonclick()
#turtle.bye()

### with main()
#def main():                     # Define the main function
#    wn = turtle.Screen()        # Set up the window and its attributes
#    wn.bgcolor("lightgreen")
#
#    alex = turtle.Turtle()      # create alex
#    drawSquare(alex, 50)        # Call the function to draw the square
#
#    wn.exitonclick()
#    turtle.bye()
#
#main()                          # Invoke the main function
