import sys
from collections import deque
import random
import math
import heapq

#ABCXXX - X

#n = int(sys.stdin.readline())
#li = list(map(int,sys.stdin.readline().split()))
#st = sys.stdin.readline().strip()

sys.setrecursionlimit(500001)

n = int(sys.stdin.readline())
li =[]
li2 = set()
for i in range(n):
    x,r = list(map(int,sys.stdin.readline().split()))
    li.append([x-r,i])
    li.append([x+r,i])
    li2.add(x-r)
    li2.add(x+r)
if(len(li)!=len(li2)):
    print("NO")
else:
    li.sort()
    li3 = [0]*n
    for i in range(n*2):
        li3[li[i][1]]=i
    
    def sol(l,r):
        #print(l,r)
        if(l == r):return 1
        idx = l
        while idx <r:
            if(li3[li[idx][1]] >= r):
                return 0
            if(sol(idx+1,li3[li[idx][1]])==0):return 0
            idx=li3[li[idx][1]]+1
        return 1
    print(["NO","YES"][sol(0,n*2)])
    #print(li)