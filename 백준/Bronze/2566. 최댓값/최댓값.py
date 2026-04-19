
import sys
from collections import deque

m = -1
m1 = -1
m2 = -1

for i in range(9):

    a = list(map(int,input().split()))
    for j in range(9):
        if(a[j] > m):
            m = a[j]
            m1 = i+1
            m2 = j+1

print(m)
print(m1,m2)