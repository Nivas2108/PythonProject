##### dynamic sliding window #####
###### min length #######
# def minSubArrayLen( target, nums):
#     l = 0
#     r = 0
#     sum = 0
#     mlen = float("+inf")
#     while r < len(nums):
#         sum += nums[r]
#         while sum >= target:
#             mlen = min(mlen, r - l + 1)
#             sum -= nums[l]
#             l += 1
#         r += 1
#     if mlen == float("+inf"):
#         print(0)
#     else:
#         print(mlen)
# nums=[1,2,3,4,5,7]
# target=16
# minSubArrayLen(13,[1,2,3,4,5,6,7])
############ longest substring without repeating characters
s = input("Enter a string: ")
start = 0
max_len = 0
l = {}
for end in range(len(s)):
    if s[end] in l and l[s[end]] >= start:
        start = l[s[end]] + 1
    l[s[end]] = end
    max_len = max(max_len, end - start + 1)
print("Length of longest substring:", max_len)
###########
### insertion sort ###
l=[8,2,5,7,6]
for i in range(1,len(l)):
    for j in range(i,0,-1):
        if l[j-1]>l[j]:
            l[j-1],l[j]=l[j],l[j-1]
        else:
            break
    print(l)
############
### selection sort ###
l=[7,3,4,2,5,8]
for i in range(len(l)-1):
    max=0
    for j in range(0,len(l)-i):
        if l[j]>l[max]:
            max=j