def Age(n):
    if(n<13):
        print("Child")
    elif(n>13 and n<19):
        print("Teenager")
    elif(n>20 and n<59):
        print("Adult")
    else:
        print("Senior")

age = int(input("Enter your Age: "))
Age(age)