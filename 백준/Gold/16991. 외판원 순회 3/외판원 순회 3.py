"외판원 순회"

import sys
import math

def soon(st,bang):
    if(bang == pow(2,point_su)-1):
        if(way[st][0] == 0):
            return 1000000000000000000
        return way[st][0]
    if(jegi[bang][st] != 0):
        return jegi[bang][st]
    r = 1000000000000000000
    for i in range(point_su):
        if(bang & (1 << i) == 0 and way[st][i] != 0):
            r = min(r,soon(i,bang | (1 << i))+way[st][i])
    jegi[bang][st] = r
    return r
    
sys.setrecursionlimit(10000)

point_su = int(sys.stdin.readline())
way = [[0 for i in range(point_su)] for i in range(point_su)]
xy = [[] for i in range(point_su)]
jegi = [[0 for j in range(point_su)] for i in range(pow(2,point_su))]
for i in range(point_su):
    xy[i] = list(map(int,sys.stdin.readline().split()))
for i in range(point_su):
    for j in range(point_su):
        way[i][j] = math.sqrt((xy[i][0] - xy[j][0])**2+(xy[i][1] - xy[j][1])**2)

print(soon(0,(1<<0)))