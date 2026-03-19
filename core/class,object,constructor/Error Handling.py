# • Create a class Person whose constructor takes age as an argument. Raise a
# ValueError if the age is less than 0.
from logging import exception
class person:
    def __init__(self,age):
        if age<0:
            raise ValueError("age is negative")
        self.age=age
try:
    a=person(-2)
    print(a.age)
except ValueError as v:
    print(v)
else:
    print("success")
# • Write a function named find_length(obj) that uses a loop to calculate the
# length of the given object without using the built-in len() function. The
# function should return the calculated length if the object is iterable. If a
# non-iterable object such as an integer is passed, the function should raise and
# handle a TypeError, and print an appropriate error message explaining what
# happens when an integer is sent as input.
def find_length(obj):
    try:
        c=0
        for i in obj:
            c+=1
        print(c)
    except TypeError:
        print("type error, not iterable")
a=100
find_length("sdbj")
find_length([12,3,3,3])
# • Create a class Student with an attribute marks. Implement a method
# set_marks(marks) that raises a ValueError if marks are not in the range 0 to
# 100.
class student:
    def __init__(self):
        self.marks=0
    def set_marks(self,marks):
        if marks<0 or marks>100:
            raise ValueError("marks are not in range")
        self.marks=marks
try:
    a=student()
    a.set_marks(100)
    print(a.marks)
except ValueError as e:
    print(e)
# • Create a custom exception named InvalidAgeError. Create a class Voter with a
# method check_eligibility(age) that raises this exception if age is less than 18.
class InvalidAgeError(Exception):
    pass
class voter:
    def check_eligibility(self,age):
        if age<18:
            raise InvalidAgeError("minor")
        else:
            print("eligible")
try:
    a=voter()
    a.check_eligibility(67)
except InvalidAgeError as i:
    print(i)
# • Create a class BankAccount with an attribute balance. Implement a method
# withdraw(amount) that raises an exception if the withdrawal amount is greater
# than the available balance.
class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def withdraw(self,amount):
        if amount>self.balance:
            raise Exception("withdrawal amount is greater than available balance")
        self.balance-=amount
        print("successful withdrawal")
try:
    a=BankAccount(5000)
    a.withdraw(5000)
except Exception as e:
    print(e)
# • Create a class PasswordValidator with a method validate(password). Raise an
# exception if the password length is less than 8 characters.
class PasswordValidator:
    def validate(self,password):
        if len(password)<8:
            raise Exception("less than 8")
        self.password=password
        print("great password")
try:
    a=PasswordValidator()
    a.validate("1234892e0")
except Exception as e:
    print(e)
# • Create a class UserInput with a method get_integer(value). Handle ValueError
# and TypeError using separate except blocks.
class UserInput:
    def get_integer(self,value):
        self.value=value
n = UserInput()
try:
    n.get_integer(int("hell0"))
    n.get_integer(int("hgl"+3))
except TypeError as t:
    print("type error")
except ValueError as v:
    print("value error")
# • Create a base class Shape with a method area() that raises
# NotImplementedError. Create a child class Rectangle that overrides and
# implements the area method.
class Shape:
    def area(self):
        raise NotImplementedError("not implemented")
class rectangle(Shape):
    def area(self):
        print("area is implemented")
r=rectangle()
r.area()
# a=Shape()
# a.area()
# • Create a class Service with a method that calls another method which raises an
# exception. Catch and handle the exception in the Service class.
class Service:
    def services(self):
        raise Exception("exception")
    def service(self):
        try:
            self.services()
        except Exception as e:
            print(e)
a=Service()
a.service()
# • Create a class Transaction with a method process() that uses try, except, and
# finally blocks to ensure a cleanup message is always printed.
class Transaction:
    def process(self,trial):
        try:
            self.trial=trial
            print(int(self.trial))
        except Exception as e:
            print(e)
        finally:
            print("success")
a=Transaction()
a.process("hello")
# • Create a class LoginSystem with a method login(password) that raises an
# exception for an incorrect password and handles the exception outside the class.
class LoginSystem:
    def __init__(self,password):
        self.password=password
    def login(self,npassword):
        if npassword!=self.password:
            raise Exception ("incorrect password")
try:
    a=LoginSystem(2345678)
    a.login(2345678)
except Exception as e:
    print(e)
else:
    print("welcome")