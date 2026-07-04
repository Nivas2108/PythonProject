# Basic List Questions
# 1. Write a program to create a list by taking input from the user and print the list.
# l=list(map(int,input().split()))
# print(l)
# 2. Write a program to insert an element at a specific index in a list.
# l=[1,2,3,4,5,6,78,8]
# l.insert(3,23)
# print(l)
# 3. Write a program to merge two lists into a single list.
# l=[1,2,3,4,5,6]
# l1=[23,4563,456,345,67]
# l.extend(l1)
# a=l+l1
# print(a)
# 4. Write a program to remove a specific element from a list.
# l=[1,2,3,4,5,6,7,8]
# l.remove(4)
# print(l)
# 5. Write a program to remove an element from a list using its index.
# l=[1,2,3,4,4,5,6,7]
# l.pop(3)
# print(l)
# 6. Write a program to find the index of a given element in a list.
# l=[1,2,3,4,5,6,6,8]
# a=l.index(4)
# print(a)
# 7. Write a program to count the number of occurrences of an element in a list.
# l=[1,2,3,4,5,67,89,5,5,5]
# a=l.count(5)
# print(a)
# 8. Write a program to find the sum of the first and last elements of a list.
# l=[1,2,3,4,5,6,7,8,9]
# print(l[0]+l[-1])
# 9. Write a program to calculate the sum of list elements up to a given index.
# l=[1,2,23,45,67,8,990]
# a=5
# sum=0
# for i in range(0,a+1):
#     sum+=l[i]
# print(sum)
# 10. Write a program to calculate the average of odd numbers in a list.
# l=[1,2,3,4,56,7,78,9]
# sum=0
# c=0
# for i in l:
#     if i%2!=0:
#         sum+=i
#         c+=1
#     avg=sum/c
# print(avg)
# 11. Write a program to print all prime numbers present in a list.
# l=[1,2,34,5,6,78,9,77]
# for i in l:
#     if i>1:
#         for j in range(2,int(i**0.5)+1):
#             if i%j==0:
#                 break
#         else:
#             print(i)
# 12. Write a program to print the next prime number for each element in the list
# def next_prime(a):
#     m=a+1
#     while True:
#         fc=0
#         for i in range(1,m+1):
#             if m%i==0:
#                 fc+=1
#         if fc==2:
#             return m
#             break
#         m+=1
# l=[2,54,67,8,790,6]
# for i in l:
#     print(next_prime(i),end=" ")
# print()
# 13. Write a program to print the list in reverse order.
# l=[1,2,3,4,5,67,8,9]
# l.reverse()
# print(l)
# 14. Write a program to find sum of any two elements which is equal to key value
# l=list(map(int,input().split()))
# key=int(input())
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==key:
#             print(f"{l[i]},{l[j]}")
###############
# n=int(input())
# a=[]
# for i in range(n):
#     a[i]=int(input())
# key=int(input())
# for i in range(0,n):
#     for j in range(i,n):
#         if a[i]+a[j]==key:
#             print(a[i],a[j])
# Maximum & Minimum
# 15. Write a program to find the largest number in a list.
# l=list(map(int,input().split()))
# l.sort()
# print(l[-1])
# 16. Write a program to find the second largest number in a list.
# l=list(map(int,input().split()))
# l.sort()
# print(l[-2])
# 17. Write a program to find the third largest number in a list.
# l=list(map(int,input().split()))
# l.sort()
# print(l[-3])
# 18. Write a program to sort a list without using any built-in sorting functions.
# l=[1,2,34,5,67,9,3]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)
# 19. Write a program to find the Nth largest element in a list.
# l=list(map(int,input().split()))
# l.sort()
# print(l[-1])
# 20. Write a program to print the first four smallest missing elements from a list
# l= [1, 2, 4, 6, 8, 10]
# m= []
# i = 1
# while len(m) < 4:
#     if i not in l:
#         m.append(i)
#     i += 1
# print(m)
# Searching
# 21. Write a program to perform linear search on a list.
# 22. Write a program to perform binary search on a sorted list.
# 23. Write a program to return all index positions of a searched element in a list.
# 24. Write a program to check whether a list is sorted or not.
# Math on arrays
# 25. Write a program to find the LCM of all numbers in the list.
# 26. Write a program to find the GCD of all numbers in the list.
# 27. Write a program to find the factorial of each element in a list
# Frequency
# 28. Write a program to find the frequency of each element in a list.
# 29. Write a program to calculate the backward frequency of elements in a list.
# 30. Write a program to print frequencies of each element without repetition.
# 31. Write a program to find the most frequently repeated element in a list.
