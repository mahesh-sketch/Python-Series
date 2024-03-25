def FruitRipeness(colour):
    if(colour == "Green" or colour == "green"):
        print("Unripe")
    elif(colour == "Yellow" or colour == "yellow"):
        print("Ripe")
    elif(colour == "Brown" or colour == "brown"):
        print("Overripe")
    else:
        print("Please Enter Valuable Colour")

colour = str(input("Enter your Fruit colour:"))
FruitRipeness(colour)