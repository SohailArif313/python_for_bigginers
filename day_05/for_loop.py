# 🔁 WHILE LOOP PRACTICE

# ✅ Print "Sohail" 5 times
i = 1
while i <= 5:
    print("🧑 Sohail")
    i += 1

print(30 * "-")

# ✅ Print numbers from 5 to 1
i = 5
while i > 0:
    print("🔢", i)
    i -= 1

print(50 * "*")

# 🔁 FOR LOOP PRACTICE

# ✅ Loop through a list of names
list1 = ["Sohail", "Haris", "Ali"]
print("📦 Names in list:")
for el in list1:
    print("👤", el)

print(50 * "*")

# ✅ Loop through each character in a string
str1 = "Sohail"
print("🔤 Characters in string:")
for char in str1:
    print("🆎", char)

print(50 * "*")

# 🔁 RANGE FUNCTION PRACTICE

# ✅ range(stop) → prints 0 to 4
print("🔢 Range from 0 to 4:")
for i in range(5):
    print(i)

print(30 * "-")

# ✅ range(start, stop) → prints 2 to 9
print("🔢 Range from 2 to 9:")
for i in range(2, 10):
    print(i)

print(30 * "-")

# ✅ Print even numbers from 2 to 8
print("⚖️  Even numbers (2 to 8):")
for i in range(2, 10, 2):
    print(i)

print(30 * "-")

# ✅ Print odd numbers from 1 to 9
print("➖ Odd numbers (1 to 9):")
for i in range(1, 10, 2):
    print(i)
