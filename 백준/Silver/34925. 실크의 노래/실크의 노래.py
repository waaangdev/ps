import sys
from collections import deque

# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))


h,s = list(map(int,sys.stdin.readline().split()))

if(h <= 2):
    print(1)
elif(h == 3):
    print(s+2)
elif(h == 4):
    print(s+2)
else:
    print((h+s*3)//2+(h+s*3)%2)