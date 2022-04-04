import math

print ('ax^2+bx+c')
a = int (input ("a:"))
b = int (input ("b:"))
c = int (input ("c:"))

try:
    q = (b-math.sqrt(b**2-4*a*c)/(2*a))
    w = (b+math.sqrt(b**2-4*a*c)/(2*a))
except ValueError:
    print ("Non real")
print (q)
print (w)
def factorise (a,b,c):
    afactors = []
    cfactors = []
    posd = []
    pose = []
    posf = []
    posg = []
    #(dx+e)(fx+g)
    for i in range(1, a + 1):
        if a % i == 0:
            afactors.append (i) 
            
    for i in range(1, c + 1):
        if c % i == 0:
            cfactors.append (i) 

    for i in afactors:
        for j in cfactors:
            if i*j+(a/i)*(c/j) == b:
                pose.append(a/i)
                posg.append(j)
                posd.append(i)
                posf.append(c/j)
        
    print (pose)
    print (posg)
    print (posd)
    print (posf)


    print (afactors)
    print (cfactors)

posg = list(dict.fromkeys(posg))
