def NonRepeativeChar(name):
    for i in name:
        if name.count(i) == 1:
            print("char is: ", i)
            break

name = str(input("Enter String: "))
NonRepeativeChar(name)
    