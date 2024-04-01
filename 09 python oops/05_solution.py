class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def fullName(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Disel"

class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize
    
    def ElectricFullName(self):
        return f"{self.fullName()} {self.batterySize}"
    
    def fuel_type(self):
        return "Electric Charge"
        
        
my_car = Car("Toyota","Supra")
print(my_car.fullName() +" "+ my_car.fuel_type())

my_elecar = ElectricCar("Tesla","Model 5","300wt")
print(my_elecar.fullName() + " " + my_elecar.fuel_type())
        