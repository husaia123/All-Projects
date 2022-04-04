from turtle import*
import random
import math
points = 0
choices = ["rotated 90 to the left","rotated 90 to the right","mirrored on the xaxis","mirrored on the yaxis"]
while True:
    color("black")
    x = []
    y = []
    m = 0
    available_answer = True

    for i in range (5):
        x.append (random.randint (-250,250))#random location
        y.append (random.randint (-250,250))

    for i in x:#drawing the original shape 
        if m == 0:
            pu()
        goto (i,(y[m]))
        pd()
        m += 1

    m = 0 
    color("red")
    move = choices [(random.randint (0,3))] #random choice
    for i in x:#drawing the original shape 
        if move == "rotated 90 to the left" or (move == "rotated 90 to the right"):
            if move == "rotated 90 to the left":
                angle = 90
            if move == "rotated 90 to the right":
                angle = -90
            newx = math.cos(angle)*i-math.sin(angle)*(y[m])#formula to rotate 
            newy = math.sin(angle)*i+math.cos(angle)*(y[m])
        elif move == "mirrored on the xaxis":
            newx = i
            newy = (y[m])*-1
        else:
            newx = i*-1
            newy = (y[m])
        if m == 0:
            pu()
        goto (newx,newy)
        pd()
        m += 1

    while available_answer == True:
        available_answer = False
        answer = input ("""\ndid the shape
rotated 90 to the left
rotated 90 to the right 
mirrored on the xaxis
OR mirrored on the yaxis \n""")
        if answer not in choices:
            available_answer = True 
            print ("\nplease write the answer how it is showen\n")

    if answer == move:
        print ("\nThat is correct the shape did",move)
        points += 1
        print ("you got", points,"answer right")
    else:
        print ("\nSorry that is incorrect the shape",move)
    clear()
