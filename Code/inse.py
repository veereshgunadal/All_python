import numpy as np
import random

l = [1,4,3,2,10,20,5,90,6,8,0]

def bub(l):
    for i in range(len(l)-1, 0, -1):
        for j in range(i):
            if (l[j] > l[j+1]):
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
        print(f"after inner loop - {l}")
    print(f"Bubble sort {l}")

bub(l)

l = [1,4,3,2,10,20,5,90,6,8,0]
def sel(l):
    for i in range(len(l)-1):
        min = l[i]
        for j in range(i+1, len(l)):
            if min > l[j]:
                temp = min
                min = l[j]
                l[j] = temp
        l[i] = min
        print(f"after inner loop - {l}")
    print(f"Selection sort {l}")

#sel(l)

#l = [1,4,3,2,10,20,5,90,6,8,0]
l = [5,4,10,1,6,2]
def ins(l):
    for i in range(1, len(l)):
        for j in range(i, 0 ,-1):
            if (l[j] < l[j-1]):
                temp = l[j-1]
                l[j-1] = l[j]
                l[j] = temp
        print(f"after inner loop - {l}")
    print(f"Insertion sort {l}")

ins(l)