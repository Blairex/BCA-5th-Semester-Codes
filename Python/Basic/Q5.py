# Write a Python program that takes a student's score as input and prints their corresponding grade based on the given criteria.

score = float(input("Enter the student's score: "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score <= 89:
    print("Grade: B")
elif score >= 70 and score <= 79:
    print("Grade: C")
elif score >= 60 and score <= 69:
    print("Grade: D")
elif score < 60 and score >= 0:
    print("Grade: F")
else:
    print("Invalid score.")
