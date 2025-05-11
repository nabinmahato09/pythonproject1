# Class Variables
# Problem:Add a class variable to Car that keeps track of the number of cars created.
class Car:
    total_car = 0
    
    def __init__(self, brand, model):
    # making it private __ ('double dash')
        self.__brand = brand
        self.model = model
        Car.total_car += 1
#  introduce getter method
    def get_brand(self):
        return self.__brand + "!"
     
    def full_name(self): 
        return f"{self.brand} {self.model}"
    
    
    def fuel_type(self):
       return "Petrol or Diesel"
        
 
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
       return "Electric charge"

# my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
# print(my_tesla.__brand)
# print(my_tesla.fuel_type())  

Car("Tata", "Safari")
Car("Tata", "Nexon")
# print(safari.fuel_type())
print(Car.total_car)   
     
# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model) 
# print(my_car.full_name()) 

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.brand)