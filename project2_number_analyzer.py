# Project 2: Smart Number Analyzer

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"\nWelcome {name}!")

if age >= 18:
    print("You can use full features")
else:
    print("Limited access")

n = int(input("\nHow many numbers do you want to check? "))

even_count = 0
odd_count = 0

for i in range(n):
    num = int(input("Enter number: "))

    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

    if num % 2 == 0:
        print("Even")
        even_count += 1
    else:
        print("Odd")
        odd_count += 1

    if num > 100:
        print("Greater than 100")
    else:
        print("Less than or equal to 100")

print(f"\nTotal Even numbers: {even_count}")
print(f"Total Odd numbers: {odd_count}")
