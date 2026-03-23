# l=list(map(int,input().split()))
# i=int(input())
# val=int(input())
# l.insert(i,val)
# print(*l)
#######################
# l1=list(map(int,input().split()))
# l2=list(map(int,input().split()))
# l1.extend(l2)
# print(l1)
#####
# l=list(map(int,input().split()))
# val=int(input())
# if val in l:
#     l.remove(val)
#     print(*l)
# else:
#     print("not found")
#######
# l=list(map(int,input().split()))
# i=int(input())
# if i>=-(len(l) and i<len(l)):
#     l.pop(i)
#     print(*l)
# else:
#     print("Invalid")
###########
# l=list(map(int,input().split()))
# val=int(input())
# if val in l:
#     k=l.index(val)
#     print(k)
# else:
#     print("invalid")
########
# 14. Write a program to find sum of any two elements which is equal to key value
l=list(map(int,input().split()))
k=int(input())
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==k:
            print(f"({l[i]},{l[j]})")

