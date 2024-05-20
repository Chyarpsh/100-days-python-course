<<<<<<< HEAD
# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
weight_int= int(weight)
height_float = float(height)
BMI = weight_int/(height_float*height_float)
BMI_int = int(BMI)
=======
# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
weight_int= int(weight)
height_float = float(height)
BMI = weight_int/(height_float*height_float)
BMI_int = int(BMI)
>>>>>>> 8d17104e98611fd8c4bd74c62dca46f1d3fcc446
print(BMI_int)