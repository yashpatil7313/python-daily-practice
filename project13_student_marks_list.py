# Project 14: Student Marks Manager

subjects = ("Math", "Science", "English")
marks = []

while True:
    print("\n1. Enter Marks")
    print("2. Show Marks")
    print("3. Calculate Total & Average")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # Enter Marks
    if choice == 1:
        marks = []   # reset list
        for i in range(len(subjects)):
            m = int(input(f"Enter marks for {subjects[i]}: "))
            marks.append(m)
        print("Marks saved successfully")

    # Show Marks
    elif choice == 2:
        if len(marks) == 0:
            print("No marks available. Please enter marks first.")
        else:
            for i in range(len(subjects)):
                print(f"{subjects[i]}: {marks[i]}")

    # Calculate Total & Average
    elif choice == 3:
        if len(marks) == 0:
            print("No marks available.")
        else:
            total = sum(marks)
            average = total / len(marks)
            print(f"Total: {total}")
            print(f"Average: {average}")

    # Exit
    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid choice")
