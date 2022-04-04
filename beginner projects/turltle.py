from turtle import*
from random import randint  
penup ()
speed(0)
goto (-280,140)
for i in range (28):
    write (i, align='center')
    right (90)
    forward (10)
    pendown ()
    forward (150)
    penup ()
    backward (160)
    left (90)
    forward (20)

red = Turtle ()
red.color("red")
red.shape ("turtle")
red.penup()
red.goto (-300,100)
red.pendown()

blue = Turtle ()
blue.color("blue")
blue.shape ("turtle")
blue.penup()
blue.goto (-300,70)
blue.pendown()

green = Turtle ()
green.color("green")
green.shape ("turtle")
green.penup()
green.goto (-300,40)
green.pendown()

orange = Turtle ()
orange.color("orange")
orange.shape ("turtle")
orange.penup()
orange.goto (-300,10)
orange.pendown()

for turn in range (100):
    red.forward (randint (1,10))
    blue.forward (randint (1,10))
    green.forward (randint (1,10))
    orange.forward (randint (1,10))

    


