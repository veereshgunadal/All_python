import os

f = open("C:\\Users\\002MKJ744\\Documents\\All Python\\Code\\a.txt",'r')
#print(f.readlines())
#print(list(f))
print(f.tell())

print(f.read())
print(f.tell())
f.seek(3)
print(f.tell())
f.close()


