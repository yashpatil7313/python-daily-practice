# Project 1: User Info & Decision System

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print(f"\nHello {name} from {city}")

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

if age < 10:
    print("You are a kid")
elif age < 18:
    print("You are a teenager")

num = int(input("\nEnter a number: "))

if num > 0:
    print("Number is Positive")
elif num < 0:
    print("Number is Negative")
else:
    print("Number is Zero")

if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")
