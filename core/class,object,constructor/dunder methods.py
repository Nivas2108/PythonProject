### __getattribute__ ###
class A:
    def __init__(self,a):
        self.a=a
    def __getattribute__(self, item):
        print(item)
        return super().__getattribute__(item)
obj=A(20)
print(obj.a)

### __hash__ ###
class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __eq__(self, other):
        return self.a==other.a and self.b!=other.b
    def __hash__(self):
        return super().__hash__()
obj=A(1,3)
print(obj.a)

### __getitem__ ###
class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __getitem__(self, item):
        if item=="a":
            return self.a
        else:
            return self.b
obj=A(4,5)
print(obj.a)