age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
age_int = int(age)
weeks_left = (90 - age_int)* 52
weeks_left_int = int(weeks_left)
print("You have", weeks_left_int,"weeks left.")