# 📘 Python Beginner Project – Day 8 (Part 2)

## 📝 Topics Covered
Day 8 (Part 2) continues **Object-Oriented Programming (OOP)** with **Inheritance, Class Methods, Property Decorators, Polymorphism, Private Attributes, and Object Deletion**.

---

## 1️⃣ Inheritance
- **Definition:** When a class (child/derived) acquires the **properties and methods** of another class (parent/base), it is called inheritance.  
- **Purpose:** Reuse existing code and create a hierarchy of classes.  

### Types of Inheritance:
1. **Single Inheritance:** Child inherits from one parent class.  
2. **Multi-Level Inheritance:** Class hierarchy chain (grandparent → parent → child).  
3. **Multiple Inheritance:** Child inherits from **multiple parent classes**.  

**Key Points:**
- Inheritance allows **code reuse and modular design**.  
- Use the `super()` function to **call parent class methods or constructors**.

---

## 2️⃣ Class Methods
- **Definition:** Methods that are bound to the class rather than an instance.  
- Declared using the `@classmethod` decorator.  
- First parameter is `cls` (class itself).  

**Comparison with Static Methods:**  
- Static methods (`@staticmethod`) cannot access class or instance data.  
- Class methods can access/modify class attributes.  

---

## 3️⃣ Property Decorator
- **Definition:** `@property` allows methods to be accessed like attributes.  
- Useful for **calculated values** or controlling access to attributes.  

**Example Use Case:** Calculating **percentage from marks** without calling a method explicitly.

---

## 4️⃣ Polymorphism
- **Definition:** Ability of the same operator or function to behave differently based on context.  
- **Operator Overloading:** Using special methods (`__add__`, `__sub__`, `__mul__`, `__mod__`) to define **custom behavior for operators**.  
- Promotes **flexibility and readability** in code.

---

## 5️⃣ Private Attributes and Methods
- **Definition:** Attributes/methods prefixed with double underscore (`__`) are **private to the class**.  
- They **cannot be accessed directly** from outside the class.  
- Private methods can still be used **internally by class methods**.  

**Key Points:**
- Helps **protect sensitive data** like passwords or account numbers.  
- Promotes **encapsulation** in OOP.

---

## 6️⃣ Deleting Objects
- Use the **`del` keyword** to delete an object.  
- Once deleted, accessing the object will raise an error.  

**Use Case:** Freeing memory or removing objects that are no longer needed.

---

## 💡 Key Takeaways
- OOP allows **structured, reusable, and maintainable code**.  
- Inheritance reduces redundancy and **establishes class hierarchies**.  
- Class methods and static methods provide **different levels of access** to class data.  
- Property decorators allow **dynamic attributes and calculated properties**.  
- Polymorphism enables **flexible operator or method behavior**.  
- Private attributes and methods ensure **data security and encapsulation**.  
- Object deletion (`del`) is useful for **resource management**.  

---
