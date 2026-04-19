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

n,t = list(map(int,sys.stdin.readline().split()))
li = list(map(int,sys.stdin.readline().split()))
ql = []
rl = [0]*t
for i in range(t):
    inp = list(map(int,sys.stdin.readline().split()))
    inp[0]-=1
    ql.append((inp,i))

ql.sort(key=lambda x:x[0][0]//317*1000000+x[0][1])

li2 =[0]*1000001
r = 0
shis = -1
for i in range(t):
    if(shis//317 != ql[i][0][0]//317):
        li2 =[0]*1000001
        r = 0
        for j in range(ql[i][0][0],ql[i][0][1]):
            his = li2[li[j]]
            li2[li[j]]+=1
            r+=(li2[li[j]]*li2[li[j]]-his*his)*li[j]
    else:
        if(shis < ql[i][0][0]):
            for j in range(shis,ql[i][0][0]):
                his = li2[li[j]]
                li2[li[j]]-=1
                r+=(li2[li[j]]*li2[li[j]]-his*his)*li[j]
        else:
            for j in range(ql[i][0][0],shis):
                his = li2[li[j]]
                li2[li[j]]+=1
                r+=(li2[li[j]]*li2[li[j]]-his*his)*li[j]

        for j in range(ql[i-1][0][1],ql[i][0][1]):
            his = li2[li[j]]
            li2[li[j]]+=1
            r+=(li2[li[j]]*li2[li[j]]-his*his)*li[j]

    shis = ql[i][0][0]
    rl[ql[i][1]]=str(r)
print("\n".join(rl))