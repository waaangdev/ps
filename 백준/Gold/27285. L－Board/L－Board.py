import sys
import heapq
n,m = list(map(int,sys.stdin.readline().split()))
maps = []
maxs = [[[0,0,0,0] for i in range(m)] for i in range(n)]
for i in range(n):
    maps.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    maxs[i][m-1][0] = maps[i][m-1]
    for j in range(m-2,-1,-1):
        maxs[i][j][0] = maps[i][j]+max(0,maxs[i][j+1][0])

    maxs[i][0][1] = maps[i][0]
    for j in range(1,m):
        maxs[i][j][1] = maps[i][j]+max(0,maxs[i][j-1][1])

for j in range(m):
    maxs[n-1][j][2] = maps[n-1][j]
    for i in range(n-2,-1,-1):
        maxs[i][j][2] = maps[i][j]+max(0,maxs[i+1][j][2])

    maxs[0][j][3] = maps[0][j]
    for i in range(1,n):
        maxs[i][j][3] = maps[i][j]+max(0,maxs[i-1][j][3])

r = -100000000000
for i in range(n):
    for j in range(m):
        r = max(r,maxs[i][j][0]+maxs[i][j][2]-maps[i][j])
        r = max(r,maxs[i][j][0]+maxs[i][j][3]-maps[i][j])
        r = max(r,maxs[i][j][1]+maxs[i][j][2]-maps[i][j])
        r = max(r,maxs[i][j][1]+maxs[i][j][3]-maps[i][j])
print(r)