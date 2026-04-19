import sys
from collections import deque

# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))


li = [100000000000 for i in range(101)]
n,m = list(map(int,sys.stdin.readline().split()))
ways = [[] for i in range(101)]
for i in range(n+m):
    a,b = list(map(int,sys.stdin.readline().split()))
    ways[a] += [b]

q = deque([[1,0]])
while q:
    lenq = len(q)
    for _ in range(lenq):
        qpop,qpop2 = q.popleft()
        if(ways[qpop] == []):
            for i in range(1,7):
                if(qpop+i > 100):break
                if(li[qpop+i] > qpop2+1):
                    li[qpop+i] =  qpop2+1
                    q.append([qpop+i,qpop2+1])
        for i in ways[qpop]:
            if(li[i] > qpop2):
                li[i] =  qpop2
                q.append([i,qpop2])
print(li[100])