# # print the highest digit in a number #
# a=int(input())
# h=0
# while a>0:
#     r=a%10
#     if r>h:
#         h=r
#     a=a//10
# print(h)
# # print the lowest digit in a number #
# a=int(input())
# l=9
# while a>0:
#     r=a%10
#     if r<l:
#         l=r
#     a=a//10
# print(l)
# # automorphic number #
# n=int(input())
# if n>0:
#     a=n*n
#     b=a%10
# if n==b:
#     print("automorphic number")
# else:
#     print("not a automorphic number")
###########################################
# a=212
# if a<=0:
#     print("invalid input")
# else:
#     s=0
#     for i in str(a):
#         if int(i)%2==0:
#             s=s+int(i)
#     print(s)
####################HIGHEST,LOWEST,SPAN
# a=2674672
# h=0
# l=9
# while a>0:
#     r=a%10
#     if r<l:
#         l=r
#         a=a//10
#         print(l)
#     elif r>h:
#         h=r
#         print(h)
#         print(h-l)
##################### HIGHEST,LOWEST,DIFFERENCE #######
# n=6745489
# # Convert number to string and then to list of digits
# a = [int(d) for d in str(n)]
# highest = max(a)
# lowest = min(a)
# span=max(a)-min(a)
# print("Highest digit:", highest)
# print("Lowest digit:", lowest)
# print(span)
#####################################  NEAREST PRIME  ######
y=int(input())
a=y
def prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True
c=0
while c!=1:
    a=a+1
    if prime(a)==True:
        c=1
print(a)
c=0
b=y
while c!=1:
    b=b-1
    if prime(a)==True:
        c=1
print(b)
############# FIBONACCI ################
# n=int(input())
# a=0
# b=1
# for i in range(1,n+1):
#     print(a)
#     c=a+b
#     a=b
#     b=c