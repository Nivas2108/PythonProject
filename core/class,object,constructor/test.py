# import sys
# import current
# print(current.__name__)
# # print(__name__)
# module_name=input()
# import importlib as il
# curr=il.import_module(module_name)
# il.reload(curr)
# print(il.__all__)
# print(sys.modules.pop(module_name))
# import current as c
# class B(c.A):
#     pass
# obj=B()
# # print(c.__dict__)
# print(c.__name__)

# 1. Write a Python program that attempts to dynamically import a module at
# runtime. The program should only import the module if it actually exists;
# otherwise, it should print "Module does not exist".
import importlib as il
try:
    module_name=input()
    il.import_module(module_name)
except ModuleNotFoundError:
    print("module does not exist")

# 2. Create a Python package that contains two or more modules. Each module should
# define classes with attributes and methods. Then create another module outside
# the package, import the package modules, and create a subclass that inherits
# from at least one of the classes. Finally, create objects of both parent and
# child classes.
