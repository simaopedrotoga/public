import turtle

wn = turtle.Screen()
wn.bgcolor("green")

cyril = turtle.Turtle()
cyril.pensize(5)       # just to notice better
cyril.shape("turtle")
cyril.color("blue")

cyril.stamp()

for _ in range(12):
    cyril.up()
    cyril.forward(80)  # line offset relative to center
    cyril.down()
    cyril.forward(10)  # line length
    cyril.up()
    cyril.forward(15)  # stamp offset relative to center
    cyril.stamp()
    cyril.backward(105)  # almost all the way back (5 units offset to center clock on turtle center, otherwise will center on upper left corner)
    cyril.left(30)

wn.mainloop()
turtle.bye()
