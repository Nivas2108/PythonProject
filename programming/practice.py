########## ARMSTRONG two variables ###
# a=1
# b=200
# for i in range(a,b+1):
#     dc=len(str(i))
#     d=0
#     for j in str(i):
#         d+=int(j)**dc
#     if d==i:
#         print(i,end=" ")
############ armstrong ####
# a=500
# for i in range(1,a+1):
#     dc=len(str(i))
#     d=0
#     for j in str(i):
#         d+=int(j)**dc
#     if d==i:
#         print(i,end=" ")
############ ARMS
# a=153
# b=str(a)
# c=len(b)
# d=0
# for i in range(c):
#     d+=int(b[i])**c
# if d==a:
#     print(a,end=" ")
############ FIBONACCI #######
# n=10
# a=0
# b=1
# for i in range(1,n+1):
#     if i%2==1:
#         print(a,end=" ")
#     c=a+b
#     a=b
#     b=c
######### fibonacci two variables #####
# n1=10
# n2=90
# a=0
# b=1
# while a<=n2:
#     if a>=n1:
#         print(a,end=" ")
#     c=a+b
#     a=b
#     b=c
########### PALINDROME #####
# n=131
# k=n
# rev=0
# while n>0:
#     r=n%10
#     rev=rev*10+r
#     n=n//10
# # print(rev)
# if rev==k:
#     print(k)
########## palindrome 2 variables ####
# a=100
# b=200
# for i in range(a,b+1):
#     t=i
#     rev=0
#     while t>0:
#         r=t%10
#         rev=rev*10+r
#         t=t//10
#     if rev==i:
#         print(rev,end=" ")
#########
# a=11
# fc=0
# for i in range(1,a+1):
#     if a%i==0:
#         fc=fc+1
# if fc==2:
#     print(i,end=" ")
############ palindrome simple
# n=100
# n2=200
# sum=0
# for i in range(n,n2+1):
#     if i==int(str(i)[::-1]):
#        print(i,end=" ")
##### mock question arms ###
# a=1
# n=400
# k=0
# sum=0
# for i in range(a,n+1):
#     b=str(i)
#     c=len(b)
#     d=0
#
#     for j in range(c):
#         d+=int(b[j])**c
#     if d==i:
#         if k==0:
#             print("Armstrong Numbers are (",end=" ")
#         k+=1
#         if k%2==1:
#             if k>1:
#                 sum+=i
#                 print("+",end=" ")
#             print(i,end=" ")
# print(")","=",sum,end="")
####### mock patterns ###
# n=6
# for i in range(1, n + 1):
#     t = i
#     d = n - 1
#     for j in range(i):
#         print(t, end=" ")
#         t += d
#         d-=1
#     print()
##### mock arms ####
# start = 1
# end = 200
# count = 0
# total_sum = 0
# alt_index = 0
# expr = ""
# for num in range(start, end + 1):
#     digits = str(num)
#     power = len(digits)
#     total = 0
#     for d in digits:
#         total += int(d) ** power
#     if total == num:
#         if alt_index % 2 == 0:
#             total_sum += num
#             count += 1
#             if expr == "":
#                 expr = str(num)
#             else:
#                 expr += " + " + str(num)
#         alt_index += 1
# if count == 0:
#     print("No Armstrong Numbers in a Given Range")
# else:
#     avg = total_sum / count
#     print(f"Average of Alternative Armstrong Numbers in the Given Range is ( {expr} ) / {count} = {avg:.2f}")

####
n="ABTRYIHNK12233637abfjk"
a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
b="abcdefghijklmnopqrstuvwxyz"
c="1234567890"
for i in n:
    s=""
    if i in a:
        s+=i
        print(s,end="")

    # print()
    # elif i in b:
    #     print(i,end="")
    # elif i in c:
    #     print(i,end="")
########
l=[4,6,5,6,-1,0,2,7]
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
print(l)
