# 🐍 Day 3 – Lists & Tuples in Python

Welcome to **Day 3** of my Python learning journey!  
Today, I explored two of the most important data structures in Python — **Lists** and **Tuples**.  
These help us store multiple values in a single variable and perform operations efficiently.

---

## 📘 Topics Covered

### 🔹 Lists
- Creating and printing lists  
- Checking list type and length  
- Accessing elements using **indexing**  
- Modifying list elements  
- Performing **slicing operations**  
- Using common **list methods** like:
  - `append()`
  - `insert()`
  - `remove()`
  - `pop()`
  - `sort()` / `reverse()`

### 🔹 Tuples
- Understanding the difference between `(2)` and `(2,)`
- Creating tuples with multiple data types
- Accessing elements via **indexing & slicing**
- Using tuple methods:
  - `count()`
  - `index()`

---

## 💻 Example Code
```python
st_data = ["Sohail", 19, "Pakistan"]
print("📦 Type of st_data ➤", type(st_data))
print("Original list:", st_data)
print("Length of list:", len(st_data))

# Indexing
print("First element:", st_data[0])

# Modify list
st_data[0] = "Haris"
print("After change:", st_data)

# List methods
l = [1, 2, 3, 4, 5]
l.append(6)
l.insert(2, 5)
l.remove(5)
l.pop(2)
print("Final list:", l)

# Tuple example
tup = (2)
print("Type of tup ➤", type(tup))

tup1 = (2,)
print("Type of tup1 ➤", type(tup1))

tup2 = ("Sohail", 1, True)
print(tup2[1:])
print(tup2.count(1))
print(tup2.index(True))
