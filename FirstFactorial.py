#Using the Python language, have the function FirstFactorial(num) take the num parameter being passed
#and return the factorial of it (ie. if num = 4, return (4 * 3 * 2 * 1)). For the test cases, the 
#range will be between 1 and 18.  

from math import factorial

def FirstFactorial(num):
    return factorial(num)

def FirstFactorial2(num):
    factorial = 1
    
    for i in range(1, num + 1):
        factorial = factorial * i
        
    return factorial
userinput = int(raw_input("Enter a number\n"))
print FirstFactorial(userinput)
print FirstFactorial2(userinput)