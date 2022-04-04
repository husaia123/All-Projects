import random
def hint():
    if guess == ("hint"):
        b = random.randint(1,(len (nospace))) 
        overallguess += (nospace[b])
        if overallguess in nospace:
            for char in secretword:
                if char == (" "):
                    print (" ") 
                elif char in overallguess:
                    print (char)
                    x += 1
                else:
                    print ("_")
print('''	
      #   #   ###   ##  #   ####         
      #   #  #   #  ##  #  #   #              
      #   #  #   #  ##  #  #   #             
      #####  #####  # # #  #       
      #   #  #   #  #  ##  # ####             
      #   #  #   #  #  ##  #   #              
      #   #  #   #  #  ##   #### 
	  
								   
								   
          ## ##    ###   ##   #         
         #  #  #  #   #  ##   #
         #  #  #  #   #  ##   #
         #  #  #  #####  #### #
         #  #  #  #   #  #  ###
         #  #  #  #   #  #   ##
         #     #  #   #  #   ##      
         
''')
def drawing():
    print(
'''         %%%%%%%%%%%%%%%      
         %%% /    $           
         %%%/     $           
         %%%      $          
         %%%      $          
         %%%%%%   $  %%%     
         %%%     ()            
         %%%    /||\          
         %%%    / \          
         %%%                  
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%''')


secretword = "stop watching videos"


mistakes = 0
overallguess = ""
f = open ("words").read().splitlines()
secretword = random.choice (f)
x = 0

nospace = secretword.replace(' ', '')
print ("press enter after every input or guess")
startorrule = input ("enter any key to start playing or type RULES for how the game works ")
if (startorrule.lower()) == "rules":
    input ("""
The rules are, there is a secret word that you have to guess letter by
letter.Every letter you get right it will be shown but you can only
make 6 mistakes.If you go above 6 you lose and the secret world will
be revealed. If you get lost or have no idea type in hint as a guess.
enter any key when ready to play.""")

while x != (len(nospace)) and mistakes != 6:
    guess = input ("Whats your guess ")
    x = 0
        #print ("bozingo BLANK lick my mangos") #the hint
    if guess == ("hint"):
        hint()
    else:        
        while (len(guess)) > 1:
            print ("You can only guess one letter each time")
            guess = input ("Whats your guess ")
            hint ()
        
    if guess in nospace:
        overallguess += guess
        for char in secretword:
            if char == (" "):
                print (" ") 
            elif char in overallguess:
                print (char)
                x += 1
            else:
                print ("_")
  
    elif guess != ("hint"):
        mistakes += 1
        print ("Your guess was wrong")
        print ("You have", (6 - mistakes), "lives left\n\n")
    
if x == (len(nospace)):
    print ("Congratulations, you've won")
    
else:
    drawing()
    print ("You have lost the secret word was", secretword)