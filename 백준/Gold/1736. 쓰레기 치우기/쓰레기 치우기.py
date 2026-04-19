import sys
import heapq
from collections import deque
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

n,m = list(map(int,sys.stdin.readline().split()))
maps = []
li = []
for i in range(n):
    maps.append(list(map(int,sys.stdin.readline().split())))
    li.append(sum(maps[-1]))
if(sum(li) == 0):
    print(0)
else:
    r = 0
    while sum(li) != 0:
        r+=1
        idx = 0
        for i in range(n):
            while (1):
                #print(i,idx)
                li[i]-=maps[i][idx]
                maps[i][idx] = 0
                if(sum(maps[i][idx:]) == 0):
                    break
                idx+=1
        
    print(r)