s = input()
k = int(input())
# Check invalid length
if k <= 0:
    print("Invalid Length")
# Check substring possibility
elif k > len(s):
    print("Substring not possible")
# Check special characters
elif not s.isalnum():
    print("Invalid String")
# Print substrings without slicing
else:
    for i in range(len(s) - k + 1):
        sub = ""
        for j in range(i, i + k):
            sub = sub + s[j]
        print(sub)