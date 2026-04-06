# Registration
print("=== Registration ===")
username = input("Create username: ")
password = input("Create password: ")

# Bonus: password length check
while len(password) < 4:
    print("Password must be at least 4 characters")
    password = input("Create password again: ")

# Store credentials
stored_username = username
stored_password = password

print("\nRegistration Successful!\n")

# Login system
attempts = 0

while attempts < 3:
    print("=== Login ===")
    login_username = input("Enter username: ")
    login_password = input("Enter password: ")

    if login_username == stored_username and login_password == stored_password:
        print("Login Successful")
        break
    else:
        print("Invalid credentials")
        attempts += 1
        print(f"Attempts left: {3 - attempts}")

# Lock system
if attempts == 3:
    print("Account Locked")
