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
def isprime(a):
    fc=0
    for i in range(1,a+1):
        if a%i==0:
            fc=fc+1
    return fc==2
n=int(input())
if isprime(n):
    print("prime number")


