import functools
# l=[[1,2,3,4],[5,6],[7,8,9]]
# l2=list(map(lambda x:list(map(lambda y:y+5,x)),l))
# print(l2)
# res=[]
# for i in range(len(li)):
#     res.append(li[i]**3)
# # print(res)
# def cube(x):
#     return x**3
# res=list(map(cube,li))
# print(res)
# marks=[35,47,88,22,32]
# res=list(filter(lambda x:x>=35,marks))
# print(res)
# res=functools.reduce(lambda a,b:a+b,marks)
# print(res)
l=[1,2,3,4,7]
l2=list(map(lambda x:x+5,l))
print(l2)
l=[20,30,47]
l2=list(filter(lambda x:x<=20,l))
print(l2)
l=[1,2,45,67]
l2=functools.reduce(lambda a,b:a*b,l)
print(l2)