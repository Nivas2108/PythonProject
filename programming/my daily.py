# a=0
# b=1
# for i in range(10):
#     print(a)
#     c=a+b
#     a=b
#     b=c
#####
a=int(input())
dc=len(str(a))
sum=0
while a>0:
    r=a%10
    sum+=r**dc
    a=a//10
if sum==a:
    print("Armstrong number")
else:
    print("Not Armstrong number")