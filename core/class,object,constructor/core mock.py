# class Insufficient(Exception):
#     pass
# class Bankaccount:
#     def __init__(self,balance):
#         self.balance=balance
#     def Withdraw(self,amount):
#         if amount>self.balance:
#             raise Insufficient("amount is insufficient")
#         self.balance=amount
# B=Bankaccount(4000)
# B.Withdraw(5000)
# a=Bankaccount(5000)
# a.Withdraw(5000)
#####
# class book:
#     def __init__(self,title,author,price):
#         self.title=title
#         self.author=author
#         self.price=price
#         if self.price<=0:
#             raise ValueError("Invalid price")
#     def display_details(self):
#         print("The title is",self.title,"author is",self.author,"and price of the book is",self.price)
# # a=book("core","tyson",900)
# # a.display_details()
# try:
#     b=book("title","author",-100)
#     b.display_details()
# except ValueError as v:
#     print(v)
##########
# from abc import ABC,abstractmethod
# class UserBase(ABC):
#     def get_role(self):
#           pass
# class Member(UserBase):
#     def __init__(self,username,credentials,perms):
#         self.username=username
#         self._credentials=credentials
#         self.__perms=perms

