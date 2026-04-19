import sys
#from collections import deque
a = int(input())
d = [1 for i in range(a-1)]
b = int(input())
for i in range(b):
    x,y = map(int,input().split())
    x-=1
    y-=1
    for j in range(x,y):
        d[j] = 0
re = 0
for i in range(a-1):
    if(d[i] == 1):
        re+=1
print(re+1)