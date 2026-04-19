"외판원 순회"

import sys

def soon(st,bang):
    if(bang == pow(2,point_su-1)-1):
        if(way[st][0] == 0):
            return 1000000000000000000
        return way[st][0]
    if(jegi[bang][st] != 0):
        return jegi[bang][st]
    r = 1000000000000000000
    for i in range(1,point_su):
        if(bang & (1 << (i-1)) == 0 and way[st][i] != 0):
            r = min(r,soon(i,bang | (1 << (i-1)))+way[st][i])
    jegi[bang][st] = r
    return r
    
sys.setrecursionlimit(10000)

point_su = int(sys.stdin.readline())
way = [[] for i in range(point_su)]
jegi = [[0 for j in range(point_su)] for i in range(pow(2,point_su))]
for i in range(point_su):
    way[i] = list(map(int,sys.stdin.readline().split()))

print(soon(0,0))