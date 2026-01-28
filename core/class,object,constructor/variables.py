from tkinter.font import names


class Student:
    total_students=0
    def __init__(self,name):
        self.name=name
        Student.total_students+=1
        print(f"new student has been created {self.name}.Total students={Student.total_students}")
s1=Student("Nivas")
s2=Student("nivas")
#####################################
d = {'a': 1}
k = d.keys()
d['b'] = 2
print(list(k))
#########################################
class Loan:
    interest=0.1
    def __init__(self,a,n):
        self.name=n
        self.amount=a
    def total_amount(self,x):
        return self.amount(x*(self.amount*self.interest))
    def change_interest(self,b):
        Loan.interest=b
l1=Loan('hl',10000)
l1.change_interest
####################################
class Loan:
    interest=0.1
    @classmethod
    def m1(cls,ni):
        cls.interest=ni
Loan.m1(0.2)
print(Loan.interest)
####################################
class payment:
    def __init__(self,amount):
        self.amount=amount
    @classmethod
    def upipayment(cls,a,p):
        print(f"upi payment to {p} is done")
        return cls(a)
p1=payment.upipayment(500,9121949490)
############################################
class date:
    def __init__(self,d,m,y):
        self.d=d
        self.m=m
        self.y=y
    @classmethod
    def usdateformat(cls,date):
        m,d,y=date.split("/")
        return cls(d,m,y)
d1=date.usdateformat("01/06/2026")
print(d1.d)
###########################
# Q1. Create a class Student with instance attributes name and marks.
# Add an instance method is_passed() that returns True if marks > 40.
# Then create 2 student objects and print whether each has passed or failed.
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def is_passed(self):
        if self.marks>40:
            return True
        return False
def class_marks(b):##function
    if b:
        print("passed")
    else:
        print("failed")
student1=Student("nivas",50)
student2=Student("madhu",40)
class_marks(student1.is_passed())
class_marks(student2.is_passed())

# Q2. Create a class Employee with attributes name and company_name = "TechCorp".
# Add a class method change_company(cls, new_name) to update the company name for all employees.
# Demonstrate how this change affects all instances.
class Employee:
    company_name="TechCorp"
    def __init__(self,name):
        self.name=name
    @classmethod
    def change_company(cls,new_name):
        cls.company_name=new_name
obj=Employee("nivas")
print(f"previous company {obj.company_name} {obj.name}")
obj.change_company("cvcorp")
print(f"changed company {obj.company_name} {obj.name}")

# Q3. Create a class MathOps with a static method is_even(num) that returns True if the number is even.
# Then call it both from the class and an instance.
class MathOps:
    @staticmethod
    def is_even(num):
        if num%2==0:
            return True
        return False
obj=MathOps()
print(obj.is_even(5))
# Q4. Create a class Car with:
# •	instance attribute mileage
# •	class attribute wheels = 4
# Add an instance method display_specs() that prints mileage and wheels.
# Then change wheels using a class method, and print again.
class Car:
    wheels=4
    def __init__(self,mileage):
        self.mileage=15
        self.wheels=4
    @classmethod
    def change_wheels(cls,new_wheels,new_mileage):
        cls.new_wheels=new_wheels
        cls.new_mileage=new_mileage
    def display_specs(self):
        self.mileage=25
        self.wheels=6
obj=Car("audi")
print(f"{obj.wheels} wheeler mileage is {obj.mileage}")
obj.change_wheels(2,50)
print(f"{obj.new_wheels} wheeler mileage is {obj.new_mileage}")
# Q5. Create a class Temperature with:
# •	instance attribute celsius
# •	a static method to_fahrenheit(celsius)
# •	an instance method show_conversion() that uses the static method to print both values.
class Temperature:
    def __init__(self,celsius):
        self.celsius=celsius
    @staticmethod
    def to_fahrenheit(celsius):
        celsius=celsius
    def show_conversion(self,fahrenheit):
        self.fahrenheit=fahrenheit
obj=Temperature(98)
print(obj.celsius*9/5+32)