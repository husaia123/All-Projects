def factorial (x):
  if x == 3:
    return 
  else:
    print(x, "*(", x-1, ")!")
    return x * factorial(x-1)
    
		
print(factorial(100))
