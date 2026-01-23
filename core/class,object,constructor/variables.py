class Student:
    total_students=0
    def __init__(self,name):
        self.name=name
        Student.total_students+=1
        print(f"new student has been created {self.name}.Total students={Student.total_students}")
s1=Student("Nivas")
s2=Student("nivas")
#####################################
d = {'a': 1}
k = d.keys()
d['b'] = 2
print(list(k))
#########################################
class Loan:
    interest=0.1
    def __init__(self,a,n):
        self.name=n
        self.amount=a
    def total_amount(self,x):
        return self.amount(x*(self.amount*self.interest))
    def change_interest(self,b):
        Loan.interest=b
l1=Loan('hl',10000)
l1.change_interest
####################################
class Loan:
    interest=0.1
    @classmethod
    def m1(cls,ni):
        cls.interest=ni
Loan.m1(0.2)
print(Loan.interest)
####################################
class payment:
    def __init__(self,amount):
        self.amount=amount
    @classmethod
    def upipayment(cls,a,p):
        print(f"upi payment to {p} is done")
        return cls(a)
p1=payment.upipayment(500,9121949490)
############################################
class date:
    def __init__(self,d,m,y):
        self.d=d
        self.m=m
        self.y=y
    @classmethod
    def usdateformat(cls,date):
        m,d,y=date.split("/")
        return cls(d,m,y)
d1=date.usdateformat("01/06/2026")
print(d1.d)