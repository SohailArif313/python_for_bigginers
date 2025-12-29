# ✅ Write Mode: "w" ➤ creates file if not exist, overwrites if exist
f = open("demo.txt", "w")
f.write("Hello bro\n")
f.close()

# ✅ Read Mode: "r" ➤ throws error if file not found
f = open("demo.txt", "r")
print("📖 Full content:\n", f.read())  # Must read before readline
f.close()

# ✅ Readline Example (1 line at a time)
f = open("demo.txt", "r")
print("📄 First Line:", f.readline())
print("📄 Second Line:", f.readline())  # Will be empty if only 1 line exists
f.close()

# ✅ Append Mode: "a" ➤ adds at end, doesn't overwrite
f = open("demo.txt", "a")
f.write("My name is Sohail\nI am 19 years old\n")
f.close()

# ✅ r+ Mode: Read & Write ➤ overwrites from start
f = open("demo.txt", "r+")
f.write("How are you?\n")     # Overwrites initial part
print("🧾 Content after r+ write:\n", f.read())  # Remaining file
f.close()

# ✅ w+ Mode: Write & Read ➤ truncates file
f = open("demo.txt", "w+")
f.write("This is w+ mode!\n")
f.seek(0)  # Move cursor to beginning
print("🧾 Content after w+:\n", f.read())
f.close()

# ✅ a+ Mode: Append & Read ➤ writes at end, can read entire file
f = open("demo.txt", "a+")
f.write("Appended using a+ mode!\n")
f.seek(0)
print("🧾 Content after a+:\n", f.read())
f.close()

# ✅ Using 'with' ➤ safer (auto close)
with open("demo.txt", "a+") as f:
    f.write("Written inside with block!\n")
    f.seek(0)
    print("🧾 With block read:\n", f.read())

# ✅ Create new file (if doesn't exist)
with open("sample.txt", "w") as f:
    f.write("🔹 This is a new file created with write mode.")

# ✅ Delete a file using os module
import os
if os.path.exists("demo.txt"):
    os.remove("demo.txt")
    print("🗑️ demo.txt deleted!")
else:
    print("❌ File not found to delete.")
