class A:
    x=0
    def __init__(self):
        self.a=1
        self.b=2
        self.c=3
obj=A()
print(obj.a)
obj1=A()
print(obj)
obj.a=10
print(obj.a)
A.x=100
obj.x=obj.x+100
print(A.x)
print(obj.x)