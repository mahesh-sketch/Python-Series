def GradeCalculator(number):
    if(number>=101):
        print("Please verify your number again")
        exit()
        
    if(number >= 90):
        print("Grade is: A")
    elif(number >= 80):
        print("Grade is: B")
    elif(number >= 70):
        print("Grade is: C")
    elif(number >= 60):
        print("Grade is: D")
    else:
        print("Grade is: F")

number = int(input("Enter your Number: "))
GradeCalculator(number)