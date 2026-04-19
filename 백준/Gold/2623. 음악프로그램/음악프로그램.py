"음악프로그램"

import sys
from collections import deque

point_su,way_su = map(int,sys.stdin.readline().split())
way = [[] for i in range(point_su)]
point = [0 for i in range(point_su)]
q = deque([])
bang = [0 for i in range(point_su)]
r = []

for i in range(way_su):
    dum = list(map(int,sys.stdin.readline().split()))
    for j in range(dum[0]-1):
        way[dum[1+j]-1].append(dum[2+j]-1)
        point[dum[2+j]-1] += 1

for i in range(point_su):
    if(point[i] == 0):
        q.append(i)
        bang[i] = 1
        r.append(i+1)
#print(way)
while q:
    #print(q,point)
    lenq = len(q)
    for i in range(lenq):
        qpop = q.popleft()
        for j in range(len(way[qpop])):
            if(bang[way[qpop][j]] == 0):
                point[way[qpop][j]] -= 1
                if(point[way[qpop][j]] == 0):
                    bang[way[qpop][j]] = 1
                    q.append(way[qpop][j])
                    r.append(way[qpop][j]+1)
if(len(r) == point_su):
    for i in range(point_su):
        print(r[i])
else:
    print(0)
        