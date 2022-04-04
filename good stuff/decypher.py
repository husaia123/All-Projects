abc = "abcdefghijklmnopqrstuvwxyz"
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print ("I will decode the any cypher message but first i need the digit it was coded by ")
try:
    key = int (input ("Put in the digit here "))
except:
    key = int (input ("Please put in a real digit this is you last chance "))

finalmessage = ""

cyphermessage = input ("Put in the coded message ")

for character in cyphermessage:
    if character in abc:
        posistion = abc.find (character)
        newposistion = (posistion - key) %26
        newmessage = abc[newposistion]
        finalmessage += newmessage
    elif character in ABC:
        posistion = ABC.find (character)
        newposistion = (posistion - key) %26
        newmessage = ABC[newposistion]
        finalmessage += newmessage
    else:
        finalmessage += character

print ("The message is ",finalmessage)
