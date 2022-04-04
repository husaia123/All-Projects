from turtle import*
import random
from itertools import cycle 
speed (0)
x = -250
y = 250
hideturtle()
ship_hits = 0
misses = 0
m = 0
q = 0
xchanged = False
forcoordinates = 1#for writing down the x and y axis in turtle
onetoten = ["1","2","3","4","5","6","7","8","9","10"]#xaxis
abc = ["A","B","C","D","E","F","G","H","I","J"]#yaxis
allspots = []
for element in onetoten:
    thing1 = element
    for element in abc:
        thing = element
        spot = thing1 + thing 
        allspots.append (spot)

def coordinates ():
    global x
    global y
    global m 
    global q
    #finding x coordinates 
    if x < 5:#x spot is a negative
        x = ((x-5)*50) -40
    elif x == 5:
        x = -40
    else:#x spot is positive 
        x = ((x-6)*50) + 10

    #finding y coordinates
    if y > 5:#y spot is a negative 
        y = ((y-6)*50) + 10
        y *= -1
        if m == 1 and q == 1:
            y -25
    elif y == 5:
        y = 40
    else:#y spot is a positive 
        y = ((5-y)*50) + 40   

def a ():    
    global add2
    global add1

    if x == 1:#to change the abc+1
        add1 = (abc[(abc.index (add2[1]))+1])#next yaxis space of ship
        add2 = add2[0]#adding spot1 y axis and old xaxis together
        add2 += add1#making yaxis by self 

    else:#to change the number+1
        add1 = (onetoten[(onetoten.index (add2[0]))+1])#next xaxis space of ship
        add2 = add2[1]#making xaxis by self
        add2 = add1 + add2#adding spot1 x axis and old yaxis together


def hit ():
    global x
    global y
    pu ()
    goto (x,y)
    pd ()
    seth (315)
    fd (45)
    pu()
    goto(x,y-31)
    pd()
    seth (45)
    fd(45)
    for ship_name, coords in allships.items():
        for i in coords:
            if i not in allship_spots:
                m = 1
            else:
                m = 2
                break

        if m == 1:#ship is completely destroyed
            first = 0
            last = -1
            spot1 = coords[first]
            for q in range (2):

                if len(spot1) == 3:
                    x = 10
                    y = (abc.index(spot1[2]))+1
                    length = 3

                else:
                    x = int (spot1[0])
                    y = (abc.index(spot1[1]))+1
                    length = 1

                coordinates()
                pu ()
                color("red")

                if q == 1:#going to the second spot (second round)
                    for numberofspots in (coords):#has variable spot1 = last coord in destroyed ship
                        last += 1
                if len(spot1) == 3:
                    x = 10
                    y = (abc.index(spot1[2]))+1
                    length = 3

                else:
                    x = int (spot1[0])
                    y = (abc.index(spot1[1]))+1
                    length = 1
                    if length == 3:#if x = 10
                        thingxfirst = 10
                        thingyfirst = 2
                    else: 
                        thingxfirst = (int (spot1[0]))
                        thingyfirst = 1

                    if (int (spot1[0])) < (int((coords[last])[0])):#goes right
                        seth (90)
                        fd(31)
                        seth (180)
        
                    elif (int (spot1[0])) > (int((coords[last])[0])):#goes left:      
                        seth (-180)#same as 0

                    elif (abc.index(spot1[thingyfirst])) > (abc.index((coords[last])[1])):#goes down
                        seth (90)
    
                    elif (abc.index(spot1[thingyfirst])) < (abc.index((coords[last])[])):#goes up
                        seth (-90)#same as 270

                    for i in coords:
                        fd(50)

                else:#going to first spot (first round)
                    goto(x,y)
                spot1 = (coords[last])
                

                

def miss ():
    print ("MISS at", guess)
    pu()
    goto(x+15,y)
    pd()
    seth(0)
    circle(-16)

for i in range (2):#making outside wall 
    pu()
    goto (-250,250)
    pd()
    fd(500)
    rt(90)
for i in range (10):#making the grid with x and y axis
    pu()
    if forcoordinates == 2:
        fd(10)
        write (i, align='center') #writing down xaxis
    goto(-250,y-50)
    seth(0)
    pd()
    fd(500)
    pu()
    fd(10)
    write (abc[i], align='center')#writing down yaxis
    pd()
    y -= 50
    pu()
    seth(270)
    goto(x+50,250)
    pd() 
    fd(500)
    x += 50
    forcoordinates = 2
pu()
fd (10)
pd()
write (10, align='center')
allship_spots = ["repeat"] #all spots taken
norepeats = []


while allship_spots != norepeats:#repeats if spot is taken up twice 
    rangeoflist = 8
    destroyer = []#2space
    cruiser = []#3 space
    submarine = []#3 space
    battleship = []#4 space
    aircraft_carrier = []#5 spaces
    allship_spots = ["repeat"]
    norepeats = []

    for i in range (4):#choosing random starting spots for 5 different ships
        add1 = abc[random.randint((0),rangeoflist)]#choosing a random letter
        add2 = onetoten[random.randint((0),rangeoflist)]#choosing a random number
        add2 += add1

        if rangeoflist == 8:#destroyer 2
            destroyer.append (add2)
            x = (random.randint(1,2))#to change x or y axis: x = 1 changes y
            a()
            destroyer.append (add2)

        elif rangeoflist == 7:#cruiser & submarine 3
            cruiser.append (add2)

            x = (random.randint(1,2))
            for i in range (2):
                a ()
                cruiser.append (add2)

            add1 = abc[random.randint((0),rangeoflist)]#spot1 spot for same length of ship but different ship
            add2 = onetoten[random.randint((0),rangeoflist)]
            add2 += add1

            x = (random.randint(1,2))#submarine 3
            submarine.append (add2)
            for i in range (2):
                a ()
                submarine.append (add2)
         
        elif rangeoflist == 6:#battleship 4
            battleship.append (add2)

            x = (random.randint(1,2))
            for i in range (3):
                a ()
                battleship.append (add2)

        elif rangeoflist == 5:#aircraft_carrier 5
            aircraft_carrier.append (add2)
            x = (random.randint(1,2))
            for i in range (4):
                a ()
                aircraft_carrier.append (add2)

        rangeoflist -= 1

    allship_spots.remove ("repeat")

    for i in destroyer:
        allship_spots.append (i)
    for i in cruiser:
        allship_spots.append (i)
    for i in submarine:
        allship_spots.append (i)
    for i in battleship:
        allship_spots.append (i)
    for i in aircraft_carrier:
        allship_spots.append (i)

    for element in allship_spots:
        if element not in norepeats:
            norepeats.append (element)

allships = {"destroyer": destroyer, "cruiser": cruiser, "submarine": submarine, "battleship": battleship, "aircraft_carrier": aircraft_carrier}
names = [destroyer,aircraft_carrier,cruiser,submarine,battleship]

print (allship_spots)
x = input ("\nThis is a game of battle ship. type RULES to see the rules or type START to \nstart playing ")
x = x.upper()
while x != "START":
    x = x.upper()
    if x == "RULES":
        x = input ("""\nThe rules are they're are 5 ships hidden and you have to shoot
them down by guessing their corridents. The Aircraft Carrier is 5 spaces long,
the battle ship is 4, the Submarine is 3, the cruiser is 3 and the destroyer 
is 2. Each hit you get will show up as a X, a miss will show up as a O.

GOOD LUCK. Type START when ready.
""")

    else:
        x = input ("Please type only START or RULES\n")
    x = x.upper()
    

while ship_hits != 17 and misses != 10:
    guess = input ("""\nType in a coordinates to shoot a missile at that spot.
Start with the xaxis first then y axis.        E.G 9B \n\n""")
    guess = guess.upper()

    if guess not in allspots:#not a valid guess or already guessed
        print ("That spot is not avialble. Please choose another spot\n")
    else:
        if len(guess) == 3:
            x = 10
            y = (abc.index(guess[2]))+1
        else:
            x = int (guess[0])
            y = (abc.index(guess[1]))+1

        coordinates()                     
        if guess in allship_spots:
            allship_spots.remove (guess)
            hit ()
            print ("HIT at", guess)
            ship_hits += 1 
        
        else:
            miss ()
            misses += 1 
        allspots.remove (guess)
        

leftspots = []
color("red")
m = 0
if misses == 10:
    for i in allship_spots:
        guess = i 
        if len(guess) == 3:
            x = 10
            y = (abc.index(guess[2]))+1
        else:
            x = int (guess[0])
            y = (abc.index(guess[1]))+1
        coordinates ()
        hit()
    print ("You lost, only", (17-ship_hits),"more hits and you would of Won. The last spots were at", allship_spots,"and will show up on the grid as a red X")
else:
    print ("Congradulations, you won with", (10-misses),"mistakes avialable left")
