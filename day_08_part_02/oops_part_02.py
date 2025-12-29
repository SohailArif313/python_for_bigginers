# Use of del keyword
# class student:
#     def __init__(self, name):
#         self.name = name
        
# s1 = student("Sohail")
# del s1
# print(s1) # Output: Error

# Private(like) attribute & methods 

# class Account:
#     def __init__(self, acc_no,acc_pas):
#         self.acc_no = acc_no
#         self.__acc_pas = acc_pas
#     def reset_pass(self):
#         print(self.__acc_pas) 
# s1 = Account(1234,"Abc")
# s1.reset_pass()

# important note:Remember that if we make a private attr then we cannot use it outof class but the method internelly can use it.
class Person:
   __name = "Sohail"
   def __hello(self):
       print("Hello person!")
   def welcome(self):
       self.__hello()
   
s1 = Person()
# s1.__hello() # Output: Error
s1.welcome() # Output: Hello person!