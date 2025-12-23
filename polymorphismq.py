# Q1. Create a class Animal with make_sound() and derived classes Dog, Cat, Cow that
# override it.
# Demonstrate polymorphism by iterating over a list of different animal objects and calling
# make_sound().
class animal:
    def make_sound(self):
        print("animal in X")
class dog(animal):
    def make_sound(self):
        print("dog in X")
class cat(animal):
    def make_sound(self):
        print("cat in X")
class cow(animal):
    def make_sound(self):
        print("cow in X")
def calling_make_sound(x):
    x.make_sound()
obj=animal()
obj1=dog()
obj2=cat()
calling_make_sound(obj)
calling_make_sound(obj1)
calling_make_sound(obj2)


# Q2. Write a function operate(device) that calls device.start().
# Pass in objects of Car, Computer, and WashingMachine — all of which define a start()
# method, but share no inheritance relationship.
# Show that Python’s polymorphism works through behavior, not type.
class car:
    def start(self):
        print("car started")
class computer:
    def start(self):
        print("computer started")
class WashingMachine:
    def start(self):
        print("Washing Machine started")
def operate(device):
    device.start()
obj=computer()
obj.start()
obj1=WashingMachine()
obj1.start()
obj2=car()
obj2.start()


# Q3. Create a Vector class that supports:
# • + operator → add coordinates
# • == operator → compare equality
# Show how operator overloading gives natural polymorphism to user-defined classes.

class vector :
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return self.x+other.x+self.y+other.y
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y

v1=vector(1,2)
v2=vector(3,4)
print(v1+v2)
print(v1==v2)


# Q4. Create a base class Transport with move() and derived classes Bus and Bike that
# override it but also call the parent implementation using super().
# Show the combination of reuse + custom behavior.
class transport:
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def move(self):
        print("transport is good for travelling")
class bus(transport):
    def __init__(self,start,end,repair):
        super().__init__(start,end)
        self.repair=repair
    def move(self):
        print("bus is a public transport")
class bike(transport):
    def __init__(self,start,end,repair,reach):
        super().__init__(start,end)
        self.reach=reach
    def move(self):
        print("bike riding is adventurous")
obj=transport(1,2)
obj.move()
obj1=bus(1,2,2)
obj1.move()
obj2=bike(4,6,6,8)
obj2.move()

# Q6. Design:
# • Base class Payment with process(amount)
# • Subclass CreditCardPayment adds process(amount, card_type)
# Demonstrate what happens when overriding with different signatures and how Python
# handles it.

class payment_with_process:
    def __init__(self,amount):
        self.amount=amount
    def pay(self):
        print("payment is done")
class Creditcardpayment_adds_process(payment_with_process):
    def __init__(self,amount,card_type):
        super().__init__(amount)
        self.card_type=card_type
    def pay(self):
        print("card payment is done")
obj=Creditcardpayment_adds_process(10000,"debit card")
obj.pay()
obj1=Creditcardpayment_adds_process(28000,"credit card")
obj1.pay()
obj2=payment_with_process(6000)
obj2.pay()


# Q7. Create:
# • Class Sorter with change(strategy) method. Separate strategy classes: BS, MS, QS,
# each implementing a different logic method.
# Demonstrate how polymorphism can be achieved without inheritance by using
# interchangeable strategy objects.

class sorter:
    def __init__(self,strategy):
        self.strategy=strategy




















# Q8. Create:
# • Base Account → withdraw()
# • Subclass SavingsAccount → modifies withdraw()
# • Subclass PremiumSavingsAccount → overrides again but calls parent using super()
# Show how polymorphism works across multiple levels.
class account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def withdraw(self,balance):
        self.balance=balance
        print("Account withdrawn")
class savingsAccount(account):
    def __init__(self,name,balance,savings):
        super().__init__(name,balance)
        self.savings=savings
    def withdraw(self,savings):
        self.savings-=savings
        print("savingsAccount withdrawn")
class PremiumSavingsAccount(account):
    def __init__(self,name,balance,premium,savings):
        super().__init__(name,balance)
        self.premium=premium
        print("Premium Savings Account withdrawn")
obj=account(name="nivas",balance=10000)
obj.withdraw(100)
obj1=savingsAccount(name="tyson",balance=10000,savings=10000)
obj1.withdraw(100)
obj2=PremiumSavingsAccount(name="tyson",balance=10000,savings=10000,premium=100000)
obj2.withdraw(100)




# Q9. Create a function draw(shape) that works for objects of classes Circle, Square, and
# Rectangle,
# each implementing a draw() method.
# Add another unrelated class Car with draw() and pass it — what happens and why?

class circle:
    def __init__(self,radius):
        self.radius=radius
    def draw(self):
        print("circle is round")
class Square(circle):
    def __init__(self,radius,side):
        super().__init__(radius)
        self.side=side
    def draw(self):
        print("square is like a box")
class rectangle(circle):
    def __init__(self,radius,length,side):
        super().__init__(radius)
        self.length=length
    def draw(self):
        print("rectangle is like a rectangle")
class car:

    def draw(self):
        print("car is rich")
def draw(shape):
    shape.draw()
obj=car()
obj.draw()
obj1=Square(3,4)
obj1.draw()
obj2=rectangle(3,4,5)
obj2.draw()

# Q10. Design a polymorphic system for payment handling (UPI, Card, Cash) — all have a
# pay() method.
# Now implement a version that checks types explicitly using isinstance() before calling
# pay().
# Compare both designs and explain why one breaks the spirit of polymorphism.

