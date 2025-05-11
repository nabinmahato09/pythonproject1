# Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, or unripe based on its color. (eg. Banana, Green- Unripe, Yellow - Ripe, Brown - Overripe).
fruit = "Banana"
# color = input("please choose fruit color:")
color = "Brown"

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color =="Yellow":
        print("Ripe")
    elif color == "Brown":
        print("Overripe")
