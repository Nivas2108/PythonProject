# # ANTI CLOCKWISE ROTATION #
# l=[10,20,40,30,50]
# for i in range(len(l)):
#     print(*l)
#     l=l[1:]+[l[0]]
# #### or ####
# l=[10,20,30,40]
# for i in range(len(l)):
#     print(*l)
#     t=l[0]
#     for j in  range(1,len(l)):
#         l[j-1]=l[j]
#     l[len(l)-1]=t
# ####### CLOCKWISE ROTATION #######
# l=[10,20,30,40]
# for i in range(len(l)):
#     print(*l)
#     l=[l[len(l)-1]]+l[0:len(l)-1]
## or ###
# l=[10,20,30,40]
# for i in range(len(l)):
#     print(*l)
#     t=l[len(l)-1]
#     for j in range(len(l)-2,-1,-1):
#         l[j+1]=l[j]
#     l[0]=t
################ kth time rotation  in clockwise direction ###
# l=[10,20,30,40]
# k=4
# for i in range(len(l)):
#     if k%len(l)==i:
#         print(*l)
#     t=l[len(l)-1]
#     for j in range(len(l)-2,-1,-1):
#         l[j+1]=l[j]
#     l[0]=t
######### SUB LISTS ######
# l=[10,20,30,40,50]
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         for k in range(i,j+1):
#             print(l[k],end=" ")
#         print()
##### OR #####
# l=[10,20,30,40]
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         l1=l[i:j+1]
#         print(*l1)
######## key same to sum of sublists #####
# n=30
# l=[10,20,30,40]
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         l1=l[i:j+1]
#         if sum(l1)==n:
#             print(*l1)
######### linear search #########
# l=list(map(int, input().split()))
# element=int(input())
# exist=False
# for i in range(len(l)):
#     if element==l[i]:
#         print(i)
#         exist=True
# if exist:
#     print("element found")
# else:
#     print("Not found")
######## binary search ######
# l=list(map(int, input().split()))
# element=int(input())
# l.sort()
# low=0
# high=len(l)-1
# found=False
# while low<=high:
#     mid=(low+high)//2
#     if l[mid]==element:
#         print("element found:",mid+1)
#         found=True
#         break
#     elif element>l[mid]:
#         low=mid+1
#     else:
#         high=mid-1
# if not found:
#     print("element not found")
############# sum of two#############
l=list(map(int, input().split()))
element=int(input())
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==element:
            print(f"[{l[i]},{l[j]}]")
