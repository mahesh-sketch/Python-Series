def CoffeeOrder(name, option):
    if option:
        print(name + " with Extra Shot")
    else:
        print(name + " Coffee")

coffee = input("Enter size of coffee (Small/Medium/Large): ").capitalize()
option = input("Extra Shot (True/False): ").capitalize()

if option == "True":
    option = True
else:
    option = False

CoffeeOrder(coffee, option)
