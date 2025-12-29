# Inheritance:
# When one class(child/drived) derives the properties & methods of another class(parent/base), it is called inheritance.
# inheritance is used to create a new class from an existing class.

# Single inheritance
# class Car():
#     @staticmethod
#     def start():
#         print("Car started...")
#     @staticmethod
#     def stop():
#         print("Car stopped")
        
# class ToyotaCar(Car):
#     def __init__(self,name,color):
#         self.name = name
#         self.color = color
        
# car1 = ToyotaCar("Fortuner","red")
# car2 = ToyotaCar("Camry","blue")
# print(car1.name,"is a",car1.color,"color car")

# Multi-level inheritance
class Car():
    @staticmethod
    def start():
        print("Car started...")
    @staticmethod
    def stop():
        print("Car stopped")
        
class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand
        
class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type
        
# car1 = Fortuner("petrol")
# car1.start()


# # Multiple inheritance

class A:
    varA = "Welcome to A class"
class B:
    varB = "Welcome to B class"
class C(A,B):
    varC = "Welcome to C class"
    

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)


# super () function
class Car:
    def __init__(self, type):
        print("Setting up car type")
        self.type = type
        self.engine = "V8"
        self.transmission = "Automatic"

    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped")


# class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)


car1 = ToyotaCar("Fortuner", "diesel")

print("Name:", car1.name)
print("Type:", car1.type)
print("Engine:", car1.engine)
print("Transmission:", car1.transmission)
car1.start()

# class methos
# A Class method is bound to the class & recieves the class as an implicit first argument.
# Note-static method can't access or modify class state & generally for utility 

class Person():
    name = "Haris"
    
    def cahngeName(self,name):
        Person.name = name  # first method
        # self.__class__.name = name # second method
    @classmethod
    def changeName(cls,name): # thirs method
        cls.name = name
        
p1 = Person()
p1.cahngeName("Sohail") 
print(p1.name) # prints: Sohail
print(Person.name) # prints: Sohail
        
        
# Property Decorator
class Student:
    def __init__ (self, math,phy,chem):
        self.math = math
        self.phy = phy
        self.chem = chem
    @property
    def percentage(self):
        return str((self.chem+self.phy+self.math)/3)+"%"
stu1 = Student(98,97,93)
stu1.phy = 86
stu1.math = 20
print(stu1.phy)
print(stu1.percentage) # prints: 92.33333333333333%