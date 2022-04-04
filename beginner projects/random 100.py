import random
f = open ("100 RAN CHARACTERS","w")
x = 0
while x < 1000:
    f.write (str(random.randint (0,100)))
    x += 1
    if x < 1000:
        f.write (",")
    if x % 38 == 0: 
        f.write ("\n")