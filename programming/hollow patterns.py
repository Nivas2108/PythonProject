# ######################################### HOLLOW PATTERNS ################################################
# ##### rectangle hollow ###
# #########
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j==n or j==1:
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()
# ############
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j==n or j==1:
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()
# #### hollow right angle triangle ####
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j or i==n or j==1:
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()
# ####
# n=5
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         if i==j or i==n or j==1:
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()
# ######### hollow equilateral ####
# n=5
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         if i==j or j==1 or i==n:
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()
# ###########  hollow rhombus ######
# n=5
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         if i==j or j==1 :
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()
# n=5
# for i in range(n,0,-1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         if i==j or j==1:
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()
########## prime pattern ###
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
# n=4
# p=2
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(p,end=" ")
#         p=next_prime(p)
#     print()
######## fibonacci pattern ###
# n=5
# a=0
# b=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(a,end=" ")
#         c=a+b
#         a=b
#         b=c
#     print()



