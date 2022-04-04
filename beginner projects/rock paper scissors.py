import random
print ("lets play rock, paper, scissors. choose rock, paper or scissors ")
while True:
    x = (str (input ()))
    y = random.sample (("rock","paper","scissors"), 1)[0]
    #rock
    if x == "rock" and y == "rock":
        print (y)
        print ("tie")
    elif x == "rock" and y == "paper":
        print (y)
        print ("you lose")
    elif x == "rock" and y == "scissors":
        print (y)
        print ("you win")
    #paper
    elif x == "paper" and y == "paper":
        print (y)
        print ("tie")
    elif x == "paper"  and y == "rock":
        print (y)
        print ("you win")
    elif x == "paper"  and y == "scissors":
        print (y)
        print ("you lose")
    #scissors
    elif x == "scissors" and y == "scissors":
        print (y)
        print ("tie")
    elif x == "scissors" and y == "paper":
        print (y)
        print ("you win")
    elif x == "scissors" and y == "rock":
        print (y)
        print ("you lose")
