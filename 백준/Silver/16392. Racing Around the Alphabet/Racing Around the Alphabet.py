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

a = 6.73198425769
l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ '"
l = {l[i]:i for i in range(len(l))}
for _ in range(int(input())):
    st = sys.stdin.readline().strip()
    r = 1
    for i in range(len(st)-1):
        dum = abs(l[st[i]]-l[st[i+1]])
        r+=1+min(dum,len(l)-dum)*a/15
    print(r)