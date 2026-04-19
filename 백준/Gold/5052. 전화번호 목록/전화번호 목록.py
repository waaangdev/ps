import sys
from collections import deque

# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

for _ in range(int(input())):
    n = int(sys.stdin.readline())
    li = []
    for i in range(n):
        li.append(sys.stdin.readline().strip())
    li.sort()
    li2 = [0,[[] for i in range(10)]]
    r = "YES"
    for i in range(n):
        p = li2
        for j in li[i]:
            if(p[1][int(j)] == []):
                p[1][int(j)] = [0,[[] for i in range(10)]]
            if(p[0]==1):
                r = "NO"
            p=p[1][int(j)]
        p[0]=1
    print(r)