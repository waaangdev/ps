import sys
from collections import deque

# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))
n,m = list(map(int,sys.stdin.readline().split()))
li1 = list(map(int,sys.stdin.readline().split()))+list(map(int,sys.stdin.readline().split()))
li = [0 for i in range(n)]
r = 0
for _ in range(6**n):
    #print(li)
    prev = li[0]+1
    dum  =0
    for i in range(n):
        if(li[i]%3==prev%3):
            dum+=li1[li[i]]//2
        else:
            dum+=li1[li[i]]
        prev = li[i]
    if(dum >= m):
        r+=1
    li[0]+=1
    for i in range(n-1):
        if(li[i]==6):
            li[i]=0
            li[i+1]+=1
print(r)