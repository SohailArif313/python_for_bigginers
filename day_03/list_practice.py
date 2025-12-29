# ✅ Program 1: Store 3 Favourite Movies in a List

print("🎬 Favourite Movies Collector")
movies = []
movie1 = input("Enter your favourite first movie name: ")
movies.append(movie1)
movie2 = input("Enter your favourite second movie name: ")
movies.append(movie2)
movie3 = input("Enter your favourite third movie name: ")
movies.append(movie3)

print("\n📽️ Your Favourite Movies List:", movies)


# ✅ Program 2: Check if a List is a Palindrome

print("\n🔁 Palindrome Checker for Lists")

# You can test any of these:
list1 = [1, 2, 3, 2, 1]
list2 = [1, 2, 3]
list3 = ["m", "a", "m"]

# Choose the list you want to test:
test_list = list3  # 👈 change to list1 or list2 if you want

# Create a reversed copy
reversed_list = test_list.copy()
reversed_list.reverse()

# Check if palindrome
if test_list == reversed_list:
    print("✅ Yes, the list is a palindrome!")
else:
    print("❌ No, the list is not a palindrome.")
