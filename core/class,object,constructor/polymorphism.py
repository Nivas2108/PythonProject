# Q1. Create a class Animal with make_sound() and derived classes Dog, Cat, Cow that
# override it.
# Demonstrate polymorphism by iterating over a list of different animal objects and calling
# make_sound().
from abc import abstractmethod


class Animal:
    def make_sound(self):
        print(1)
class Dog(Animal):
    def make_sound(self):
        print(2)
        # super().make_sound()
class cat(Animal):
    def make_sound(self):
        print(3)
        # super().make_sound()
class cow(Animal):
    def make_sound(self):
        print(4)
        # super().make_sound()
animals = [Dog(), cat(), cow()]
for i in animals:
    i.make_sound()

# Q2. Write a function operate(device) that calls device.start().
# Pass in objects of Car, Computer, and WashingMachine — all of which define a start()
# method, but share no inheritance relationship.
# Show that Python’s polymorphism works through behavior, not type.
class car:
    def start(self):
        print("car")
class computer:
    def start(self):
        print("computer")
class washing_machine:
    def start(self):
        print("machine")
def operate(device):
    device.start()
a=car()
operate(a)

# Q3. Create a Vector class that supports:
# • + operator → add coordinates
# • == operator → compare equality
# Show how operator overloading gives natural polymorphism to user-defined classes.
class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, other):
        return self.x+other.x,self.y+other.y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
a=vector(5,5)
b=vector(5,5)
r=a+b
if a==b:
    print(r)

# Q4. Create a base class Transport with move() and derived classes Bus and Bike that
# override it but also call the parent implementation using super().
# Show the combination of reuse + custom behavior.
class Transport:
    def move(self):
        print("transport")
class bus(Transport):
    def move(self):
        print("bus",end=' ')
        super().move()
class bike(Transport):
    def move(self):
        print("bike",end=' ')
        super().move()
a=bike()
print(a.move())

# Q5. Using the abc module, create an abstract class Notification with send().
# Implement subclasses EmailNotification, SMSNotification, PushNotification — each
# with its own send() logic.
# Demonstrate polymorphism by looping over all and calling send().
from abc import ABC,abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self):
        pass
class Email_Notification(Notification):
    def send(self):
        print("Email")
class SMS_Notification(Notification):
    def send(self):
        print("SMS")
class push_Notification(Notification):
    def send(self):
        print("push")
m=[Email_Notification(),SMS_Notification(),push_Notification()]
for n in m:
    n.send()

# Q6. Design:
# • Base class Payment with process(amount)
# • Subclass CreditCardPayment adds process(amount, card_type)
# Demonstrate what happens when overriding with different signatures and how Python
# handles it.
class Payment:
    def process(self,amount):
        print(amount)
class Credit_card_payment(Payment):
    def process(self,amount,card_type):
        print(amount,card_type)
a=Payment()
a.process(20)
c=Credit_card_payment()
c.process(60,"upi")

# def feature(f):
#     def wrapper(*args):
#         print("called function")
#         f(*args)
#     return wrapper
# @feature
# def fun(x,y):
#     print(x+y)
# fun(10,20)
# fun=feature(fun)




