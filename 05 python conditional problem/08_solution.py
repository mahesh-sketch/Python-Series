def PasswordChecker(password):
    if(len(password) < 6):
        print("Weak Password")
    elif(len(password) >=6 and len(password)<=10):
        print("Medium Password")
    elif(len(password) > 10):
        print("Strong Password")
        
password = str(input("Enter your Password to check Strength:"))
PasswordChecker(password)
        