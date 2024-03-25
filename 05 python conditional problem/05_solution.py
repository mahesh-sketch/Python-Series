def Acitivity(weather):
    if(weather == "Sunny" or weather == "sunny"):
        print("Go for walk")
    elif(weather == "Rainy" or weather == "rainy"):
        print("Read a book")
    elif(weather == "Snowy" or weather == "snowy"):
        print("Build a snowman")
    else:
        print("Check your weather name!")


weather = str(input("Enter your weather:"))
Acitivity(weather)