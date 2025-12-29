# ✅ Print numbers from 1 to 100 using for loop
print("📈 Numbers from 1 to 100:")
for i in range(1, 101):
    print(i, end=" ")
print("\n" + 50 * "*")


# ✅ Print numbers from 100 to 1 using for loop
print("📉 Numbers from 100 to 1:")
for i in range(100, 0, -1):
    print(i, end=" ")
print("\n" + 50 * "*")


# ✅ Print multiplication table of a number
n = int(input("🔢 Enter a number to print its multiplication table: "))
print(f"📊 Multiplication Table of {n}")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
print(50 * "*")


# ✅ Pass statement in for loop
# Pass is used as a placeholder — it does nothing but avoids error

for i in range(1, 11):
    pass  # 🔒 Placeholder: Loop is intentionally left empty

print("✅ I am Sohail — Code after loop is still executed.")
