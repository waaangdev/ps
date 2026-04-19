import sys
from collections import deque
t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,sys.stdin.readline().strip().split()))
    li2 = "abcdefghijklmnopqrstuvwxyz"
    for i in li:
        print(li2[i],end='')
        li2 = li2[i]+li2[:i]+li2[i+1:]
    print()