import MyPackage1.module1

print("-"*20+" import module1,module2 "+"-----"+" imports everything "+"-"*20)
print("variable - ",MyPackage1.module1.var)
print("method - ",MyPackage1.module1.func())
a = MyPackage1.module1.Ab()
print("class - ",a.Ab_func())