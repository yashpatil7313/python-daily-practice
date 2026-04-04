# Project 7: User Menu System

while True:
    print("\n1. Check Even/Odd")
    print("2. Check Positive/Negative/Zero")
    print("3. Simple Calculator")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # Even / Odd
    if choice == 1:
        num = int(input("Enter number: "))
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")

    # Positive / Negative / Zero
    elif choice == 2:
        num = int(input("Enter number: "))
        if num > 0:
            print("Positive")
        elif num < 0:
            print("Negative")
        else:
            print("Zero")

    # Calculator
    elif choice == 3:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        op = input("Enter operator (+, -, *, /): ")

        if op == "+":
            print(f"Result: {a + b}")
        elif op == "-":
            print(f"Result: {a - b}")
        elif op == "*":
            print(f"Result: {a * b}")
        elif op == "/":
            if b != 0:
                print(f"Result: {a / b}")
            else:
                print("Cannot divide by zero")
        else:
            print("Invalid operator")

    # Exit
    elif choice == 4:
        print("Program Ended")
        break

    # Invalid choice
    else:
        print("Invalid choice")
