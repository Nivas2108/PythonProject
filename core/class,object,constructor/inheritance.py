# • Create a base class Animal with a method sound(). Create a derived class Dog
# that overrides the sound() method. Demonstrate method overriding.
class Animal:
    def sound(self):
        print("animal")
class Dog(Animal):
    def sound(self):
        print("barks")
obj = Dog()
obj.sound()

#  Create class A with method show(). Create class B(A) that overrides show() and
# also calls the parent method using super()
class A:
    def show(self):
        print("method A ")
class B(A):
    def show(self):
        super().show()
        print("method B")
a=B()
a.show()

#  Create multi-level inheritance with classes A → B → C, each having a method
# display() printing the class name. Create object of C and call display(),
# showing method resolution.
class A:
    def display(self):
        print("A")
class B(A):
    pass
class C(B):
    pass
obj = C()
obj.display()
# Implement hierarchical inheritance using a base class Vehicle and two child
# classes Car and Bike, each defining a method wheels().
class vehicle:
    def wheels(self):
        print("vehicle class")
class car(vehicle):
    def wheels(self):
        print("car class")
class bike(vehicle):
    def wheels(self):
        print("bike class")
a=bike()
a.wheels()
b=car()
b.wheels()
# Create class Employee with an instance method salary(). Create class
# Manager(Employee) that overrides salary() and adds an incentive. Demonstrate
# both outputs.
class employee:
    def salary(self,sal):
        sal=20
        print(sal)
class manager(employee):
    def salary(self,inc):
        inc+=30
        print(inc)
a=manager()
a.salary(4)
b=employee()
b.salary(7)
# Create class University with a class variable and a class method. Inherit it
# into class College and access the parent’s class variable from the child class
class university:
    c=0
    @classmethod
    def op(cls,c):
        c+=20
        print(c)
class college(university):
    pass
n=college()
n.op(4)
# Create class MathOps with a static method add(a, b). Create class
# AdvancedOps(MathOps) and use the static method without overriding it.
class mathops:
    @staticmethod
    def add(a,b):
        a=a
        b=b
        print(a+b)
class advanced_mathops(mathops):
    pass
obj=advanced_mathops()
obj.add(1,6)
# Create two classes Father and Mother, both defining a method skills(). Create
# class Child(Father, Mother) and check which skills() runs using MRO.
class father:
    def skills(self):
        print("father")
class mother:
    def skills(self):
        print("mother")
class child(father,mother):
    pass
obj=child()
obj.skills()
print(child.mro())
# Create class Person with a constructor __init__(name). Create class
# Student(Person) with constructor __init__(name, roll). Use super() to call the
# parent constructor
class person:
    def __init__(self,name):
        self.name=name
class student(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll=roll
i=student("nivas",45)
print(i.name)
