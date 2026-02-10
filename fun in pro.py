# def isevenodd(a):
#     return a%2==0
# n=int(input())
# if isevenodd(n):
#     print("even")
# else:
#     print("odd")
###################
# def Range(a,b):
#     for i in range(a,b+1):
#         print(i)
# n=int(input())
# n1=int(input())
# Range(n,n1)
# ################
# def Range(a,b):
#     sum=0
#     for i in range(a,b+1):
#         if True:
#             sum=sum+i
#     return sum
# n1=int(input())
# n2=int(input())
# k=Range(n1,n2)
# print(k)
################### PRIME(one input) #######
# def prime(a):
#     fc=0
#     for i in range(1,a+1):
#         if a%i==0:
#             fc=fc+1
#     if fc==2:
#         print("prime")
#     else:
#         print("not prime")
# n=int(input())
# prime(n)
##################### PRIME(two inputs) ##########
# def isprime(a,b):
#     for i in range(a,b+1):
#         fc=0
#         for j in range(1,i+1):
#             if i%j==0:
#                 fc=fc+1
#         if fc==2:
#             print(i)
#         else:
#             print("not a prime")
# n=int(input())
# n1=int(input())
# isprime(n,n1)
############### ARMSTRONG ##############
# def armstrong(a,b):
#     for i in range(a,b+1):
#         t=i
#         d=len(str(i))
#         s=0
#         while t>0:
#             r=t%10
#             s=s+(r**d)
#             t=t//10
#         if s==i:
#             print(i)
# n1=int(input())
# n2=int(input())
# armstrong(n1,n2)
############### PALINDROME ###############
def palindrome(a,b):
    for i in range(a,b+1):
        t=i
        c=0
        rev=0
        avg=0
        while t>0:
            sum = 0
            r=t%10
            rev=rev*10+r
            t=t//10
        if rev==i:
            print(i)
n1=int(input())
n2=int(input())
palindrome(n1,n2)