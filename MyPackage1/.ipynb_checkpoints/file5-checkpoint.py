import module3

print("-"*20+" import module3 "+"-----"+" imports all if few named inside __all__ variable in module3 "+"-"*20)

print("variable - ",module3.var)
print("method - ",module3.func())
a = module3.Ab()
print("class - ",a.Ab_func())