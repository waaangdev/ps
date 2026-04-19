
import sys
from collections import deque

a = sys.stdin.readline().strip()
d = 1
for i in range(len(a)//2):
    if(a[i] != a[len(a)-1-i]):
        d = 0
print(d)

