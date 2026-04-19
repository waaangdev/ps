import sys
from collections import deque

# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

n = int(input())
li = [list(map(int,sys.stdin.readline().split())),[],[]]
rl = ""
r = 0
for i in range(n):
    idx = 0
    if((n-i) not in li[0]):idx = 1

    while(li[idx][-1]!=(n-i)):
        li[1-idx].append(li[idx][-1])
        rl+=F"{idx+1} {1-idx+1}\n"
        li[idx].pop()
        r+=1
    li[2].append(li[idx][-1])
    li[idx].pop()
    rl+=F"{idx+1} {3}\n"
    r+=1
print(r,"\n"+rl)