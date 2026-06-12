class bank:
    def __init__(self,name,acc):
        self._acc=acc
        self.__pin="1234"
    def get_pin(self,password):    ##getter
        if password=="345678":
            return self.__pin
        return None
    def set_pin(self,password):   ##setter
        if password=="345678":
            a=input()
            self.__pin=a
        return None
obj=bank("teja",123)
print(obj.get_pin("345678"))

# 1.  Create a BankAccount class that stores:
# • account number
# • balance (should not be directly modifiable)
# You must:
# 1. Make the balance attribute inaccessible from outside.
# 2. Provide functions to deposit/withdraw that validate the amount.
# 3. Prevent withdrawal if balance becomes negative.
# 4. Show what happens if someone tries to modify balance directly and why
# encapsulation prevents it.
class Bank:
    def __init__(self,acc,balance):
        self.acc=acc
        self.__balance=200
    def deposit(self,cash):
        self.__balance+=cash
        print(cash)
    def withdraw(self,money):
        self.__balance-=money
        print(money)
    def get_balance(self):
        print(self.__balance)
a=Bank(1234,700)
a.deposit(2000)
a.withdraw(1000)
# a.__balance(100000)

# 2. Design a Student class where marks:
# • should always be between 0 and 100
# • should never be set directly
# Enable updating marks only through a controlled method that performs range
# checks.
# Demonstrate:
# • trying to assign marks manually
# • why encapsulation protects invalid states

class Student:
    def __init__(self,marks):
        self.__marks=0


# 3. Create a SecureFile class that:
# • stores content privately
# • provides a method read(password)
# • refuses access if the password is incorrect
# • logs an "Unauthorized attempt" internally (cannot be accessed from outside)

class SecureFile:
    def __init__(self,password,balance):
        self.__password=password
        self.__balance=balance
    def get_balance(self,password):
        if self.__password==password:
            print(self.__balance)
        else:
            print("unauthorized attempt")
a=SecureFile(1234,500)
a.get_balance(1234)
####
class SecureFile:
    def __init__(self, content, password):
        self.__content = content          # private content
        self.__password = password        # private password
        self.__log = []                   # private log
    def read(self, password):
        if password == self.__password:
            return self.__content
        else:
            self.__log.append("Unauthorized attempt")
            return "Access Denied"
# Demonstration
file = SecureFile("Secret Data: Project X", "1234")
print(file.read("1234"))   # correct password
print(file.read("1111"))   # wrong password
# 4.Design an Employee class where:
# • salary is hidden
# • outsiders cannot read salary directly
# • use getter method that logs each access attempt
# • provide a method to update salary but only if the new salary is higher (prevent
# accidental downgrade)
class Employee:
    def __init__(self,salary):
        self.__salary=salary
    def get_salary(self,salary):
            print(salary)
    def set_salary(self,salary):
        if salary > 0:
            self.__salary+=salary
            print(self.__salary)
a=Employee(40000)
a.get_salary(60000)
a.set_salary(45000)

# 5. Create a Product class where:
# • price cannot be negative
# • discount cannot exceed 70%
# • internal final price calculation should not be directly exposed
# Provide only one public method get_final_price().
class Product:
    def __init__(self,price,discount):
        self.__price=price
        self.__discount=discount
    def get_price(self):
        if self.__price<0:
            print("price cannot be negative")
        else:
            print(self.__price)
    def set_discount(self):
        if self.__discount>70:
            print("discount exceeded")
        else:
            print(self.__discount)
    def get_final_price(self):
        final_price=self.__price-(self.__price*self.__discount/100)
        print(final_price)
a=Product(5000,45)
a.get_price()
a.set_discount()
a.get_final_price()

# 6. Create a Character class with:
# • private _health
# • methods to damage(points) and heal(points)
# • health cannot drop below 0 or exceed max limit
# • expose only current health through a read-only getter
class Character:
    def __init__(self,health):
        self.__health=health
    def damage(self,damage):
        self.damage=damage
        self.__health-=self.damage
        if self.__health<=0:
            print("go to hospital")
        else:
            print("health is ok")
    def heal(self,heal):
        self.heal=heal
        self.__health+=self.heal
        if self.__health==100:
            print("healthy body")
        else:
            print("take precautions")
    def get_health(self):
        print(self.__health)
a=Character(100)
a.damage(50)
a.heal(30)
a.get_health()

# 7. Create:
# • An Engine class with private state like temperature
# • A Car class that uses an Engine but should:
# o Not allow users to manipulate engine temperature
# o Only expose methods like start_car() or cool_engine()
# Demonstrate why giving direct engine access is dangerous.
class Engine:
    def __init__(self,temperature):
        self.__temperature=temperature
# class Car(Engine):
#     def start_car(self):


# class A:
#     def __init__(self):
#         self.__x=1234
#     @property
#     def y(self):
#         return self.__x
#     @y.setter
#     def z(self,nx):
#         self.__x=nx
# obj=A()
# print(obj.y)
# obj.z=1024