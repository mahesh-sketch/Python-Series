

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def fullName(self):
        return f"{self.brand} {self.model}"
      
    
class Battery:
    def battery_info(self):
        return "This is Battery"

class Engine:
    def engine_info(self):
        return "This is Enginer"

class ElectricCar(Battery,Engine,Car):
    pass


my_new_tesla = ElectricCar("Tesla" , "Model 5")
print(my_new_tesla.fullName())
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())
