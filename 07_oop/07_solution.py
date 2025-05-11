# Static Method
# Problem: Add  a static method to the Car class that returns a general description of a car. 
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
   @staticmethod  
   def general_description():
       return "Cars are means of transport"
 
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
       return "Electric charge"

 

safari = Car("Tata", "Safari")

print(safari.general_description())  
 