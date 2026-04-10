# Project 12: Smart Student System

name = ""
total = 0
average = 0
grade = ""
result = ""

while True:
    print("\n1. Enter Student Details")
    print("2. Show Result")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    # Enter Student Details
    if choice == 1:
        name = input("Enter student name: ")
        n = int(input("Enter number of subjects: "))

        total = 0

        for i in range(n):
            marks = int(input(f"Enter marks for subject {i+1}: "))
            total += marks

        average = total / n

        # Grade calculation
        if average >= 90:
            grade = "A"
        elif average >= 75:
            grade = "B"
        elif average >= 50:
            grade = "C"
        else:
            grade = "Fail"

        # Result
        if average >= 50:
            result = "Pass"
        else:
            result = "Fail"

        print("Details saved successfully")

    # Show Result
    elif choice == 2:
        if name == "":
            print("No data available. Please enter student details first.")
        else:
            print(f"\nStudent: {name}")
            print(f"Total Marks: {total}")
            print(f"Average: {average}")
            print(f"Grade: {grade}")
            print(f"Result: {result}")

    # Exit
    elif choice == 3:
        print("Program Ended")
        break

    else:
        print("Invalid choice")
