name  = input("enter student name:")

m1 = int(input("enter marks for subject 1: "))
m2 = int(input("enter marks for subject 2:"))
m3 = int(input("enter marks for subject 3: "))

total = m1 + m2 + m3
average = total / 3

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"

if average >= 50:
    result = "Pass"
else:
    result = "Fail"

print(f"\nStudent: {name}")
print(f"Total Marks: {total}")
print(f"Average: {average}")
print(f"Grade: {grade}")
print(f"Result: {result}")
