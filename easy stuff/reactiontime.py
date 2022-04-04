import time
import random
p = "y"
input ("This is a reaction time test. Soon as you see the word NOW press Enter.\nPress enter when ready")
while p == "y":
    timewait = random.randint (1,5)
    time.sleep(timewait)
    x = time.clock()
    input ("NOW")
    x = x - time.clock
    print ("You have a reaction time of",x,"seconds")
    p = input ("Want to play again. y/n ")
