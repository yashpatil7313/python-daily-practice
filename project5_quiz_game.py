# Welcome user
name = input("Enter your name: ")
print(f"\nWelcome {name} to the Quiz Game!")

# Score variable
score = 0

# Question 1
ans1 = input("What is 2 + 2? ")
if ans1 == "4":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 2
ans2 = input("What is capital of India? ")
if ans2.lower() == "delhi":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 3
ans3 = input("What is 5 * 2? ")
if ans3 == "10":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Final score
print(f"\nYour final score is: {score}")
