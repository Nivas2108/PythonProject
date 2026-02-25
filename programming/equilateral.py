## inverted ##
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i<=j:
#             print("*",end=" ")
#         else:
#             print(end=" ")
#     print()
#### STRAIGHT TRIANGLE ####
# n=5
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     print("* "*i)
#### OR ####
n=5
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(end=" ")
    for j in range(1,i+1):
        print(end="* ")
    print()
######## NUMBER TRIANGLE ######
n=5
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(end=" ")
    for j in range(1,i+1):
        print(i,end=" ")
    print()
###### NUMBER COLUMN TRIANGLE #####
n=5
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
###### REVERSE AND STRAIGHT NUMBER TRIANGLE ###
n=5
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(end="  ")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()
##### REVERSE AND STRAIGHT NUMBER TRIANGLE ANOTHER TYPE  ###
n=5
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(end="  ")
    for j in range(i,0,-1):
        print(j,end=" ")
    for j in range(2,i+1):
        print(j,end=" ")
    print()

