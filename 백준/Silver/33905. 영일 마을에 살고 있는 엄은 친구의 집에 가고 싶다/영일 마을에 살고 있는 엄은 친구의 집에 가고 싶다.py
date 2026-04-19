import sys
from collections import deque

# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))
n,m,k = list(map(int,sys.stdin.readline().split()))
ways = [[] for i in range(n+1)]
no = [1 for i in range(n+1)]
for i in range(m):
    a,b= list(map(int,sys.stdin.readline().split()))
    ways[a-1].append(b-1)
    ways[b-1].append(a-1)
for i in list(map(int,sys.stdin.readline().split())):
    no[i-1]=0
no[0]=0
q=deque([0])
r=0
while(q):
    qpop = q.popleft()
    for i in ways[qpop]:
        if(no[i]):
            no[i]=0
            q.append(i)
            r+=1

print(r)