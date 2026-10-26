# a=0
# b=1
# for i in range(10):
#     print(a)
#     c=a+b
#     a=b
#     b=c
#####
# a=int(input())
# dc=len(str(a))
# sum=0
# while a>0:
#     r=a%10
#     sum+=r**dc
#     a=a//10
# if sum==a:
#     print("Armstrong number")
# else:
#     print("Not Armstrong number")
######################
arr = [2, 7, 11, 15, 3, 6]
target = 9
seen = {}
for i in range(len(arr)):
    complement = target - arr[i]
    if complement in seen:
        print(seen[complement], i)
        break
    seen[arr[i]] = i