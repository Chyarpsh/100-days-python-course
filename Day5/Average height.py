# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total_height = sum(student_heights)
print("total height =",total_height)
number_of_students= len(student_heights)
print("number of students =",number_of_students)
average_height = round(total_height/number_of_students)
print("average height =",average_height)