# Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age.(eg. Dog:<2 years-Puppy food, Cat:>5 years-Senior cat food).
    
pet = "Cat"
age = 1

if pet == "Dog":
    if age < 2:
        food = "Puppy food"
    elif age > 5:
        food = "Senior dog food"
    else:
        food = "Adult dog food"
elif pet == "Cat":
    if age < 2:
        food = "Kitten food"
    elif age > 5:
        food = "Senior cat food"
    else:
        food = "Adult cat food"
else:
    food = "Unknown pet type"

print(f"{pet}, {age} years - {food}")

