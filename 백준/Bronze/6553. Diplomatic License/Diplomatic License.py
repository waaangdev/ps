import sys
from collections import deque
import random
import math
import heapq

#ABCXXX - X

#n = int(sys.stdin.readline())
#li = list(map(int,sys.stdin.readline().split()))
#st = sys.stdin.readline().strip()

#sys.setrecursionlimit(100001)


inpl = [*open(0)]

for inp in inpl:
    inp = list(map(int,inp.split()))
    inp2 = []
    n = inp[0]
    for i in range(n):
        inp2.append([inp[1+i*2],inp[1+i*2+1]])

    inner=[]
    print(n,end=' ')
    for i in range(n):
        inner.append([(inp2[(i+1)%n][0]+inp2[i][0])/2,(inp2[(i+1)%n][1]+inp2[i][1])/2])
        print("{0:6f} {1:6f}".format(inner[i][0],inner[i][1]),end = " ")
    print()
    