from replit import clear
from art import logo


def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
"-" : subtract,
"+" : add,
"*" : multiply,
"/" : divide
}
is_screen_on = True
while is_screen_on:
num1 = int(input("What's the first number?: "))
print("Pick an operator:'operation'")
num2 = int(input("What's the next number?: "))

for keys in operations:
  print(operations)

