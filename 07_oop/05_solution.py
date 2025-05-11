# Polymorphism
# Demonstrate polymorphism by definind a method fuel_type in both Car and ElectriCar classes, but with different behaviors.

class Car:
   def __init__(self, brand, model):
    # making it private __ ('double dash')
     self.__brand = brand
     self.model = model
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

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
# print(my_tesla.__brand)
print(my_tesla.fuel_type())  

safari = Car("Tata", "Safari")
print(safari.fuel_type())   
     
# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model) 
# print(my_car.full_name()) 

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.brand)