# ✅ Python Sets: Basics, Methods, and Operations

# 🎯 Set Example: Duplicates are removed automatically
set1 = {27, 2.8, 2.9, "Hello", "World", "Hello"}  # "Hello" appears only once
print("🧺 set1 =", set1)
print("📏 Length of set1 =", len(set1))  # Length excludes duplicates


# ✅ Creating an empty set
collection = set()
print("📦 Type of collection ➤", type(collection))  # Output: <class 'set'>


# 🧩 Adding Elements to Set
collection.add(12)
collection.add(1.3)
collection.add((14, 15, 16))  # ✅ Tuples allowed (immutable)
collection.add("Hello")
collection.add("world")

# ❌ Lists can't be added because they are mutable
# collection.add([17, 18, 19])  # 🚫 Error: unhashable type: 'list'

# 🗑️ Removing an element
collection.remove("Hello")  # Removes "Hello" if it exists

# 🔄 Clear all elements from the set
collection.clear()
print("🧹 After clear(), collection =", collection)


# ✅ Set Pop Operation (Random Removal)
set2 = {"hello", "World", "Python", "coding"}
print("🎯 Random pop ➤", set2.pop())  # Removes a random element
print("🎯 Another random pop ➤",
