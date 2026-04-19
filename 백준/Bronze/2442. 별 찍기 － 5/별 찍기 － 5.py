
import sys
from collections import deque

a = int(sys.stdin.readline())

b = 1
for i in range(a):
    print(' '* (a-i-1),end = '')
    print('*'* b)
    b+=2