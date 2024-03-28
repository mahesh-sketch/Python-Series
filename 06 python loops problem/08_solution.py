def PrimeCheck(num):
    flag = False
    if num == 1:
        print(num, "is not a prime number")
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
        if flag:
            print(num, "is not a prime number")
        else:
            print(num, "is a prime number")

number = int(input("Enter number to check wheather its prime or not ? : "))
PrimeCheck(number)