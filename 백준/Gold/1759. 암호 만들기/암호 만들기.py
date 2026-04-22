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

l,c = list(map(int,sys.stdin.readline().split()))
li = sorted(sys.stdin.readline().strip().split())

lae = 0
for i in range(c):
    if(li[i] in "aeiou"):
        lae=i

def sol(idx,idx2,mo,ja):
    #print(idx,idx2,mo)
    if(idx==l):
        if(mo and ja>=2):
            return [""]
        else:
            return []
    dmo=li[idx2] in "aeiou"
    dja=not dmo
    if(idx2==lae and not mo):
        rli = []
        for i in sol(idx+1,idx2+1,mo or dmo,ja+1*dja):
            rli.append(li[idx2]+i)
        return rli
    if(l-idx == c-idx2):
        rli = []
        for i in sol(idx+1,idx2+1,mo or dmo,ja+1*dja):
            rli.append(li[idx2]+i)
        return rli
    rli = []
    for i in sol(idx+1,idx2+1,mo or dmo,ja+1*dja):
        rli.append(li[idx2]+i)
    
    for i in sol(idx,idx2+1,mo,ja):
        rli.append(i)
    return rli

for i in sol(0,0,0,0):
    print(i)