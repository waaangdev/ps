#g
import sys
from collections import deque

#n,k = map(int,sys.stdin.readline().strip().split())
n = int(input())
li = []
for i in range(n):
    li.append(int(input()))
li2 = sorted(li[:])
if(li[0] == li2[0]):
    print("ez")
elif(li[0] == li2[-1]):
    print("hard")
else:
    print("?")
