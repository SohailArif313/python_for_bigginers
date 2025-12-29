# ✅ Strings in Python

str1 = "Hello, world."
str2 = "I am Sohail"
finalStr = str1 + " " + str2

print("Combined string:", finalStr)
print("Length of combined string:", len(finalStr))
print("Length of str1:", len(str1))


# 🎯 Indexing

s1 = "Sohail"
print("First character:", s1[0])        # S
print("Last character:", s1[5])        # l


# 🔪 Slicing

text = "Hello, world"
print("Slice [0:5]:", text[0:5])        # Hello
print("Slice [6:len(text)]:", text[6:]) # world
print("Slice [6:]:", text[6:])          # world


# ➖ Negative Indexing

f = "Apple"
print("Negative slice [-3:-1]:", f[-3:-1])  # pl


# 🧰 String Functions

str3 = "i am a coder"

print("Ends with 'er'? ->", str3.endswith("er"))         # True
print("Starts with 'I'? ->", str3.startswith("am"))      # False
print("Capitalized:", str3.capitalize())                 # i am a coder → I am a coder (only first letter capitalized)
print("Uppercase:", str3.upper())                        # I AM A CODER
print("Lowercase:", str3.lower())                        # i am a coder
print("Replace 'coder' with 'programmer':", str3.replace("coder", "programmer"))
print("Index of 'coder':", str3.find("coder"))           # 7
print("Count of 'a':", str3.count("a"))                  # 2
