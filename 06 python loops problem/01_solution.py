def CountPositive(num):
    count = 0
    for i in num:
        if i > 0:
            count+=1
    
    print("All positive Number count is: ",count)



number = [int(item) for item in input("Enter the list items : ").split()]

print(number)

CountPositive(number)
