import sys
from collections import deque

# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))
n,h = list(map(int,sys.stdin.readline().split()))
lines = [[],[]]
for i in range(n):
    dum = int(sys.stdin.readline())
    lines[i%2] += [dum]
for i in range(2):
    lines[i] = deque(sorted(lines[i]))

r = n//2
minr = n+1
rl =0
for i in range(1,h+1):
    while(lines[1]):
        dum = lines[1].pop()
        if(dum!=h-i+1):
            lines[1].append(dum)
            break
        r+=1
    #print(lines,r)
    if(minr > r):
        minr = min(minr,r)
        rl = 1
    elif(minr == r):
        rl += 1
    
    while(lines[0]):
        dum = lines[0].popleft()
        if(dum!=i):
            lines[0].appendleft(dum)
            break
        r-=1
    
print(minr,rl)

