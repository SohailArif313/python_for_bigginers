# 📘 Dictionary Example: Student Info

info = {
    "key": "value",
    "name": "Sohail",
    "subjects": ["Python", "C++", "Java", "C"],
    "topics": ("dict", "set"),   # Tuple is hashable
    "age": 19
}

# 🔍 Accessing Dictionary Values
print("📛 Name:", info["name"])
print("📚 Subjects:", info["subjects"])


# ✏️ Updating and Adding New Keys
info["name"] = "Haris"         # Overwrites old name
info["surname"] = "Arif"       # Adds new key-value pair
print("\n📝 Updated Info:", info)


# ✅ Nested Dictionary Example
student = {
    "name": "Sohail",
    "marks": {
        "computer": 98,
        "physics": 96,
        "chemistry": 93
    }
}

# 🎯 Access Nested Value
print("\n🧪 Chemistry Marks:", student["marks"]["chemistry"])


# 🛠️ Dictionary Methods
print("\n🗂️ Keys:", list(student.keys()))       # Convert keys to list
print("📦 Values:", student.values())          # View all values

# 🔗 Pairs of key-value
pairs = list(student.items())
print("🧩 First Pair:", pairs[0])              # ('name', 'Sohail')

# 🔍 Safe Access using get()
print("🔍 Get 'name1':", student.get("name1"))  # Returns None if not found
# print(student["name1"])  # ❌ Would give error: KeyError

# ➕ Add a new key-value pair
student.update({"country": "Pakistan"})
print("\n🌍 Updated Student:", student)
