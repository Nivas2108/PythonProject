#print all n number of prime numbers
# a=int(input())
# c=0
# n=2
# while c<a:
#     fc=0
#     for i in range(2,n):
#         if n%i==0:
#             fc=fc+1
#             break
#     if fc==0:
#         print(n)
#         c=c+1
#     n=n+1
# # PALINDROME #
# n=int(input())
# sum=0
# while n>0:
#     r=n%10
#     sum=sum*10+r
#     n=n//10
# print(sum)
# after
# a=int(input())
# c=0
# n=a+1 ### or n-1 for previous prime
# while c<1:
#     prime=True
#     for i in range(2,n):
#         if n%i==0:
#             prime=False
#             break
#     if prime:
#         c=c+1
#         print(n)
#     n=n+1 ##n-1 for previous prime
# ################## NEXT PRIME SIMPLE #######
# def next_prime(a):
#     m=a+1
#     while True:
#         fc=0
#         for i in range(1,m+1):
#             if m%i==0:
#                 fc+=1
#         if fc==2:
#             return m
#             break
#         m+=1
# n=7
# print(next_prime(n))
# ############# PREVIOUS PRIME SIMPLE ########
# def next_prime(a):
#     m=a-1
#     while True:
#         fc=0
#         for i in range(1,m+1):
#             if m%i==0:
#                 fc+=1
#         if fc==2:
#             return m
#             break
#         m-=1
# n=5
# print(next_prime(n))
########## NEAREST PRIME #########
a = 9
ap = a - 1
bp = a + 1
while True:
    prime = True
    for i in range(2, ap):
        if ap %  i == 0:
            prime = False
            break
    if prime:
        break
    ap -= 1
while True:
    prime = True
    for j in range(2, bp):
        if bp % j == 0:
            prime = False
            break
    if prime:
        break
    bp += 1
if abs(a - ap) > abs(a - bp):
    print(bp)
elif abs(a - ap) == abs(a - bp):
    print(ap)
    print(bp)
else:
    print(ap)



