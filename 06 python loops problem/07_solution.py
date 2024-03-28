def PlayGame():
    while(True):
        number = int(input("Guess number:"))
        if(number >= 1 and number <= 10):
            print("Whoa ! you won the game and choose ", number)
            break
        else:
            print("Invalid Number ! Try again ")



PlayGame()