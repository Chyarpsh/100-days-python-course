input_string = ('{"Monday": 12, '
                '"Tuesday": 14, '
                '"Wednesday": 15, '
                '"Thursday": 14, '
                '"Friday": 21, '
                '"Saturday": 22, '
                '"Sunday": 24}')
weather_c = eval(input_string)
# 🚨 Don't change code above 👆
weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()}

# Write your code 👇 below:

print(weather_f)