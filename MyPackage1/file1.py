import module1,module2

print("-"*20+" import module1,module2 "+"-----"+" imports everything "+"-"*20)
print("variable - ",module1.var)
print("_us - ",module1._us)
print("method - ",module1.func())
a = module1.Ab()
print("class - ",a.Ab_func())