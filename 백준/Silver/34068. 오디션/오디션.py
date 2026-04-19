

#e
import sys
from collections import deque

n,m = map(int,sys.stdin.readline().strip().split())
li = [0]*n
for i in range(m):
    inp1,inp2 = map(int,sys.stdin.readline().strip().split())
    inp1 -= 1
    li[inp1] += 1
li.sort()
his = -1
r = 0
for i in range(n):
    tar = his+1
    r += max(0,tar-li[i])
    li[i] = max(li[i],tar)
    his = li[i]
print(r)

