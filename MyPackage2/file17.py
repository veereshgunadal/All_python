from MyPackage1.MyHalfPackage import *

print("-"*20+" from MyPackage1 import * "+"-----"+"  "+"-"*20)
print(dir())

print(module4.var4)
print(module4.func4())
a = module4.Ab4()
print("class - ",a.Ab_func4())