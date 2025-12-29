# 📚 Lists in Python

st_data = ["Sohail", 19, "Pakistan"]
print("📦 Type of st_data ➤", type(st_data))

print("Original list:", st_data)                    # ['Sohail', 19, 'Pakistan']
print("Length of list:", len(st_data))              
print(type(st_data))
# 🎯 Indexing
print("First element:", st_data[0])                
print("Second element:", st_data[1])            
print("Third element:", st_data[2])                

# 📝 Modifying list
st_data[0] = "Haris"
print("After changing first element:", st_data)    
# 🔪 Slicing
print("Slice [0:2]:", st_data[0:2])                
print("Slice [:2]:", st_data[:2])                  
print("Slice [-1:]:", st_data[-1:])    
print("Slice [-3:-1]:", st_data[-3:-1])       

# 🧰 List methods
l = [1, 2, 3, 4, 5]
l.append(6)                                        # [1, 2, 3, 4, 5, 6]
l.sort()                                         # Sorts the list (in-place)
l.sort(reverse=True)                            # Sorts in reverse (in-place)
l.reverse()                                     # Reverses the list (in-place)

l.insert(2, 5)                                     # Inserts 5 at index 2
l.remove(5)                                        # Removes first occurrence of 5
l.pop(2)                                           # Removes element at index 2

print("Final list:", l)
