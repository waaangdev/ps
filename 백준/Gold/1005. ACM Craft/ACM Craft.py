"ACM Craft"

import sys
from collections import deque
import heapq

case = int(sys.stdin.readline())

for _ in range(case):
    point_su,way_su = map(int,sys.stdin.readline().split())
    point = list(map(int,sys.stdin.readline().split()))
    way = [[] for i in range(point_su)]
    line_sort = 0
    q = []
    duml = [0]*point_su
    for i in range(way_su):
        inp = list(map(int,sys.stdin.readline().split()))
        way[inp[0]-1].append(inp[1]-1)
        duml[inp[1]-1]+=1
    
    bang = [-1 for i in range(point_su)]
    for i in range(point_su):
        if(duml[i]==0):
            heapq.heappush(q,(point[i],i))
            bang[i] = point[i]
    
    end = int(sys.stdin.readline())

    
    while q:
        qpop = heapq.heappop(q)

        for j in way[qpop[1]]:
            if(bang[j] == -1):
                duml[j]-=1
                if(duml[j]==0):
                    bang[j] = qpop[0]+point[j]
                    heapq.heappush(q,(bang[j],j))
    print(bang[end-1])
        