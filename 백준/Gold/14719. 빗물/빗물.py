import sys
from collections import deque
n,k = map(int,input().split())
li = list(map(int,input().split()))
s = 0
for i in range(n):
    a = 0
    for j in range(k):
        if(li[j] >= n-i):
            if(a == 0):
                a = 1
            if(a != 0):
                s+=a-1
                a = 1
        elif(a != 0):
            a += 1
print(s)