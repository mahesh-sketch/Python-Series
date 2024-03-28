def Factorial(num):
    result = 1
    while(num > 0):
        result *= num
        num -= 1
    print("Factorial of number is: ",result)


number = int(input("Enter number: "))
Factorial(number) 
        