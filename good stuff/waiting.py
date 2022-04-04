import time
def thing():
    while True:
        timetowait = int (input ("how long do you want to wait in seconds "))            
        try:
            timetowait = int (timetowait)
        except ValueError:
            print ("please put in a real number")
            continue
        print ("before: ", time.ctime())
        x = 1
        for i in range (timetowait):
            time.sleep (1)
            print (x," seconds")
            x = x + 1
        print (str (timetowait)," seconds after: ",time.ctime())
    

try:
    thing()
except KeyboardInterrupt:
    print('\n\nKeyboard exception received. Exiting.')
    exit()
    
