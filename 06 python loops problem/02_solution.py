def SumOfEven(number):
    sum = 0
    for i in number:
        if (i % 2 == 0):
            sum += i
    
    print("Sum of even number is: ",sum)


number = [int(item) for item in input("Enter the element: ").split()]

print(number)

SumOfEven(number)