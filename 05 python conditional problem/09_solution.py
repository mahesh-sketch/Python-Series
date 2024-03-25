def LeapYearCheck(year):
    if(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(year , "is Leap Year")
    else:
        print(year , "is not a Leap Year")

year = int(input("Enter Year to check Leapyear or not: "))
LeapYearCheck(year)