# ✅ Conditional Statement: Voting Eligibility

age = 18

if age >= 18:
    print("Can vote")
else:
    print("Can't vote")


# ✅ Conditional Statement: Grading System

marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 80 and marks < 90:
    grade = "B"
elif marks >= 70 and marks < 80:
    grade = "C"
elif marks >= 60 and marks < 70:
    grade = "D"
else:
    print("You have failed")
    grade = None

print("Grade of student is:", grade)


# ✅ Nested If Statement: Age Category Checker

age = int(input("Enter your age: "))

if age >= 18:
    if age >= 33:
        print("You are a senior citizen")
    else:
        print("You are an adult")
else:
    print("You are a minor")
