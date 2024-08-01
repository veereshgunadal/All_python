from MyPackage1 import *

print("-"*20+" from MyPackage1 import * "+"-----"+" import modules that are inside __all__ , __init__.py has __all__ list variable with module names "+"-"*20)

print(module3.var)
print(module3.func())
a = module3.Ab()
print("class - ",a.Ab_func())