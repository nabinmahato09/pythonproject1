# Find the first Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.
given_string = "nabin"


for char in given_string:
    print(char)
    if given_string.count(char) == 1:
       print("Char is:", char)
       break