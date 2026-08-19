import threading
def sum(a,b):
    res=a+b
    print(res)
thread=threading.Thread(target=sum(4,5))
thread.start()
thread.join()
#####
# class user:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
# class Digital_Wallet(user):
#     def __init__(self, balance, name, phone):
#         super().__init__(name, phone)
#         self.__balance=balance
# class Insufficient(Exception):
#    pass
# def add_money(self,money):
#     self.__balance += money
# def pay_bill(self,money):
#     if money>self.__balance:
#         raise Exception("Insufficient amount")
#     self.__balance-=money
#####

from contextlib import contextmanager
@contextmanager
def open_file(filename,mode):
    file=open(filename,mode)
    try:
        yield file
    finally:
        file.close()