# Password Strength Checker
# Problem: Check if a password is "Weak","Medium",or "Strong". Criteria:<6 chars(Weak),6-10 chars(Medium),>10 chars(Strong).

password = "Radheradhe@"
password_length = len(password)  
# if len(password) <6:
if password_length <6:
    strength = "Weak"
    
# elif len(password) <=10:
elif password_length <=10:
    strength = "Medium"
else:
    strength = "Strong"

print("Password strength is: ", strength)  