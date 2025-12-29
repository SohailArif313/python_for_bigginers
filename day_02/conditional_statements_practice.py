# ✅ Program 1: Check if a number is Even or Odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# ✅ Program 2: Find the Greatest of 3 Numbers

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    print("First number is greatest:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Second number is greatest:", num2)
else:
    print("Third number is greatest:", num3)


# ✅ Program 3: Check if a Number is a Multiple of 7

n = int(input("Enter a number: "))

if n % 7 == 0:
    print("Yes, the number is a multiple of 7.")
else:
    print("No, the number is not a multiple of 7.")
