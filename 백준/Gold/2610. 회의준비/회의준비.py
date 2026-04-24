import sys
from collections import deque


    

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

li = [-1 for i in range(n)]
bang = [0 for i in range(n)]
ways = [[] for i in range(n)]
group = []


for i in range(m):
    c,d = map(int,sys.stdin.readline().split())
    ways[c-1].append(d-1)
    ways[d-1].append(c-1)

r = 0

for i in range(n):
    q = deque([[i,0]])
    bang = [0 for i in range(n)]
    bang[i]=1
    group_c=li[i]
    if(li[i]==-1):
        group_c=len(group)
        li[i]=group_c
        group.append([-1,100000])

    t = 0
    while q:
        qpop = q.popleft()
        for j in ways[qpop[0]]:
            if(bang[j]==0):
                li[j]=group_c
                bang[j]=1
                q.append([j,qpop[1]+1])
                t=max(t,qpop[1]+1)
    if(group[group_c][1] > t):
        group[group_c] = [i,t]
#print(group)
group.sort()
print(len(group))
for i in group:
    print(i[0]+1)
        
