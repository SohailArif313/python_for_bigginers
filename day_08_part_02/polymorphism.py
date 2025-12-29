# Polymorphism:Operator Overloading
# When the same operator is allowed to have different meaning acccordding to the context

class Complex():
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def showNumber(self):
        print(f"{self.real}i + {self.img}j")
    def __add__(self,num2):
        newReal = self.real+num2.real
        newImg = self.img+num2.img
        return Complex(newReal,newImg)
    def __sub__(self,num2):
        newReal = self.real-num2.real
        newImg = self.img-num2.img
        return Complex(newReal,newImg)
    def __mul__(self,num2):
        newReal = self.real*num2.real
        newImg = self.img*num2.img
        return Complex(newReal,newImg)
    def __mod__(self,num2):
        newReal = self.real%num2.real
        newImg = self.img%num2.img
        return Complex(newReal,newImg)
num1 = Complex(5,2)
num1.showNumber()
num2 = Complex(2,1)
num2.showNumber()
num3 = num1%num2
print(7*"=")
num3.showNumber()
# Add two complex numbers