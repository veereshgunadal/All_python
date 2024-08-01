import MyPackage1.module1

print("-"*20+" import MyPackage1.module1 "+"-----"+" imports everything MyPackage1.module1.var "+"-"*20)
print("variable - ",MyPackage1.module1.var)
print("method - ",MyPackage1.module1.func())
a = MyPackage1.module1.Ab()
print("class - ",a.Ab_func())