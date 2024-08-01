from MyPackage1 import module1

print("-"*20+" from MyPackage1 import module1 "+"-----"+" imports module1 everything  "+"-"*20)

print("variable - ",module1.var)
print("method - ",module1.func())
a = module1.Ab()
print("class - ",a.Ab_func())