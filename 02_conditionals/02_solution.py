# Problem: Movie tickets are priced based on age:$12 for adults(18 and over), $8 for child. Everyone gets a $2 discount on Wednesday.
age = 5
day = "Wednesday"

price = 12 if age >= 18 else 8
# if age >= 18:
#     price = 12
# else:
#     price = 8
if day == "Wednesday":
    price = price - 2
    # price -= 2
print("Ticket price for you is $",price)
