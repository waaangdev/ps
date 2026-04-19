import sys
from collections import deque

# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))


h,m = list(map(int,sys.stdin.readline().split(":")))
if(h > 12): h -= 12
t = h*60+m
h2,m2 = list(map(int,sys.stdin.readline().split(":")))
if(h2 > 12): h2 -= 12
t2 = h2*60+m2

if(t2 < t): t2,t=t,t2

print(min(6*(abs(t-t2)),6*(t+(12*60-t2))))