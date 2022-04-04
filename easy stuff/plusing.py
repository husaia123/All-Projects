x = 2
print ((x), "+", (x))

while True:
    y = (int (input ()))
    if y == x + x:
        print ("correct")
        x += x
        print ((x), "+", (x))
    else:
        print ("wrong",(x), "+", (x), "is", (x + x))
        print ("please type in", (x + x))
    
