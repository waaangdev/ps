import sys
from collections import deque
n = int(input())
li=sorted(list(map(int,input().split())))
print(max([li[i]+li[-1-i] for i in range(n)])-min([li[i]+li[-1-i] for i in range(n)]))