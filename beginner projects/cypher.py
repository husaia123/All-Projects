abc = "abcdefghijklmnopqrstuvwxyz"
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
try:
    key = int (input ("enter a digit "))
except ValueError:
    key = int (input("please put in a digit, this is your last chance "))
    
finalmessage = ""
message = input ("Put in a message and i'll turn it into a secret code ")

for character in message:
    if character in abc:
        position = abc.find (character)
        newposition = (position + key) % 26
        newmessage = abc[newposition]
        finalmessage += newmessage
    elif character in ABC:
        position = ABC.find (character)
        newposition = (position + key) % 26
        newmessage = ABC[newposition]
        finalmessage += newmessage
    else:
        finalmessage += character

print ("Your new secret message is", finalmessage)



