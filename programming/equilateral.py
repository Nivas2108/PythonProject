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
###$$ typical $$###
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i<=j:
            print(j,end=" ")
        else:
            print(end="  ")
    for j in range(n-1,i-1,-1):
        print(j,end=" ")
    print()

####
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i==n or j==1:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
####
n=5
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(end=" ")
    for j in range(1,i+1):
        if i==j :
            print("*",end=" ")
    print()
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j  or j==n:
            print("*",end=" ")
        else:
            print(end=" ")
    print()
################ $$ PASCAL TRIANGLE $$ ######
n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    # for j in range(1,n-i+1):
    #     print(end=" ")
    m=1
    for j in range(1,i+1):
        print(m,end=" ")
        m=m*(i-j)//j
    print()
######
### $$$ RHOMBUS $$$ ###
n=5
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(1,n+1):
    for j in range(1,n+1):
        if i<=j:
            print("*",end=" ")
        else:
            print(end=" ")
    print()
###### rhombus #####
n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("* "*(i))
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    print("* "*(i))
print()
######### rhombus row number ####
n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(i,end=" ")
    print()
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(i,end=" ")
    print()
######## typical numbers in rhombus ###
n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()
###########
n=5
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end="")
    for j in range(2,i+1):
        print(j,end="")
    print()
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    for j in range(i,1,-1):
        print(j,end="")
    print()
###### different * pattern ####
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i<=j:
            print("*",end="")
        else:
            print(end=" ")
    for j in range(1,i+1):
        print("*",end="")
    print()