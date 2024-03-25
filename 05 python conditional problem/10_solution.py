def PetFoodRecommand(petname,age):
    if(petname == "Dog" and age <= 2):
        print("Puppy Food")
    elif(petname == "Cat" and age >= 5):
        print("Senior Cat Food")
    else:
        print("Please check your pet age")

name = str(input("Enter your pet name(Dog/Cat): "))
age = int(input("Enter Your "+ name + " Year:"))
PetFoodRecommand(name,age)