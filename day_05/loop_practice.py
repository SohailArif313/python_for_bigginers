# ✅ Print numbers from 1 to 100
print("📈 Numbers from 1 to 100:")
i = 1
while i <= 100:
    print(i, end=" ")
    i += 1

print("\n" + 50 * "*")

# ✅ Print numbers from 100 to 1
print("📉 Numbers from 100 to 1:")
i = 100
while i >= 1:
    print(i, end=" ")
    i -= 1

print("\n" + 50 * "*")

# ✅ Multiplication Table
n = int(input("🔢 Enter a number for table: "))
print(f"🧮 Multiplication Table of {n}:")
i = 1
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1

print(50 * "*")

# ✅ Print elements of a list using while loop
l = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print("📦 List elements using while loop:")
i = 0
while i < len(l):
    print(l[i])
    i += 1

print(50 * "*")

# ✅ Search for a number using while loop (with break)
l2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 49
i = 0
print(f"🔍 Searching for {x} in list using while loop:")
while i < len(l2):
    if x == l2[i]:
        print(f"✅ Number found at index {i}")
        break
    else:
        print("⏳ Finding...")
    i += 1

print(50 * "*")

# ✅ Print odd numbers from 1 to 100
print("🔢 Odd Numbers from 1 to 100:")
i = 1
while i <= 100:
    if i % 2 == 1:
        print(i, end=" ")
    i += 1

print("\n" + 50 * "*")

# ✅ Print list using for loop
print("📦 List elements using for loop:")
for num in l:
    print(num)

print(50 * "*")

# ✅ Search for a number in list using for loop
l2 = [1, 4, 9, 16, 25, 36, 49, 64, 4, 81, 100]
x = 4
print(f"🔍 Searching for {x} in list using for loop:")
for idx in range(len(l2)):
    if l2[idx] == x:
        print(f"✅ {x} found at index {idx}")

print(50 * "*")

# ✅ Sum of first n numbers using while loop
n = int(input("➕ Enter a number to find sum till n: "))
i = 0
total_sum = 0
while i <= n:
    total_sum += i
    i += 1
print(f"🧮 Total sum = {total_sum}")

print(50 * "*")

# ✅ Factorial of n using for loop
n = int(input("✖️ Enter a number to find factorial: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"📦 Factorial of {n} = {fact}")
