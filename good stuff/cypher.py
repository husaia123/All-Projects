abc = "abcdefghijklmnopqrstuvwxyz"
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
try:
    key = int (input ("enter a digit "))
except ValueError:
    key = int (input("please put in a digit, this is your last chance "))
    
finalmessage = ""
message = input ("Put in a message and i'll turn it into a secret code ")
includekey = input ("do you want to include the digit as non coded so the reciver can decode it ")

for character in message:
    if character in abc:
        position = abc.find (character)
        newposition = (position + key) % 26
        newmessage = abc[newposition]
        finalmessage += newmessage
    elif character in ABC:
        posistion = ABC.find (character)
        newposistion = (posistion - key) %26
        newmessage = ABC[newposistion]
        finalmessage += newmessage
    
    else:
        finalmessage += character
    

if includekey == "yes":
    finalmessage += (" THE KEY IS " + str (key))
print ("Your new secret message is", finalmessage)


