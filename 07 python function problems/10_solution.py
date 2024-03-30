# Create a recursive function to calculate 
# the factorial of a number.

def Factorial(num):
    if num == 0:
        return 1
    else:
        return num * Factorial(num-1) 

print(Factorial(5))