print ("who are you")
x = input()
print ("hello " + (x))
print ("how are you " + (x))
x = input ()
if (x == "good"):
    print ("that is good")
elif (x == "bad"):
    print ("oh well")

while (x != "7"):
    print ("pick a number between 0 and 10")

    x = input ()
    if (x == "7"):
        print ("correct")
    else:
        print ("wrong")