def fib(n):
    d = 1
    a = 1
    if n < 0:
        print (0)
    else:
        for i in range (n):
            print (d) 
            d = d+a
            a = d-a
while True:           
    dig = input('how many digits ')
    fib (int (dig))
