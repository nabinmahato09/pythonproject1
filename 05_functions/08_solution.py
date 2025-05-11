# Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and points them in the format key: value.
def print_kwargs(**kwargs):
   for key, value in kwargs.items():
       print(f"{key}:{value}")


print_kwargs(name="Shaktiman", power="lazer")
print_kwargs(name="Shaktiman")
print_kwargs(name="Shaktiman", power="lazer", enemy = "Dr. Jackaal")