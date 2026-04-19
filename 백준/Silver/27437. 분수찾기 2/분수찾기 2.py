import sys
from collections import deque

n = int(input())
dum = 0
while (n > (dum*(dum+1)//2)):dum+=10000
dum-=10000
n -= (dum*(dum+1)//2)
#print(n)
for i in range(dum+1,1000000000000000000000):
    if(n <= i):
        if(i%2 == 0):
            print(F'{n}/{i-n+1}')
        else:
            print(F'{i-n+1}/{n}')
        break
    else:
        n-=i