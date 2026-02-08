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
# a=267467289
# l=9
# h=0
# while a>0:
#     r=a%10
#     if r<l:
#         l=r
#     elif r>h:
#         h=r
#     a=a//10
# print(l)
# print(h)
# print(h-l)
        # print(h-l)
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
################################# nearest prime
# a = int(input())
# num1 = a - 1
# num2 = a + 1
# while True:
#     prime = True
#     for i in range(2, num1):
#         if num1 %  i == 0:
#             prime = False
#             break
#     if prime:
#         break
#     num1 -= 1
# while True:
#     prime = True
#     for j in range(2, num2):
#         if num2 % j == 0:
#             prime = False
#             break
#     if prime:
#         break
#     num2 += 1
# if abs(a - num1) > abs(a - num2):
#     print(num2)
# elif abs(a - num1) == abs(a - num2):
#     print(num1)
#     print(num2)
# else:
#     print(num1)
##############################  n terms of alternative fibonacci series   ######
# n=int(input())
# a=0
# b=1
# for i in range(1,2*n+1):
#     if i%2==1:
#         print(a,end=" ")
#     c=a+b
#     a=b
#     b=c
############# Average of all Palindrome Numbers between the Range ########
# a=int(input())
# b=int(input())
# for i in range(a,b+1):
#     t=i
#     c=0
#     rev=0
#     avg=0
#     while t>0:
#         sum = 0
#         r=t%10
#         rev=rev*10+r
#         t=t//10
#     if rev==i:
#         print(i)
####################### ROUND ##########
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
############################### prime factors ####
# def isprime(a):
#     fc=0
#     for i in range(1,a+1):
#         if a%i==0:
#             fc=fc+1
#     return fc==2
# a=int(input())
# f=0
# if a<0:
#     a=-a
# if a==0:
#     print("Invalid Input")
# else:
#     for i in range(1,a+1):
#         if a%i==0:
#             if isprime(i):
#                 print(i,end=" ")
#                 f=1
#     if f==0:
#         print("No Prime Factors")
############################################# ARMSTRONG NUMBERS IN THE GIVEN RANGE ####
# a=int(input())
# b=int(input())
# for i in range(a,b+1):
#     t=i
#     d=len(str(i))
#     s=0
#     while t>0:
#         r=t%10
#         s=s+(r**d)
#         t=t//10
#     if s==i:
#         print(i)
# #####################
# t = (10, 20, 30)
# for i in t:
#     if i == 20:
#         i = 99
#     print(t)
######################################## $ PRIME $ #########################################
################### using mul operator ##########
# n=int(input())
# if int(n*0.5)*2==n:
#     print("even")
# else:
#     print("odd")
# #################### using left and right shift operators #########
# n=int(input())
# if int((n>>1)<<1)==n:
#     print("even")
# else:
#     print("odd")
# ################### using sub operator ##############
# n=int(input())
# while n>1:
#     n=n-2
# if n==0:
#     print("even")
# else:
#     print("odd")
# ################## using add operator ##############
# n=int(input())
# m=0
# while m<n:
#     m=m+2
# if m==n:
#     print("even")
# else:
#     print("odd")








