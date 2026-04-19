import sys
#from collections import deque
n,b = map(int,input().split())
li2 = [1 for j in range(n*2-1)]
m1 = [[1 for j in range(n)] for i in range(n)]
for i in range(b):
    li = list(map(int,sys.stdin.readline().strip().split()))
    li = [0]*li[0]+[1]*li[1]+[2]*li[2]
    for j in range(n*2-1):
        li2[j] += li[j]

for j in range(n):
    print(li2[n-1-j],*li2[n:])
