# Project 11: Multi-User System

users = {}

while True:
    print("\n=== Main Menu ===")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    # Register
    if choice == 1:
        username = input("Enter username: ")
        
        if username in users:
            print("Username already exists")
        else:
            password = input("Enter password: ")
            users[username] = password
            print("Registered successfully")

    # Login
    elif choice == 2:
        attempts = 0

        while attempts < 3:
            username = input("Enter username: ")
            password = input("Enter password: ")

            if username in users and users[username] == password:
                print("Login successful")

                # User Menu
                while True:
                    print("\n--- User Menu ---")
                    print("1. Check Even/Odd")
                    print("2. Calculator")
                    print("3. Logout")

                    user_choice = int(input("Enter choice: "))

                    # Even / Odd
                    if user_choice == 1:
                        num = int(input("Enter number: "))
                        if num % 2 == 0:
                            print("Even")
                        else:
                            print("Odd")

                    # Calculator
                    elif user_choice == 2:
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

                    # Logout
                    elif user_choice == 3:
                        print("Logged out")
                        break

                    else:
                        print("Invalid choice")

                break  # exit login loop after success

            else:
                print("Invalid credentials")
                attempts += 1
                print(f"Attempts left: {3 - attempts}")

        if attempts == 3:
            print("Account Locked")

    # Exit
    elif choice == 3:
        print("Program Ended")
        break

    else:
        print("Invalid choice")
