import sys
#from collections import deque
a = int(input())
d = [0 for i in range(a)]
li = list(map(int,input().split()))
ms = 0
s = 0
for i in li:
    if(d[i-1] == 0):
        s+=1
        ms = max(ms,s)
        d[i-1] = 1
    else:
        s-=1
        d[i-1] = 0
print(ms)