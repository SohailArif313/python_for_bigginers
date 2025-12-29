# ✅ FUNCTION: Print the length of a list
books = ["English", "Math", "Science", "History"]
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Philadelphia"]

def print_list_length(lst):
    print("📏 Length:", len(lst))
    return len(lst)

print_list_length(cities)
print_list_length(books)

print(40 * "-")

# ✅ FUNCTION: Print all elements of a list in one line
def print_list_elements(lst):
    print("📚 Elements:", end=" ")
    for item in lst:
        print(item, end=" ")
    print()

print_list_elements(cities)
print_list_elements(books)

print(40 * "-")

# ✅ FUNCTION: Find factorial of n
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"🧮 Factorial of {n} is {fact}")
    return fact

factorial(5)
factorial(4)

print(40 * "-")

# ✅ FUNCTION: Convert USD to PKR
def usd_to_pkr(usd):
    pkr = usd * 282.88
    print(f"💵 {usd} USD = {pkr:.2f} PKR")
    return pkr

usd_to_pkr(5000)

# ✅ FUNCTION: Convert PKR to USD
def pkr_to_usd(pkr):
    usd = pkr / 282.88
    print(f"💰 {pkr} PKR = {usd:.2f} USD")
    return usd

pkr_to_usd(1414415)

print(40 * "-")

# ✅ FUNCTION: Check if a number is odd or even
def check_odd_even(n):
    if n % 2 == 0:
        print(f"{n} is Even ✅")
    else:
        print(f"{n} is Odd ❌")

check_odd_even(5)
check_odd_even(10)

print(40 * "-")

# ✅ RECURSION: Sum of first n natural numbers
def sum_natural(n):
    if n == 0:
        return 0
    return sum_natural(n - 1) + n

print(f"📊 Sum of first 6 natural numbers: {sum_natural(6)}")

print(40 * "-")

# ✅ RECURSION: Print elements of list
cities = ["Lahore", "Islamabad", "Karachi", "Faisalabad", "Multan"]

def print_list_recursive(lst, idx):
    if idx == 0:
        return
    print_list_recursive(lst, idx - 1)
    print(lst[idx - 1], end =" -> ")

print("🌍 Cities (recursively): ", end="")
print_list_recursive(cities, len(cities))
