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

for c in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    li={}
    set1 = set()
    set2 = set()
    for i in range(n):
        s,e = sys.stdin.readline().strip(),sys.stdin.readline().strip()
        set1.add(s)
        set2.add(e)
        li[s]=e
    st = (set1-set2).pop()
    print(f"Case #{c+1}: ",end ="")
    for i in range(n):
        print(f"{st}-{li[st]}",end =" ")
        st=li[st]
    print()