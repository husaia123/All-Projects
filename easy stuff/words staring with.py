f = open("words", "r")
letter = input ("Choose a letter/s to see all the words that start with the it ")
length = len (letter)
for x in f:
    if length == 1:
        if (x[0]) == letter:
            print (x,end="")
    else:
        if (x[0:length]) == letter:
            print (x,end="")
