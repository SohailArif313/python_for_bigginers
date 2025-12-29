# class student:
#     name = "sohail"
    
# s = student()
# print(s.name)  # Output: name

# Default construcctors
# class Student:
#     def __init__(self):
#         pass
    

# paramiterized constructor
class Student:
    college_name = "ABC"    # class attribute

    def __init__(self, name, age, grade):
        self.name = name    # instance attributes
        self.age = age
        self.grade = grade

    @staticmethod
    def hello():
        print("Hello")


# Step 1: Create list to store student objects
students = []

n = int(input("Enter number of students: "))
for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    age = int(input(f"Enter age of student {i+1}: "))
    grade = input(f"Enter grade of student {i+1}: ")
    
    student = Student(name, age, grade)
    students.append(student)   # store in list

print("\n", 50 * "-")

# Step 2: Print all students
print("📚 All Students Info:")
print(f"🏫 College Name: {Student.college_name}")
for i, student in enumerate(students, start=1):
    print(f"\nStudent {i}")
    print(f"Name: {student.name}")
    print(f"Age: {student.age}")
    print(f"Grade: {student.grade}")

    


  