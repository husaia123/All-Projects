from turtle import*
import random 
hideturtle ()
speed(0)
pu ()
goto (150,250)
pd()
rt (90) 
fd (600)        
pu()
goto(-150,250)
pd()
fd(600)
pu()
goto(-300,100)
lt(90)
pd()
fd(600)
pu()
goto(-300,-100)
pd()
fd(600)
moves = 1
spot1 = 0
spot2 = 0
p = 0

def xx ():
    pu()
    seth (315)
    goto (spot1,spot2)
    pd()
    fd (200)
    rt (135)
    pu()
    goto (spot1+145,spot2)
    pd()
    seth (225)
    fd (200)
    rt (135)
    xsets.add(x)

def o ():
    pu()
    goto (spot1+20,spot2-70)
    pd()
    osets.add(x)
    for i in range (18):
        fd(20)
        rt(20)
        
print ("""\nWhere do you want to go in this game of tic tac toe.
Have the y first then the xaxis. Type options to see all the choices\n""")      
available = {"top left", "top middle", "top right", "middle left","middle", "middle right", "bottom left", "bottom middle", "bottom right"}
xsets = {""}
osets = {""}

while moves < 10:
    if moves % 2 == 0:
        x = input ("It's O turn ")
    else:
        x = input ("It's X turn ")
    x = (x.lower())

    if x == "options":#to see all moves
        print (available)
        
    elif x not in available:#choice is not correct
        print ("that choice is not available")
        
    elif x in available:
        if x == ("top left"):
            spot1 = -300
            spot2 = 250
        if x == ("top middle"):
            spot1 = -80
            spot2 = 250
        if x == ("top right"):
            spot1 = 160
            spot2 = 250
        

            
        if x == ("middle left"):
            spot1 = -300
            spot2 = 70
        if x == ("middle"):
            spot1 = -80
            spot2 = 70
        if x == ("middle right"):
            spot1 = 160
            spot2 = 70

            

        if x == ("bottom left"):
            spot1 = -300
            spot2 = -110
        if x == ("bottom middle"):
            spot1 = -80
            spot2 = -110
        if x == ("bottom right"):
            spot1 = 160
            spot2 = -110


        if moves % 2 == 0:
            o()
        else:
            xx()
        moves += 1
        available.remove (x)
        if ("top left" in xsets) and ("top middle" in xsets) and ("top right"in xsets):
            print ("Congratulations X has won")
            break
        if ("top left" in xsets) and ("middle left" in xsets) and ("bottom left" in xsets):
            print ("Congratulations X has won")
            break
        if ("top left" in xsets) and ("middle" in xsets) and ("bottom right" in xsets):
            print ("Congratulations X has won")
            break
        if ("top middle" in xsets) and ("middle" in xsets) and ("bottom middle" in xsets):
            print ("Congratulations X has won")
            break
        if ("top right" in xsets) and ("middle right" in xsets) and ("bottom right" in xsets):
            print ("Congratulations X has won")
            break
        if ("top right" in xsets) and ("middle" in xsets) and ("bottom left" in xsets):
            print ("Congratulations X has won")
            break
        if ("middle left" in xsets) and ("middle" in xsets)and ("middle right" in xsets):
            print ("Congratulations X has won")
            break
        if ("bottom left"in xsets) and ("bottom middle" in xsets) and ("bottom right" in xsets):
            print ("Congratulations X has won")
            break

            
        if ("top left" in osets) and ("top middle" in osets) and ("top right"in osets):
            print ("Congratulations O has won")
            break
        if ("top left" in osets) and ("middle left" in osets) and ("bottom left" in osets):
            print ("Congratulations O has won")
            break
        if ("top left" in osets) and ("middle" in osets) and ("bottom right" in osets):
            print ("Congratulations O has won")
            break
        if ("top middle" in osets) and ("middle" in osets) and ("bottom middle" in osets):
            print ("Congratulations O has won")
            break
        if ("top right" in osets) and ("middle right" in osets) and ("bottom right" in osets):
            print ("Congratulations O has won")
            break
        if ("top right" in osets) and ("middle" in osets) and ("bottom left" in osets):
            print ("Congratulations O has won")
            break
        if ("middle left" in osets) and ("middle" in osets)and ("middle right" in osets):
            print ("Congratulations O has won")
            break
        if ("bottom left"in osets) and ("bottom middle" in osets) and ("bottom right" in osets):
            print ("Congratulations O has won")
            break
        elif moves == 10:
            print ("It was a tie. Everyone loses AND everyone wins")
            p = 1
clear ()
if p != 1:
    for i in range (25): #random stars
        color (random.sample (("red","green","blue","orange","purple","brown","black"), 1)[0]) 
        pu()
        goto ((random.randint (-300,300)),(random.randint (-300,300)))
        pd ()
        begin_fill ()
        x = (random.randint (10,200))
        for i in range (5):
            left (144)
            forward (x)
        end_fill ()
