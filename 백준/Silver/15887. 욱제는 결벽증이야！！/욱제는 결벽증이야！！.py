
import sys
from collections import deque

a = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
li2 = []

for i in range(a):
    for j in range(a-i-1):
        if(li[j] > li[j+1]):
            li[j],li[j+1] = li[j+1],li[j]
            li2.append([j+1,j+2])

print(len(li2))
for i in li2:
    print(*i)