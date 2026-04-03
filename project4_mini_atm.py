balance = 1000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(f"Your balance is {balance}")

    elif choice == 2:
        amount = int(input("Enter amount: "))
        balance += amount
        print(f"Updated balance: {balance}")

    elif choice == 3:
        amount = int(input("Enter amount: "))
        if amount > balance:
            print("Insufficient balance")
        else:
            balance -= amount
            print(f"Updated balance: {balance}")

    elif choice == 4:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")
