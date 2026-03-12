# 11. Using abc module:
# • Create an abstract class Shape with area(), perimeter()
# • Implement Circle, Rectangle, Triangle
# Demonstrate:
# • why base class should NOT contain calculation logic
# • what happens if a subclass fails to implement one of the methods
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass
# class Circle(Shape):
#     def area(self):
#         print("circle area")
#     def perimeter(self):
#         print("circle peri")
# class Rectangle(Shape):
#     def area(self):
#         print("Rectangle area")
#     def perimeter(self):
#         print("Rectangle peri")
# class Triangle(Shape):
#     def area(self):
#         print("Triangle area")
#     def perimeter(self):
#         print("Triangle peri")
# a=[Circle(),Rectangle(),Triangle()]
# for i in a:
#     # i.area()
#     i.perimeter()

# 12. Design an abstract class PaymentGateway with:
# • authenticate()
# • pay(amount)
# • refund(amount)
# Implement subclasses:
# • UPIPayment
# • CardPayment
# • NetBankingPayment
# from abc import ABC, abstractmethod
# class paymentGateway:
#     def __init__(self,amount):
#         self.amount=amount
#     @abstractmethod
#     def authenticate(self):
#         print("Authentication")
#     @abstractmethod
#     def pay(self,amount):
#         self.amount=200
#         print(self.amount)
#     @abstractmethod
#     def refund(self,amount):
#         self.amount+=amount
#         print(self.amount)
# class UPIPayment(paymentGateway):
#     def authenticate(self):
#         print("upi authentication")
#     def pay(self,amount):
#         print("payed via upi")
#     def refund(self,amount):
#         print("refunded via upi")
# class card_payment(paymentGateway):
#     def authenticate(self):
#         print("card authentication")
#     def pay(self,amount):
#         print("payed via card")
#     def refund(self,amount):
#         print("refunded via card")
# class net_banking(paymentGateway):
#     def authenticate(self):
#         print("net banking authentication")
#     def pay(self,amount):
#         print("payed via net banking")
#     def refund(self,amount):
#         print("refunded via net banking")
# a=paymentGateway(500)
# a.refund(300)
# a.pay(300)
# a.authenticate()

# 13. Create:
# • Abstract class VehicleControl with methods accelerate(), brake(), steer()
# • Implement CarControl, BikeControl, TruckControl
# Demonstrate calling each through a single interface.
# from abc import ABC ,abstractmethod
# class Vehicle_control:
#     @abstractmethod
#     def accelerate(self):
#         print("accelerating")
#     @abstractmethod
#     def brake(self):
#         print("breaks applied")
#     @abstractmethod
#     def steer(self):
#         print("using steering")
# class Car_control(Vehicle_control):
#     def accelerate(self):
#         print("Car accelerates")
#     def brake(self):
#         print("breaks applied to car")
#     def steer(self):
#         print("using car steering")
# class bike_control(Vehicle_control):
#     def accelerate(self):
#         print("bike accelerates")
#     def brake(self):
#         print("breaks applied to bike")
#     def steer(self):
#         print("bike doesn't have steering")
# class Truck_control(Vehicle_control):
#     def accelerate(self):
#         print("truck accelerates")
#     def brake(self):
#         print("breaks applied to truck")
#     def steer(self):
#         print("using truck steering")
# n=Vehicle_control()
# n.accelerate()
# n.brake()
# n.steer()


# 14. Create an abstract class DatabaseDriver with:
# • connect()
# • execute(query)
# • close()
# Implement concrete drivers:
# • MySQLDriver
# • PostgresDriver
# • SQLiteDriver
from abc import ABC,abstractmethod
class Database_driver:
    @abstractmethod
    def connect(self):
        print("database connected")
    @abstractmethod
    def execute(self,query):
        self.query="john"
        print(self.query)
    @abstractmethod
    def close(self):
        print("database closed")
class SQL_driver(Database_driver):
    def connect(self):
        print("sql driver connected")
    def execute(self,query):
        print(self.query)
    def close(self):
        print("sql driver closed")
class PostgresDriver(Database_driver):
    def connect(self):
        print("Postgres driver connected")
    def execute(self,query):
        print(self.query)
    def close(self):
        print("Postgres driver closed")
class SQLiteDriver(Database_driver):
    def connect(self):
        print("SQLite driver connected")
    def execute(self,query):
        print(self.query)
    def close(self):
        print("SQLite driver closed")
r=SQL_driver()
r.connect()
r.close()
