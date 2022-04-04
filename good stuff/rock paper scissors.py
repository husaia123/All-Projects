import random
print ("\nlets play rock, paper, scissors. choose rock, paper or scissors \n")
while True:
    x = (str (input ()))
    y = random.sample (("rock","paper","scissors"), 1)[0]
    if (x != "rock") and (x != "paper") and (x != "scissors"):
        print ("That choice is not avialabe. Choose rock, paper or scissors")
    #rock
    elif x == y:
        print (y)
        print ("tie")

    elif x == "rock" and y == "paper":
        print (y)
        print ("you lose")
    #paper
    elif x == "paper"  and y == "scissors":
        print (y)
        print ("you lose")
    #scissors
        
    elif x == "scissors" and y == "rock":
        print (y)
        print ("you lose")
    else:
        print (y)
        print ("you win")
    print ("\n")


        



    




