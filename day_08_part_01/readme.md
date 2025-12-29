# 📘 Python Beginner Project – Day 8 (Part 1)

## 📝 Topics Covered
Day 8 (Part 1) introduces **Object-Oriented Programming (OOP) in Python**, focusing on **classes, objects, abstraction, encapsulation, constructors, and attributes**.

---

## 1️⃣ Abstraction
- **Definition:** Abstraction is the process of **hiding internal implementation details** of a class and only showing the **essential features** to the user.  
- **Example Use Case:** A `Car` class may have methods to start or stop the car, but the user does not need to know **how the engine or clutch works internally**.  

**Key Points:**
- Provides **simplicity** and reduces complexity for users.
- Only exposes necessary methods and properties.

---

## 2️⃣ Encapsulation
- **Definition:** Encapsulation is **wrapping data (attributes) and methods (functions) into a single unit**, i.e., an object.  
- Protects internal object data from **unintended modification**.  
- Usually involves **private attributes** and **getter/setter methods** for controlled access.  

**Key Points:**
- Helps maintain **data integrity**.  
- Combines **state (attributes)** and **behavior (methods)** in one place.

---

## 3️⃣ Classes and Objects
- **Class:** Blueprint or template for creating objects.  
- **Object:** Instance of a class that holds **data and behavior** defined in the class.  

**Example:**
- `Student` class defines attributes like `name`, `age`, and `grade`.  
- Objects are created for each student and stored in a list for further operations.

---

## 4️⃣ Constructors
- **Default Constructor:** Automatically called when an object is created, with **no parameters**.  
- **Parameterized Constructor:** Accepts **parameters** to initialize an object's attributes.  

**Key Points:**
- `__init__` method is the constructor in Python.  
- Allows setting **initial state** of objects at creation.

---

## 5️⃣ Attributes
- **Class Attributes:** Shared across all instances of the class.  
  - Example: `college_name` is the same for all students.  
- **Instance Attributes:** Unique to each object.  
  - Example: `name`, `age`, `grade` differ for each student.  

**Key Points:**
- Use class attributes for **common data**.  
- Use instance attributes for **object-specific data**.

---

## 6️⃣ Static Methods
- **Definition:** Methods that belong to the class rather than an instance.  
- Defined using the `@staticmethod` decorator.  
- Can be called **without creating an object**.  

**Use Case in Day 8:** A `hello()` method that prints a greeting without needing a student object.

---

## 💡 Key Takeaways
- OOP allows **modular, reusable, and organized code**.  
- **Abstraction** hides unnecessary details and simplifies usage.  
- **Encapsulation** protects data and groups attributes & methods.  
- **Constructors** help initialize objects with specific values.  
- **Class vs Instance Attributes:** Class attributes are shared; instance attributes are unique.  
- **Static methods** can be called without object creation.  

---