# Basic List Questions
# 1. Write a program to create a list by taking input from the user and print the list.
# l=list(map(int,input().split()))
# print(l)
# 2. Write a program to insert an element at a specific index in a list.
l=[10,20,30,405,9]
l.insert(2,4)
print(l)
# 3. Write a program to merge two lists into a single list.
l=[1,23,4,5,5,6]
l1=[23,45,6,7]
l.extend(l1)
print(l)
# 4. Write a program to remove a specific element from a list.
l=[10,20,30,40]
l.remove(20)
print(l)
# 5. Write a program to remove an element from a list using its index.
l=[10,203,43,50,60]
l.pop(2)
print(l)
# 6. Write a program to find the index of a given element in a list.
l=[10,203,30,56,78]
print(l.index(203))
# 7. Write a program to count the number of occurrences of an element in a list.
l=[20,349,20,10,10,90]
print(l.count(10))
# 8. Write a program to find the sum of the first and last elements of a list.
l=[1,2,3,4,5,56,4]
n=l[0]+l[-1]
print(n)
# 9. Write a program to calculate the sum of list elements up to a given index.
l=[23,34,54,6,7,8,9,0]
a=4
sum=0
for i in range(0,a+1):
    sum+=l[i]
print(sum)
# 10. Write a program to calculate the average of odd numbers in a list.
l=[1,2,3,4,5,6,6,7]
sum=0
c=0
for i in l:
    if i%2!=0:
        sum+=i
        c+=1
avg=sum/c
print(avg)
# 11. Write a program to print all prime numbers present in a list.
l=[1,2,3,4,45,6,7,8,9]
for i in l:
    if i>1:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            print(i,end=" ")
print()
# 12. Write a program to print the next prime number for each element in the list
def next_prime(a):
    m=a+1
    while True:
        fc=0
        for i in range(1,m+1):
            if m%i==0:
                fc+=1
        if fc==2:
            return m
            break
        m+=1
l=[2,54,67,8,790,6]
for i in l:
    print(next_prime(i),end=" ")
print()
# 13. Write a program to print the list in reverse order.
l=[92,23,34,67,8]
l.reverse()
print(l)
# 14. Write a program to find sum of any two elements which is equal to key value

##############  Maximum & Minimum ##########
# 15. Write a program to find the largest number in a list.
from functools import reduce
l=[1,2,3,4,5,5,643,6,97]
m=reduce(lambda a,b:a if a>b else b,l)
print(m)
# 16. Write a program to find the second largest number in a list.
highest = 2
l=list(set([1,2,3,4,5,6,74,5,67,74,45,56]))
l.sort(reverse=True)
print(l[highest-1])
### or
l=list(set([1,2,3,4,5,6,74,5,67,74,45,56]))
l.sort()
print(l[-2])
# 17. Write a program to find the third largest number in a list.
l=list(set([1,2,3,4,5,6,74,5,67,74,45,56]))
l.sort()
print(l[-3])
# 18. Write a program to sort a list without using any built-in sorting functions.
l=[1,2,4,56,7,89]

# 19. Write a program to find the Nth largest element in a list.
# 20. Write a program to print the first four smallest missing elements from a list