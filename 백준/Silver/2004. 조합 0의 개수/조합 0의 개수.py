import sys
from collections import deque
import random
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

sys.setrecursionlimit(100001)

a,b  = list(map(int,sys.stdin.readline().split()))
r = 1
dum10,dum2,dum5 = 0,0,0

for i in range(1,40):
    dum2+=a//(2**i)-((a-b)//(2**i))
    dum5+=a//(5**i)-((a-b)//(5**i))
    #print(i,dum2,dum5)
for i in range(1,40):
    dum2-=b//(2**i)
    dum5-=b//(5**i)

print(min(dum2,dum5))
    