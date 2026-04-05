# Stored data
stored_username = "yash"
stored_password = "1234"

# Attempts counter
attempts = 0

# Loop (max 3 attempts)
while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check credentials
    if username == stored_username and password == stored_password:
        print("Login Successful")
        break
    else:
        print("Invalid credentials")
        attempts += 1

        # Show remaining attempts
        print(f"Attempts left: {3 - attempts}")

# Lock system
if attempts == 3:
    print("Account Locked")
