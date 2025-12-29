# 📘 Python Beginner Project – Day 7

## 📝 Topics Covered
Day 7 focuses on **File Handling in Python**, which is essential for **storing, reading, and manipulating data in external files**.

---

## 1️⃣ File Modes
Python provides multiple modes to work with files:

| Mode | Description |
|------|-------------|
| `"r"` | Read mode. Opens file for reading. Throws error if file does not exist. |
| `"w"` | Write mode. Creates file if it doesn't exist. Overwrites if file exists. |
| `"a"` | Append mode. Adds new content at the end without overwriting. |
| `"r+"` | Read & Write. Can read and overwrite from the start. |
| `"w+"` | Write & Read. Truncates the file first (empties it) before writing. |
| `"a+"` | Append & Read. Adds at the end and allows reading the entire file. |

---

## 2️⃣ Reading from Files
- **`read()`** → Reads the **entire content** of the file.  
- **`readline()`** → Reads **one line at a time**.  
- **`readlines()`** → Reads all lines into a **list of strings**.  

**Use Case:** Read content of a file sequentially or line by line.

---

## 3️⃣ Writing to Files
- **`write()`** → Writes a string to a file.  
- Overwrites the content in `"w"` mode.  
- Adds content at the end in `"a"` mode.  

**Use Case:** Store data, logs, or output results into a text file.

---

## 4️⃣ Using `with` Statement
- Syntax: 
  ```python
  with open("file.txt", "mode") as f:
      # operations
