import random
number = int (50)
print ("Starting from 50. Type rules to see the rules of the game or type start to start the game")
x = (str (input ()))
if x == "rules":
    print ("The rules are you and the other player have 50$ and can only take 1 to 7 dollars a turn, who ever gets to a negative number first loses")
    x = (str (input ()))
if x == "start":
    print ("You go first. 50")
while number >= -1:
    y = (int (input ()))
    if y > int (7):#numbers above 7
        print ("Invalide number, choose another number")
    if y <= int (7):#you pick a number
        print (number - y)
        number = (number - y)
        if number <= 0:
            print ("You win")
            break
        print ("My turn")
        y = number % 8
        if y == 0:
            y = random.randint
        number = number - random.randint (1,7)
        print (number)
        print ("Your turn")
        if number <= 0:
            print ("I win")
            break

        
