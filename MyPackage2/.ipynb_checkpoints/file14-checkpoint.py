from MyPackage1 import *

print("-"*20+" from MyPackage1 import * "+"-----"+" import __init__.py has content with import MyPackage1.module1, MyPackage1.module2 "+"-"*20)

print(MyPackage1)
print(MyPackage1.A)
print(MyPackage1.module3.var)
print(MyPackage1.module3.func())
a = MyPackage1.module3.Ab()
print("class - ",a.Ab_func())