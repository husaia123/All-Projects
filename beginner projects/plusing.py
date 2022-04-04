x = 2
print ((x), "+", (x))

while 2 == 2:
    y = (int (input ()))
    if y == x + x:
        print ("correct")
        x = x + x
        print ((x), "+", (x))
    else:
        print ("wrong",(x), "+", (x), "is", (x + x))
        print ("please type in", (x + x))
    
