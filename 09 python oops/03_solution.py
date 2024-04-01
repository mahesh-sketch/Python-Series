class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def fullName(self):
        return f"{self.brand} {self.model}"
    

class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize
    
    def ElectricFullName(self):
        return f"{self.fullName()} {self.batterySize}"
        
        
my_car = ElectricCar("Tesla","Model 5","300wt")
print(my_car.ElectricFullName())
        