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