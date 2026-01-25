# n=25
# c=0
# for i in range (1,n+1):
#     if i%2==0:
#         c=c+1
#         if c==1:
#             print(i,end=" ")
#         if c==3:
#             print(i,end=" ")
#         if c==6:
#             print(i,end=" ")
#         if c==10:
#             print(i,end=" ")
# #####################################
# n=25
# c=0
# for i in range(1,n+1):
#     c=c+1
#     if i%2==0:
#         print(i,end=" ")
# ########################################
# n = 35
# s= 4
# i = 2
# while i <= n:
#     print(i, end=" ")
#     i += s
#     s += 2
# ###########################################
# a=int(input())
# b=int(input())
# c=0
# if a<b:
#     for i in range(a,b+1,1):
#         c=c+1
#         if c>1:
#             print(",",end=" ")
#         if i<0:
#             print(f"5*({i})",end="")
#         else:
#             print(f"5*{i}",end="")
# else:
#     for i in range(a,b-1,-1):
#         c=c+1
#         if c>1:
#             print(",",end=" ")
#         if i<0:
#             print(f"5*({i})",end="")
#         else:
#             print(f"5*{i}",end="")
#######################################
# a=float(input())
# b=float(input())
# c=0
# while(round(a,1)<=b):
#     c=c+1
#     if c>1:
#         print(",",end=" ")
#     print(f"{a:.1f}^2",end="")
#     a=a+0.2
# print(".")



# 3.4566
# 6.7888
# 7.88889
# 9.20000
#############################################
# def isprime(a):
#     fc=0
#     for i in range(1,a+1):
#         if a%i==0:
#             fc=fc+1
#     if fc==2:
#         print("prime")
#     else:
#         print("not a prime")
# n=int(input())
# isprime(n)
####################boolean
# def isprime(a):
#     fc=0
#     for i in range(1,a+1):
#         if a%i==0:
#             fc=fc+1
#     return fc==2
# n=int(input())
# if isprime(n):
#     print("prime number")
#####################
for i in "welcome":
    print(i)
###############################
for i in range(1,3):
    for j in "hi":
        print(i,j)
###############################
def welcome(name):
    return "welcome" +name
print(welcome(" nivas"))
#########################
def math(small,large):
    diff=small-large
    return diff
print(math(5,4))
#############################*arg is as TUPLE #argument
def new(*args):
    for i in args:
        print(type(args))
new(1,"hi",56,True)
##########################**kwarg #KEYWORD ARGUMENT## is as dictionary
def new(**kwargs):
    for keys,values in kwargs.items():
        print(keys,values)
        print(type(kwargs))
new(a=1,b="hi",c=True)
############################GLOBAL
name="nivas"
def n():
    global name
    name="NIVAS"
    print(name)
n()


