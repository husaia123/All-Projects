from turtle import *
import random
speed (0)
shape ("turtle")
color ("red")

x = random.randint (1,250)
print (x)

backward (150)
forward (300)
for i in range (x):
    left (120)
    forward (300)
    left (120)
    forward (350)
    left (1)
