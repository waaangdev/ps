import sys
from collections import deque

# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))
def asd(a,b):
    if(a%b==0):return b
    return asd(b,a%b)
n,s = list(map(int,sys.stdin.readline().split()))
li=list(map(int,sys.stdin.readline().split()))
for i in range(n):
    li[i] = abs(li[i]-s)
dum = li[0]
for i in range(1,n):
    dum = asd(dum,li[i])
print(dum)