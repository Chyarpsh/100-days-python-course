
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# 🚨 Don't change code above 👆
# Write your code below 👇
words = sentence.split()
# Create a dictionary using dictionary comprehension
result = {word: len(word) for word in words}
print(result)