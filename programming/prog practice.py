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
a=212
if a<=0:
    print("invalid input")
else:
    s=0
    for i in str(a):
        if int(i)%2==0:
            s=s+int(i)
    print(s)

