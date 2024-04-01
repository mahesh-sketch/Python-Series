class Car:
    
    def __init__(self,brand,model):
        # change brand in to __brand means private 
        self.__brand = brand
        self.model = model
    
    # Getter method
    def get_brand(self):
        return self.__brand + " !"
    
    # Setter method
    def set_brand(self,brandname):
        self.__brand = brandname
    
    def fullName(self):
        return f"{self.__brand} {self.model}"
    

class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize
    
    def ElectricFullName(self):
        return f"{self.fullName()} {self.batterySize}"
        
        
my_car = ElectricCar("Tesla","Model 5","300wt")
# print(my_car.__brand)   # Throw Error because of private attribute

my_car.set_brand("Toyota")
print(my_car.get_brand())
        