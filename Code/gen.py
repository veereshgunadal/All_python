#1
def first_num(num):
    n = 1
    while n <num:
        yield n
        n = n+1

l = first_num(10)
print(type(l))
for i in l:
    print(i)

#2
"""
l = (x*x for x in range(1000000000000000000000000))
print(type(l))
for i in l:
    print(i)
"""

import random
import time

names = ["A", "B", "C"]
subjects = ["mat", "cat", "pat"]

def gene(num):
    for i in range(num):
        person ={ "id":i, "name":random.choices(names), "sub": random.choices(subjects)}
        yield person

t1=time.time()
l = gene(100000)
#for i in l:
#    print(i)
t2=time.time()
print(t2-t1)

def usli(num):
    l1 = []
    for i in range(num):
        person ={ "id":i, "name":random.choices(names), "sub": random.choices(subjects)}
        l1.append(person)
    return l1

t1=time.time()
l2 = usli(100000)
for i in l2:
    print(i)
t2=time.time()

print(t2-t1)
           