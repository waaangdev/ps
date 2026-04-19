import sys
from collections import deque

# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    p = []
    bang = [1 for i in range(n+2)]
    for i in range(n+2):
        p.append(list(map(int,sys.stdin.readline().split())))
    q = deque([0])
    bang[0] = 0
    while(q):
        qpop = q.popleft()
        for i in range(n+2):
            if(bang[i]):
                if(abs(p[qpop][0]-p[i][0])+abs(p[qpop][1]-p[i][1]) <= 1000):
                    q.append(i)
                    bang[i]=0
    if(bang[n+1]):
        print("sad")
    else:
        print("happy")