# Weather Activity Suggestiion
# Problem: Suggest an activity based on the weather (eg. Sunny - Go for a walk, Rainy- Read a Book, Snowy-Build a snowman).
# weather = "Sunny"

weather = input("Please Select current weather:")
  
if weather == "Sunny":
    activity = "Go for a walk"
elif weather == "Rainy":
    activity = "Read a Book"
elif weather == "Snowy":
    activity = "Build a snowman"
    
print(activity)