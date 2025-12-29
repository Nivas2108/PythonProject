# 1.  Use map() with a lambda to add 5 to every element of the following nested
# list [[1, 2], [3, 4], [5, 6]]
# from functools import reduce
# from operator import truediv

l=[[1,2],[3,4],[5,6]]
l2=list(map(lambda x:list(map(lambda y:y+5,x)),l))
print(l2)
# 2.  Given a dictionary: d = {"apple": 100, "banana": 40, "cherry": 150} . Use
# filter() to keep only the keys whose values are greater than 50.
d={"apple":100,"banana":40,"cherry":150}
d2=dict(filter(lambda x:x[1]>50,d.items()))
# print(d.values())
# for i in d.values():
#     print(i)
# d3=dict(filter(lambda x:x>50,d.values()))
print(d2)
# 3.  Use functools.reduce() with a lambda to find the largest number from a given
# list Dynamically
import functools
l=[3,7,1,2,10]
def fun(a,b):
    if a>b:
        return a
    return b
x=functools.reduce(fun,l)
print(x)
######lambda for 3rd question
from functools import reduce
l=[3,70,19,81,52,10]
x=reduce(lambda a,b:a if a>b else b,l)
print(x)
# 4.  What happens if the lambda passed to reduce() accepts only one parameter or
# three parameters? Explain the output or error.
######we have to take only two values for reduce funtion,if we take 1 or 3,4 etc., parameters we get errors
# 5.  Use map() on a string to convert each character into its ASCII value
# (using ord()). Print the result list.
l=["A","b","c","d"]
print(list(map(lambda a:ord(a),l)))
# 6.  Use filter() to remove all vowels from a string and print the final string
s="nivas"
l=["a","e","i","o","u"]
s1="aeiou"
x=list(filter(lambda i:i not in l,s ))
y=list(filter(lambda j:j in s1,s))
print(x)
print(y)
print(x+y)##concatenation
# 7.  Use reduce() to concatenate a list of characters into a single string.
# Example input: ['P', 'y', 't', 'h', 'o', 'n'].
l=['p','y','t','h','o','n']
from functools import reduce
x=reduce(lambda a,b:a+b,l)
print(x)
# 8.  Given a list of integers, use map() with id() to print the memory address###id() is used for address
# of each element.
# Example: [10, 350, 10, 350, 20] — explain why some addresses repeat.
l=[10,350,10,350,20]
print(list(map(lambda x:id(x),l)))
# 9.  Explain the difference between:
# map(str, [1, 2, 3])
# map(lambda x: str(x), [1, 2, 3])
# Which one is faster and why?
print(list(map(str,l)))
print(list(map(lambda x:str(x),l)))###this is faster
# 10.  Given a list of numbers:
# [5, 10, 15, 20, 25, 30]
# Perform the following in a single pipeline:
# • Use map() to square each number
# • Use filter() to keep only numbers divisible by 5
# • Use reduce() to calculate the sum of remaining numbers
l=[5, 10, 15, 20, 25, 30]
print(reduce(lambda a,b:a+b,filter(lambda x:x%5==0,map(lambda x:x**2,l))))







