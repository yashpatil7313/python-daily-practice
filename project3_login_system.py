# Stored data
stored_name = "Yash"
stored_age = 20

# User input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Verification
if name == stored_name and age == stored_age:
    print("\nLogin Successful")

    # Extra feature
    num = int(input("Enter a number: "))

    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

elif name == stored_name:
    print("\nAge incorrect")

else:
    print("\nUser not found")
