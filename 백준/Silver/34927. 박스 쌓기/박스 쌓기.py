import sys
from collections import deque

# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))


n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
li.sort()
s = 0
r = 0
for i in range(n):
    if(li[i] >= s):
        s+=li[i]
        r+=1
print(r)