# Define a Circle class to create a circle with radius r using the cinstructor
import math
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def Area(self):
        area = math.pi * (self.radius ** 2)
        print(f"The area of the circle with radius {self.radius} is: {area}")
    def Perimeter(self):
        perimeter = 2 * math.pi * self.radius
        print(f"The perimeter of the circle with radius {self.radius} is: {perimeter:.2f}")
        
c1 = Circle(5)
c1.Area()
c1.Perimeter()

# Define a Employee class wuth attributes name,role,department & salary this class has showDetail method()
# class Employee:
#     def __init__(self,name,age,role,department,salary):
#         self.name = name
#         self.age = age
#         self.role = role
#         self.department = department
#         self.salary = salary
#     def showDetail(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Role: {self.role}")
#         print(f"Department: {self.department}")
#         print(f"Salary: {self.salary}")
#         print("-" * 30)
        
# employeesDetail = []
# n = int(input("Enter number of employees: "))
# for i in range(n):
#     print(f"Enter details of employee {i+1}:")
#     name = input("Enter name: ")
#     age = int(input("Enter age: "))
#     role = input("Enter role: ")
#     department = input("Enter department: ")
#     salary = int(input("Enter salary: "))
#     empoyees =Employee(name,age,role,department,salary)
#     employeesDetail.append(empoyees)
    
# print("_"*20)
# print("Employees Detail:")
# for i,emp in enumerate(employeesDetail,start=1):
#     print("Empoyee",i)
#     emp.showDetail()
    
# # Create an Engineer class that inherits properties form Employee & and has additional attributes : name & age
# class Engineer(Employee):
#     def __init__(self, name,age):
#         super().__init__(name,age,"Engineer","IT",5500)
# print("Engineer Details:")
# engg1 = Engineer("Sohail",19)
# engg1.showDetail()

# Create a class called Order which stores item & its price
# Use Dunder function __gt__() to convey that:
#   Order1 > Order2 if Order1's price is greater than Order2's price

class Order:
    def __init__(self,items,price):
        self.items = items
        self.price = price
    def __gt__(self,order2):
        return self.price > order2.price

order1 = Order("laptop",645)
order2 = Order("phone",500)
print(order1 > order2) # True