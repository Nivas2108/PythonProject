# Use functools.reduce() with a lambda to find the largest number from a given list Dynamically
import functools
l=[1,2,23,45,73,9]
l2=functools.reduce(lambda x,y:x if x>y else y,l)
print(l2)
#
nums = [1, 2, 3]
result = map(lambda x: x * 2, nums)
nums.clear()
print(list(result))
###########################
from functools import reduce
lists = [[1], [2, 3], [4]]
result = reduce(lambda a, b: a + b, lists)
print("Flattened:", result)
#############################
n=3.25
p=int(n*100)
print(f"{p}CM")
#########################
F=212
C=int(((F-32)*5)/9)
print(f"{C}F")
#############################
a,b,c=3,4,7
if a<b and a<c:
    print(a)
if b<a and b<c:
    print(b)
if c<a and c<b:
    print(c)
################################
n=499
if 50<=n>=500:
    print("invalid number")
else:
    if n%2==0:
        print(n%5)
    else:
        print(n%7)
##########################################
import functools
s="*@hi123"
n= lambda text: sum(map(ord, filter(str.isalpha,text)))
result = n
print(result)
#############################################
# l="hi123@"
# l2=reduce(lambda x,y:x+ord(y,list(lambda x:x.isalpha(),l)),0)
# print()
##########################################
l1=[1,2,3,34,4,455,6,6,6,7,8,8,8,9,10]
l=set(l)
print(l)


