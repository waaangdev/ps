import sys
from collections import deque

n = int(input())
for i in range(1,10000000):
    if(n <= i):
        if(i%2 == 0):
            print(F'{n}/{i-n+1}')
        else:
            print(F'{i-n+1}/{n}')
        break
    else:
        n-=i