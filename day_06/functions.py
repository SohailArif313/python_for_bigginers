# ✅ FUNCTION: Add 2 numbers (with parameters and return)

def cal_sum(a, b):  # 🧮 Parameters: a, b
    result = a + b
    print(f"🧾 Sum of {a} and {b} is ➤ {result}")
    return result

# 🔁 Function calls (arguments passed)
cal_sum(2, 5)
cal_sum(8, 7)

print(40 * "-")

# ✅ FUNCTION: Print Hello

def print_hello():
    print("👋 Hello!")

print_hello()

print(40 * "-")

# ✅ FUNCTION: Calculate average of 3 marks

def cal_avg(math, chem, phy):
    total = math + chem + phy
    avg = total / 3
    print(f"📊 Average of marks ➤  {avg}")
    return avg

cal_avg(90, 80, 70)
cal_avg(90, 93, 97)

print(40 * "-")

# ✅ FUNCTION: Calculate product using default parameter

def cal_prod(a, b = 3):  # 🛠 b has default value of 3
    prod = a * b
    print(f"✖️  Product of {a} and {b} is ➤  {prod}")
    return prod

cal_prod(5, 2)     # User gives both a and b
cal_prod(7)        # Only a given, b = 3 used as default
