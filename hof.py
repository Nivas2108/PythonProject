# map()and filter():returns the iterators
#reduce():returns the single value
# ***lambda functions we use for single line functions
# lambda use less memory
#


# Given two lists:
# a = [1, 2, 3, 4] b = [10, 20, 30, 40]
# Use map() with a lambda to create a new list containing the sum of corresponding
# elements.
# What happens if the lists are of unequal length?
a=[1,2,3,4]
b=[10,20,30,40]
l=list(map(lambda x,y:x+y,a,b))
print(l)
#if the lists are in unequal length then the value are printed as it is.
#if lists are unequal the shortest length elements are printed.


# Given a list:
# nums = [12, 15, 7, 18, 20, 21, 25]
# Use filter() and lambda to keep numbers that are divisible by 3 OR divisible by
# 5 but NOT divisible by both.
# Explain how the logical condition work.
nums=[12,15,7,18,20,21,25]
l=list(filter(lambda x:(x%3==0)^(x%5==0),nums))
print(l)
l2=list(filter(lambda x:not((x%3==0)and(x%5==0)),nums))
print(l2)
#  Given a list:
# nums = [1, 2, 3, 4]
# Use reduce() with a lambda to compute the sum, but start with an initial value
# of 10.
# Explain how the initial value affects the reduction process.
import functools
nums=[1,2,3,4]
l=functools.reduce(lambda x,y:x+y,nums,10)
print(l)

#  Consider the code below:
# nums = [[1, 2], [3, 4], [5, 6]] result = list(map(lambda x: x.append(10), nums))
# print("Result:", result) print("Nums:", nums)
# Questions
# • What will be the output of result?
# • What will be the output of nums?
# • Why does map() behave this way with list.append()?
# • How can you modify the lambda so that nums is not changed
nums = [[1, 2], [3, 4], [5, 6]]
result = list(map(lambda x: x.append(10), nums))
print("Result:", result)
print("Nums:", nums)

