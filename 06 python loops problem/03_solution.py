def Multiplication(num):
    for i in range(1,11):
        if i == 5:
            continue
        print(num , '*' , i , '=' , num * i)


num = int(input("Enter Your Number: "))

Multiplication(num)