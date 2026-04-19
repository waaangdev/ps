
import sys
from collections import deque

a,b,c = map(int,sys.stdin.readline().split())

if(a+b-1 > c):
    print('NO')
else:
    print('YES')
    for i in range(a):
        print(*[i+j+1 for j in range(b)])