import sys
from collections import deque
import random
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

sys.setrecursionlimit(50001)

li = [0b00000,0b00001,0b00010,0b00100,0b00101,0b01000,0b01001,0b01010,0b10000,0b10001,0b10010,0b10100,0b10101]
li2 = [2**i for i in range(5)]
coll = [[] for i in range(13)]
for i in range(13):
    for j in range(13):
        if(li[i]&li[j] == 0): coll[i].append(j)

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    maps = []
    for i in range(5):
        maps.append(list(map(int,sys.stdin.readline().split())))
    mm = [[0 for i in range(13)] for i in range(n)]

    for i in range(n):
        for k in range(13):
            mm[i][k] = sum([maps[j][i]*((li[k]&li2[j])!=0) for j in range(5)])
            mm[i][k]+= max([mm[i-1][j] for j in coll[k]] )
    
    
    print(max(mm[-1]))