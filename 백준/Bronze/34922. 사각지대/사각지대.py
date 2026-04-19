import sys
from collections import deque

# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))


w,h = list(map(int,sys.stdin.readline().split()))
r = int(sys.stdin.readline())
print(w*h-r**2*3.141592/4)