import math
from turtle import*
xaxis =  int (input ("Where's the first x axis coordinate"))
yaxis = int (input ("Where's the first y axis coordinate."))
secondxaxis = int (input ("Where's the sencond x axis coordinate."))
secondyaxis = int (input ("Where's the sencond y axis coordinate."))
maxxnumber = max (abs (xaxis),(abs (secondxaxis)))
maxynumber = max (abs (yaxis),(abs (secondyaxis)))


pencolor("red")
speed (0)
left (90)
goto (0,0)
def ygrid():
    goto (0,0)
    y = 1
    rt (90) #making 0
    fd (4)
    write (0, align='center')
    bk (4)
    lt (90) #end of making 0
    for i in range (1,(maxynumber+1)):
        fd (250/(abs (maxynumber))) #making + x lines 
        rt (90)
        fd (4)
        write (i, align='center')
        bk(4)
        lt (90) #end of making the + x lines
        y += 1
        if y == (maxynumber+1):#making - x lines
            bk (250)
            lt (180)
            for m in range (1,(maxynumber+1)):
                fd (250/(abs (maxynumber)))
                rt (90)
                fd (4)
                write (m*-1, align='center')
                bk (4)
                lt (90)#end of maikng - x lines
    
              
def xgrid ():
    lt (90)
    goto (0,0)
    y = 1
    for i in range (1,(maxxnumber+1)):#making + y lines
        fd (250/(abs (maxxnumber)))
        rt (90)
        fd (4)
        pu ()#making numbers fit proper
        fd (10)
        write (i, align='center')
        bk (14)
        pd()#end of making numbers fit
        lt (90)#end of making + y lines
        y += 1
        if y == (maxxnumber+1):#making - y lines 
            bk (250)
            lt (180)
            for m in range (1,(maxxnumber+1)):
                fd (250/(abs (maxxnumber)))
                rt (90)
                fd (4)
                write ((m*-1), align='center')
                bk (4)
                lt (90)#end of making - y lines



                

pd()
ygrid ()
xgrid ()
hideturtle()

firstx = (xaxis*(250/(abs(maxxnumber))))#the y and x grid small as possible
firsty = (yaxis*(250/(abs(maxynumber))))
secondx = (secondxaxis*(250/(abs(maxxnumber))))
secondy = (secondyaxis*(250/(abs(maxynumber))))#end of small of possible
pu()
goto (firstx,firsty)#first dotpoint
pd()
goto (secondx,secondy)#second dotpoint

if (secondxaxis-xaxis) == 0:#VERTICAL LINES
    xintercept = (xaxis)
    print ("The gradient is undefined")#gradient
    print ("The y intercept is undefined")#y intercept
    print ("The x intercept is", xintercept)#x intercept
    print ("x =", xintercept)
    write ("x =", xintercept)
elif (secondyaxis-yaxis) == 0:#HORIZONTAL LINES
    m = 0
    c = (yaxis)
    print ("The gradient is 0")
    print ("The y intercept is",c)
    print ("The x intercept undefined")
    print ("y =", c)
    write ("y =", c)
else:#neither horizontal or vertical 
    m = (secondyaxis-yaxis)/(secondxaxis-xaxis)#gradient
    c = (yaxis-(m*xaxis))#y intercept
    x = ((c*-1)/m)#x intercept
    yform = ("y =",m,"x + ",c)#y formula
    print ("The gradient is", (m),"or",(secondyaxis-yaxis),"/",(secondxaxis-xaxis))#gradient
    print ("The y intercept is",c,"or",yaxis-(m*xaxis))#y intercept
    print ("The x intercept is", x)#x intercept
    print ("y =",m,"x + ",c)#y formula
    print ("x = (y +",c,") /",m)#x formula
    write (yform)#writing y formula on graph

    



x = ((((secondxaxis - xaxis)**2) + (secondyaxis - yaxis)**2))#distance
print ("The distance is ",math.sqrt(x))
x = ((xaxis + secondxaxis)/2)#midpoint
y = ((yaxis + secondyaxis)/2)
print ("The midpoint is ",x,",",y)

    

 
