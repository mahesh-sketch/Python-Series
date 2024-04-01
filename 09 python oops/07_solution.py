class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def fullName(self):
        return f"{self.brand} {self.model}"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
  

class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize
    
    def ElectricFullName(self):
        return f"{self.fullName()} {self.batterySize}"
    
        
        
my_car = Car("Toyota","Supra")

print(my_car.general_description())

print(Car.general_description())


        