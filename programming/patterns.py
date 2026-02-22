# a=5
# b=5
# for i in range(1,a+1):
#     for j in range(1,b+1):
#         print(end="* ")
#     print()
######################
# a=4
# b=5
# for i in range(1,a+1):
#     print(b*"* ")
########## ROW NUMBERS ##########
# a=4
# b=5
# for i in range(1,a+1):
#     for j in range(1,b+1):
#         print(i,end=" ")
#     print()
############# COLUMN NUMBERS ###########
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j,end=" ")
#     print()
################ COLUMN AND ROW MIX ###########
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(f"{i}{j} ",end="")
#     print()
########### DIAGONAL ################
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j:
#             print(end="1 ")
#         else:
#             print(end="0 ")
#     print()
########## UPPER DIAGONAL #########
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i<=j:
#             print(end="* ")
#         # else:
#         #     print(end="0 ")
#     print()
# # ############## LOWER DIAGONAL ########
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i>=j:
#             print(end="* ")
#         # else:
#         #     print(end="0 ")
#     print()
# ################### ROWS COLUMNS AND DIAGONAL ##########
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j:
#             print(end="1 ")
#         elif i>j:
#             print(end="0 ")
#         else:
#             print(end="2 ")
#     print()
####################### OPPOSITE DIAGONAL ############
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i+j==n+1:
#             print(end="1 ")
#         else:
#             print(end="0 ")
#     print()
############## OPPOSITE DIAGONAL ,ROWS ,COLUMNS ######
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i+j==n+1:
#             print(end="1 ")
#         elif i+j<n+1:
#             print(end="2 ")
#         else:
#             print(end="3 ")
#     print()
################ i decrement j decrement #############
# n=5
# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         if i<=j:
#             print(j,end=" ")
#         else:
#             print(i,end=" ")
#     print()
########## $$$ different pattern module basic $$$ #####
# n=6
# c=1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(c,end=" ")
#         if c==1:
#             c=0
#         else:
#             c=1
#     print()
#     if c==1:
#         c=0
#     else:
#         c=1
################# left down triangle pattern ##################
# n=5
# for i in range(1,n+1):
#     print("*"*i)
################# right down triangle pattern #############
# n=5
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(end=" ")##print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(end="*")##print("*"*i)
#     print()
################# left upper triangle pattern ##############
# n=5
# for i in range(1,n+1):
#     for j in range(1,n-i+2):
#         print(end="*")##print(" "*(n-i+1),end="")
#     print()
################# right upper triangle #################
# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print(end=" ")
#     for j in range(1,n-i+2):
#         print(end="*")
#     print()
################ Alphabets triangle ##############
# n=5
# c=65
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(c),end=" ")
#         c=c+1
#     print()
#################### Even left down triangle #####
# n=5
# c=2
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(c,end=" ")
#         c+=2
#     print()
############ one line even and other odd left down ######
# n=5
# c=2
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(c,end=" ")
#         c+=2
#     print()
#     c-=1
########### print sum of number is even or odd in pattern ###
# n=5
# c=1
# for i in range(1,n+1):
#     sum=0
#     for j in range(1,i+1):
#         print(c,end=" ")
#         sum+=c
#         c+=1
#     print(f"-{sum} @",end=" ")
#     if sum%2==1:
#         print("odd")
#     else:
#         print("even")
############### one line straight one line reverse ######
# n=6
# c=1
# for i in range(1,n+1):
#     if i%2==1:
#         print(*range(1,n-i+2))
#     else:
#         print(*range(n-i+1,0,-1))
#########################
import math
n=5
a=2
for i in range(1,n+1):
    c=0
    while c<i:
        prime=True
        for j in range(2,int((math.sqrt(a)))+1):
            if a%j==0:
                prime=False
                break
        if prime:
            print(a,end=" ")
            c+=1
        a+=1
    print()
###################
import math
n=5
for i in range(1,n+1):
    a=2
    col=2
    c=1
    print(2,end=" ")
    while c<i:
        prime=True
        for j in range(2, int(math.sqrt(n)) + 1):
            if a%j==0:
                prime=False
                break
        if prime:
            print(a,end=" ")
            c+=1
        a+=1
    print()
