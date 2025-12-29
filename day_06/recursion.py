# ✅ FUNCTION: Print numbers from n to 1 using recursion

def show(n):
    if n == 0:  # 🛑 Base case: stop when n reaches 0
        return
    print("🔢", n)     # 📥 Print before recursion
    show(n - 1)        # 🔁 Recursive call with smaller value
    print("🔚 End")     # 📤 Print after recursion (reverse order)

show(7)


# ✅ FUNCTION: Find factorial using recursion

def fact(n):
    if n == 0 or n == 1:  # 🛑 Base case: fact(0) = 1, fact(1) = 1
        return 1
    return n * fact(n - 1)  # 🔁 Recursive case: n * (n-1)!

print("🧮 Factorial of 4 =", fact(4))
