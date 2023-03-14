# Define the function first
# function: add, subtract, divide, multiply and check for reminder.
# ask for the values
# call the function
# Add a while loop until user wants to exit

def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")


def subtract(a, b):
    result = a - b
    print(f"\n{a} - {b} = {result}")


def divide(a, b):
    result = a // b
    print(f"\n{a} / {b} = {result}")


def multiply(a, b):
    result = a * b
    print(f"\n{a} x {b} = {result}")


def remainder(a, b):
    result = a % b
    print(f"\nThe remainder of {a} % {b} = {result}")


operator = ["a", "s", "d", "m", "r", "e"]

loop = True
while loop:
    prompt = "\na to add\ns to subtract\nd to divide\nm to multipy\nr to get the remainder\ne to exit calculator".lower()
    print(prompt)
    user_choice = input("Enter a letter: ")
    if user_choice == "a":
        num1 = int(input("enter a number: "))
        num2 = int(input("enter a number: "))
        add(a=num1, b=num2)
    elif user_choice == "s":
        num1 = int(input("enter a number: "))
        num2 = int(input("enter a number: "))
        subtract(a=num1, b=num2)
    elif user_choice == "d":
        num1 = int(input("enter a number: "))
        num2 = int(input("enter a number: "))
        divide(a=num1, b=num2)
    elif user_choice == "m":
        num1 = int(input("enter a number: "))
        num2 = int(input("enter a number: "))
        multiply(a=num1, b=num2)
    elif user_choice == "r":
        num1 = int(input("enter a number: "))
        num2 = int(input("enter a number: "))
        remainder(a=num1, b=num2)
    elif user_choice == "e":
        print("Goodbye...")
        loop = False
    elif user_choice not in operator:
        loop = True
        print("Operator unknown,\nTry again.")
