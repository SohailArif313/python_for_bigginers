# ✅ Create & Write a File: practice.txt

# with open("practice.txt", "w") as file:
#     file.write("Hi everyone\n")
#     file.write("We are learning file I/O\n")
#     file.write("Using java\n")
#     file.write("I like programming in java\n")

# print("📄 File 'practice.txt' created and data added!\n")


# ✅ Replace all occurrences of "java" with "python"

# with open("practice.txt", "r") as file:
#     data = file.read()

# data = data.replace("java", "python")

# with open("practice.txt", "w") as file:
#     file.write(data)

# print("🔄 Replaced 'java' with 'python' in file.\n")


# ✅ Check if a word exists in the file

# def check_for_word(word):
#     with open("practice.txt", "r") as file:
#         data = file.read()
#         if word in data:
#             print(f"✅ Word '{word}' found in file.")
#         else:
#             print(f"❌ Word '{word}' not found in file.")

# check_for_word("sohail")
# check_for_word("learning")

# print()


# ✅ Find first line number containing a specific word

def find_word_in_line(word):
    with open("practice.txt", "r") as file:
        line_no = 1
        for line in file:
            if word in line:
                print(f"🔍 Word '{word}' found on line {line_no}")
                return
            line_no += 1
        print(f"⚠️ Word '{word}' not found in any line.")
        return -1

find_word_in_line("like")
find_word_in_line("hello")

print()


# ✅ Count even numbers from a comma-separated file (numbers stored in text)

# Simulate writing comma-separated numbers to file
# with open("practice.txt", "w") as file:
#     file.write("2,3,5,6,8,9,10,13,15,22")

# # Read and count even numbers
# count = 0
# with open("practice.txt", "r") as file:
#     data = file.read()
#     nums = data.split(",")

#     for val in nums:
#         if int(val) % 2 == 0:
#             count += 1

# print(f"🔢 Even numbers count: {count}")
