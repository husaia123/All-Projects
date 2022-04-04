import random
print ("Starting from a number that you choose. Type rules to see the rules of the game or type start to start the game")
x = (str (input ()))
if x == "rules":
    print ("The rules are you and the other player have 80$ and can only take 1 to a number that you choose a turn, who ever gets to a negative number first loses")
    x = (str (input ()))
if x == "start":
    print ("choose a number to use")
    usednumber = (int (input ()))
    if usednumber > 69 :
        print ("please choose another number")
    print ("Ok 1 to ",(str(usednumber),". starting from 80"))
    print ("you go first")
number = 80
while number >= -1:
    y = (int (input ()))
    if y > int (usednumber):
        print ("Invalide number, choose another number")
    if y < 1:
        print ("Invalide number, choose another number")
    if 1 > y <= int (usednumber):
        print (number - y)
        number = (number - y)
        if number <= 0:
            print ("You win")
            break
        print ("My turn")
        y = number % (usednumber + 1)
        if y == 0:
            y = random.randint
        number = number - random.randint (1,(usednumber))
        print (number)
        print ("Your turn")
        if number <= 0:
            print ("I win")
            break
