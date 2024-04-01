class Car:
    
    def __init__(self,brand,model):
        # change brand in to __brand means private 
        self.__brand = brand
        self.model = model
    
    @property
    # Getter method
    def get_brand(self):
        return self.__brand + " !"
    
    @get_brand.setter
    # Setter method
    def set_brand(self,brandname):
        self.__brand = brandname
    
    def fullName(self):
        return f"{self.__brand} {self.model}"
    
        
        
my_car = Car("Tesla","Model 5")
# print(my_car.__brand)   # Throw Error because of private attribute

my_car.set_brand = "Toyota"

print(my_car.get_brand)
        