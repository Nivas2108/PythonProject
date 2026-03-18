l=[10,20,30,40,50]
print(l)
print(*l)
print(l[0])
print(len(l))
###
l=[10,20,30,40,50]
for i in range(len(l)):
    print(l[i],end=" ")
print()
####### OR ##
for i in l:
    print(i,end=" ")
print()
########
l=[8,9,80,65,76]
for i in range(0 ,len(l),2):
    print(l[i],end=" ")
print()
#####
for i in l:
    if i%2==0:
        print(i)
##### $ APPEND $ ###########
l.append(0)
print(l)
######### $ EXTEND $ ######
l=[10,20,30,40]
l1=[50,60,70]
l.extend(l1)
print(l)
print(l1)
####
l=[10,20,30]
l.extend("Bye")
print(l)
####### $ INSERT $ #######
l=[10,20,30,40]
l.insert(2,50)
print(l)
l.insert(3,60)
print(l)
l.insert(10,80)
print(l)
##### $ membership operators IN and NOT IN $ ####
print(90 not in l)
print(90 in l)
####
l=[10,20,30,40,20,10]
l.remove(20)
print(l)
###### $ POP $ ####
l=[10,20,30,40]
a=l.pop(2) ## or l.pop(-2)
print(a)
print(l)
## with condition ###
l=[10,20,30,40,60]
i=4
if i>=-(len(l)) or i<len(l):
    k=l.pop(i)
    print(k)
else:
    print("invalid")
### $ CLEAR $ ##
l=[10,20,30,40]
l.clear()
print(l) ### prints empty list
#### $ INDEX $ ########
l=[10,20,0,40,30,20,90]
print(l.index(30,2,5))
print(l.index(20))
####
l=[10,20,0,40,30,20,90]
val=30
if val in l:
    k=l.index(val)
    print(k)
else:
    print("not ")
#### $ COUNT $ #####
l=[10,20,30,20,40,40,50,19]
print(l.count(10))
### $ SORT $ ###
l=[10,10,40,30,50]
l.sort(reverse=True)
print(l)
##### $ reverse $ ###
l=[10,20,30,40,60]
l.reverse()
print(l)