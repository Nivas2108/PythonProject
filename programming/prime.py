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
a=int(input())
c=0
n=a+1 ### or n-1 for previous prime
while c<1:
    prime=True
    for i in range(2,n):
        if n%i==0:
            prime=False
            break
    if prime:
        c=c+1
        print(n)
    n=n+1 ##n-1 for previous prime







