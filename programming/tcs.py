## REVERSE A STRING WITHOUT BUILTIN ###
s = "tcs"
rev = ""
for i in s:
    rev = i + rev
if s==rev:
    print(rev)
else:
    print ("no")
######## SECOND HIGHEST ELEMENT ##
l = [10, 20, 4, 45, 99]
first = second = -1
for num in l:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num
print(second)
l = [10, 20, 4, 45, 99]

first = second = -1

for num in l:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num
print(second)
