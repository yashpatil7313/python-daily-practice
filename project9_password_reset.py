# Stored data
stored_username = "yash"
stored_password = "1234"

# Ask username
username = input("Enter username to reset password: ")

# Check username
if username == stored_username:

    attempts = 0

    while attempts < 3:
        new_password = input("Enter new password: ")
        confirm_password = input("Confirm password: ")

        # Optional rule (bonus)
        if len(new_password) < 4:
            print("Password must be at least 4 characters")
            continue

        # Check match
        if new_password == confirm_password:
            stored_password = new_password
            print("Password reset successful")
            break
        else:
            print("Passwords do not match")
            attempts += 1
            print(f"Attempts left: {3 - attempts}")

    # After 3 failed attempts
    if attempts == 3:
        print("Password reset failed")

else:
    print("User not found")
