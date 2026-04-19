import sys
from collections import deque
import random
import math
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

#sys.setrecursionlimit(100001)

# for i in range(int(sys.stdin.readline())):

li = []
for i in range(10):
    r = 0
    for j in range(i*100000,i*100000+100000):
        r += str(j).count('0')
    li.append(r)
#print(li)

for _ in range(int(sys.stdin.readline())):
    n,m = list(map(int,sys.stdin.readline().split()))
    r = 0
    i = n
    while (i<=m):
        if(i%100000 == 0 and i+100000 <= m):
            r+=li[i//100000]
            i+=100000
        else:
            r+=str(i).count('0')
            i+=1
    print(r)