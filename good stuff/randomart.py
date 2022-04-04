from turtle import *
import random 
speed (0)
screensize(-300,300)


shape ("turtle")
def randomcolor ():
   color (random.sample (("red","green","blue","orange","purple","brown","black"), 1)[0])
def randomplace ():
   goto ((random.randint (-300,300)),(random.randint (-300,300)))

for i in range (25): #random turtles
    randomcolor ()
    pu ()
    setheading (random.randint (1,360))
    randomplace ()
    n = i % 1
    turtlesize (random.randint (1,5))
    if n == 0:
        pd ()
        stamp ()
   
clear ()
setheading (0)

for i in range (25): #random rectangles
   pu()
   randomcolor ()
   randomplace ()
   hideturtle ()
   length = (random.randint (10,100))
   height = (random.randint (10,100))
   begin_fill ()
   for i in range (2):
      fd (length)
      rt (90)
      fd (height)
      rt (90)
   end_fill ()
clear ()

for i in range (25): #random circles
   randomcolor ()
   goto ((random.randint (-200,200)),(random.randint (-200,200)))
   pd ()
   begin_fill ()
   circle (random.randint (10,100))
   end_fill ()
   pu()
clear()

for i in range (25): #random stars
   randomcolor ()
   pu()
   randomplace ()
   pd ()
   begin_fill ()
   x = (random.randint (10,200))
   for i in range (5):
      left (144)
      forward (x)
   end_fill ()
clear ()
   
   



    
    

    
        
