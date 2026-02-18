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
n=6
c=1
for i in range(1,n+1):
    for j in range(1,n+1):
        print(c,end=" ")
        if c==1:
            c=0
        else:
            c=1
    print()
    if c==1:
        c=0
    else:
        c=1
