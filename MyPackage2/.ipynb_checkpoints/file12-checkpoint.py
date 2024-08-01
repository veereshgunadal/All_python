import MyPackage1

print("-"*20+" import MyPackage1 "+"-----"+" import only __init__.py file content is import module1,module2  "+"-"*20)

print(MyPackage1)
print(MyPackage1.A)
print(MyPackage1.module1.var)
print(MyPackage1.module1.func())
a = MyPackage1.module1.Ab()
print("class - ",a.Ab_func())