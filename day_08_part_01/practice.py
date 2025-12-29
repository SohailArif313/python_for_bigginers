# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average 
# class Student:
#     def __init__(self ,name ,marks):
#         self.name = name
#         self.marks = marks
#     def averageMarks(self):
#         sum = 0
#         for val in self.marks:
#             sum+=val
#         print(f"hi {self.name} your avg score is: {sum/3}")
    
# n = int(input("Enter the number of students: "))
# for i in range(n):
#     name = input("Enter the name of the student: ")
#     marks = list(map(int,input("Enter the marks of 3 subjects: ").split()))
#     student = Student(name,marks)
    
    
# Overall work in the form of project: 
# Creat Account class with 2 attributes - balance & account no
# Create methods for debit,credit & printing the balance

from datetime import datetime
class Account:
    def __init__(self,name,age,balance,account_no):
        self.name = name
        self.age = age
        self.balance = balance
        self.account_no = account_no
    def debit(self, amount):
        if amount > self.balance:
            print("❌ Insufficient balance")
        else:
            self.balance -= amount
            print(f"✅ Debited Rs.{amount} from your account")
            print(f"💰 Your new balance is Rs.{self.balance}")
    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"was credited")
        print(f"Credited {amount} from your account\nYour new balance is {self.balance}")
    def get_balance(self):
        return self.balance
    
now = datetime.now()
currTime = now.strftime("%H:%M:%S")
customers = int(input("Enter the number of customers: "))
accounts = []
for i in range(customers):
    print(f"customer {i+1}")
    name = input("Enter the name of the customer: ")
    age = int(input("Enter the age of the customer: "))
    balance = int(input("Enter the balance of the customer: "))
    account_no = int(input("Enter the account number of the customer: "))
    acc = Account(name,age,balance,account_no)
    accounts.append(acc)
    
print("Customers Details:")
for i,acc in enumerate(accounts,start=1):
    print(f"Customer {i}")
    print(f"Name: {acc.name}")
    print(f"Age: {acc.age}")
    print(f"Balance: {acc.balance}")
    print(f"Account No: {acc.account_no}")
    
    choice = int(input("Do you want to perform any operation on the customer? 1.Yes 2.No"))
    if choice == 1:
        print("1.Credit\n2.Debit\n3.Print Balance")
        choice1 = int(input("Enter your choice: "))
        if choice1 == 1:
            amount = int(input("Enter the amount to be credited: "))
            acc.credit(amount)
            print(f"Transaction time {currTime}")
        elif choice1 == 2:
            amount = int(input("Enter the amount to be debited: "))
            acc.debit(amount)
            print(f"Transaction time {currTime}")
        elif choice1 == 3:
            print(f"Balance of customer {i} is {acc.get_balance()}")
        else:
            print("Invalid choice")
            print("thanks for banking with us")