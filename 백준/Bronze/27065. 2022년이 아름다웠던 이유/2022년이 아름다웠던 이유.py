import sys
from collections import deque

# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))
li = [[] for i in range(5001)]
for i in range(1,5001):
    for j in range(i+i,5001,i):
        li[j].append(i)
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    r = "Good Bye"
    if(sum(li[n]) <= n):
        r="BOJ 2022"
    for i in li[n]:
        if(sum(li[i]) > i):
            r="BOJ 2022"
    print(r)