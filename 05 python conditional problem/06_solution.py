def Tansportation(distance):
    if(distance < 3):
        print("Walk")
    elif(distance >= 3 and distance <= 15):
        print("Bike")
    else:
        print("Car")


km = int(input("Enter your distance: "))
Tansportation(km)
