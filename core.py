class LibraryMember:
    borrowing_limit=3
    def __init__(self,member_name,books_borrowed):
        self.member_name=member_name
        self.books_borrowed=books_borrowed
    def borrowing(self):
        if self.books_borrowed<LibraryMember.borrowing_limit:
            self.books_borrowed += 1
        else:
            print("out of limit")
    @classmethod
    def update(cls,new_limit):
        cls.borrowing_limit=new_limit
    @staticmethod
    def books(a):
        if a.books_borrowed>1:
            print("positive")
        else:
            print("negative")
x1=LibraryMember("nivas",1)
x2=LibraryMember("madhu",4)
LibraryMember.borrowing(x1)
LibraryMember.borrowing(x2)
#####################
from functools import reduce
l=[5,10,15,20,25]
print(reduce(lambda a,b:a+b,filter(lambda x:x%5==0,map(lambda x:x**2,l))))
############
# class movie:
#     total_movies=0
#     def __init__(self,name,director):
#         self.name=name
#         self.director=director
#         movie.total_movies+=1
#     def cinema(self,t):
#         if len(self.name)<4:
#             print("alteast 4")
#         else:
#             print("valid")
#     @classmethod
#
# m1=movie("sye","rajamouli")
# m2=movie("spirit","vanga")




