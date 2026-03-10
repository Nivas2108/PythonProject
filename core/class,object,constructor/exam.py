#######2
# class Vehicle:
#     def start(self):
#         print("vehicle")
# class Car(Vehicle):
#     def start(self):
#         print("car")
# class bike(Vehicle):
#     def start(self):
#         print("BIke")
# class Generator:
#     def start(self):
#         print("generator")
# class Machine:
#     def start(self):
#         print("Machine")
# a = [Car(), bike(),Generator(),Machine()]
# for i in a:
#     i.start()
############3
# class Employee:
#     def __init__(self,salary):
#         self.__salary=salary
#         self.acc=0
#     def set(self,new_sal):
#         if new_sal>self.__salary:
#             self.__salary+=new_sal
#     def get(self):
#         self.acc+=1
#         return self.__salary,self.acc
# obj = Employee(10000)
# obj.set(11000)
# print(obj.get())
# obj.set(9000)
# print(obj.get())
############
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
class Account(Person):
    def __init__(self,name,age,gender,mail,password):
        super().__init__(name,age,gender)
        self.mail = mail
        self.password= password
class Instagram(Account):
    accounts=[]
    def __init__(self,name,age,gender,mail,password):
        super().__init__(name,age,gender,mail,password)
        Instagram.accounts.append(mail)
class Facebook(Account):
    accounts=[]
    def __init__(self,name,age,gender,mail,password):
        super().__init__(name,age,gender,mail,password)
        Facebook.accounts.append(mail)
obj1=Instagram("nivas",21,"male","67819@gmail.com",123)
obj2=Facebook(" noob",22,"male","827032984@gmail.com",456)
obj1=Instagram("niv",21,"male","6798y89@gmail.com",123)
print(Instagram.accounts)
print(Facebook.accounts)
