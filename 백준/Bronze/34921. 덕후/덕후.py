import sys
from collections import deque

# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))


a,t = list(map(int,sys.stdin.readline().split()))
print(max(0,10+2*(25-a+t)))