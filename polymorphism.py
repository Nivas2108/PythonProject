# class A:
#     def m1(self):
#         print("m1 in A")
# class B(A):
#     def m1(self):
#         print("m1 in B")
#         super().m1()
# obj=A()
# obj.m1()
# obj1=B()
# obj1.m1()
#
##########################################################

class X:
    def m1(self):
        print("m1 in X")
class Y:
    def m1(self):
        print("m1 in Y")
class Z:
    pass
def calling_m1(x):
    x.m1()
obj=X()
obj1=Y()
obj2=Z()
calling_m1(obj)
calling_m1(obj1)