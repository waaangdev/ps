import sys
import heapq
from collections import deque
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

n =0
fibo = [0 for i in range(41)]
fibo[0] = 1
fibo[1] = 1

for i in range(2,41):
    fibo[i] = fibo[i-2]+fibo[i-1]
#print(fibo)
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
dum = 0
r = 1
for i in range(m):
    inp = int(sys.stdin.readline())
    r*=fibo[inp-dum-1]
    dum = inp
r*=fibo[n-dum]
print(r)