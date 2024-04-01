#  Add a class variable to Car that 
# keeps track of the number of cars created.

class Car:
    
    total_car = 0
    
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        Car.total_car += 1
    
    def fullName(self):
        return f"{self.brand} {self.model}"
    

class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize
    
    def ElectricFullName(self):
        return f"{self.fullName()} {self.batterySize}"
        
        
my_car1 = Car("Toyota","Supra")
print(my_car1.fullName())

my_car2 = Car("Tata","Nexon")
print(my_car2.fullName())


print(Car.total_car)        