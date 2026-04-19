
import sys
from collections import deque

a,b = map(int,sys.stdin.readline().split())

li1 = sys.stdin.readline().split()
li2 = set(sys.stdin.readline().split())

r = b
for i in range(b):
    if(li1[i] in li2):
        r-=1
print(r)
        
    