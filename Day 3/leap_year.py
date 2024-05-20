<<<<<<< HEAD
# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
=======
# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
>>>>>>> 8d17104e98611fd8c4bd74c62dca46f1d3fcc446
    print("Not leap year")