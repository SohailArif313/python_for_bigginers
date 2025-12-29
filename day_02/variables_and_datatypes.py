# ✅ Basic Python Syntax & Data Types

print("Hello, world")
print("I am Sohail")
print("I am a Python programmer")

age = 18
old = False
year = None

print("Type of age:", type(age))     # int
print("Type of old:", type(old))     # bool
print("Type of year:", type(year))   # NoneType


# ✅ Arithmetic Operators

a = 5
b = 2

print("a + b =", a + b)       # 7
print("a - b =", a - b)       # 3
print("a * b =", a * b)       # 10
print("a ** b =", a ** b)     # 25 (Exponentiation: 5^2)
print("a / b =", a / b)       # 2.5
print("a % b =", a % b)       # 1 (Remainder)


# ✅ Relational (Comparison) Operators

print("a == b:", a == b)      # False
print("a != b:", a != b)      # True
print("a > b:", a > b)        # True
print("a < b:", a < b)        # False
print("a >= b:", a >= b)      # True
print("a <= b:", a <= b)      # False


# ✅ Assignment Operators

num = 20
num += 10                    # num = 30

print("num =", num)
print("num * 2 =", num * 2)         # 60
print("num / 2 =", num / 2)         # 15.0
print("num % 2 =", num % 2)         # 0
print("num ** 2 =", num ** 2)       # 900
print("Square root of num =", num ** 0.5)
print("num to power 4 =", num ** 4)


# ✅ Logical Operators

a = 10
b = 5

print("a and b =", a and b)                # returns b = 5 (both non-zero)
print("a or b =", a or b)                  # returns a = 10 (first non-zero)
print("not (a > b) =", not (a > b))        # False


# ✅ Type Casting

a = "22.3"
a = float(a)
print("After type casting:", a)            # 22.3


# ✅ Input in Python (with f-string output)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))

print(f"Your name is {name}, your age is {age}, and your marks are {marks}.")
