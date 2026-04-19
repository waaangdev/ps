"총깡 총깡"

import sys
from collections import deque

def dijkstra(dway,dpoint_su,dst):
    dpoint = [-1 for i in range(dpoint_su)]
    dq = [i for i in range(dpoint_su)]
    
    dmin = 0
    dmin_i= dst
    dpoint[dmin_i] = 0
    while dq:
        dqpop = dq[dmin_i]
        del dq[dmin_i]
        
        for i in range(len(dway[dqpop])):
            if(dpoint[dway[dqpop][i][0]] == -1 or dpoint[dway[dqpop][i][0]] > dpoint[dqpop] + dway[dqpop][i][1]):
                dpoint[dway[dqpop][i][0]] = dpoint[dqpop]+ dway[dqpop][i][1]
    
        dmin = -1
        dmin_i = -1
        
        for i in range(len(dq)):
            if(dpoint[dq[i]] != -1 and (dmin == -1 or dpoint[dq[i]] < dmin)):
                dmin = dpoint[dq[i]]
                dmin_i = i
                
        if(dmin_i == -1): break
    
    return dpoint

point_su,way_su = map(int,sys.stdin.readline().split())

point = [0] * point_su
way = [[] for i in range(point_su)]


st1 =int(sys.stdin.readline())
st1-=1

h_su = int(sys.stdin.readline())
h = [[],[]]
for i in range(2):
    inp = list(map(int,sys.stdin.readline().split()))
    for j in range(h_su):
        h[i].append(inp[j]-1)

for i in range(way_su):
    inp = list(map(int,sys.stdin.readline().split()))
    way[inp[0]-1].append([inp[1]-1,inp[2]])
    way[inp[1]-1].append([inp[0]-1,inp[2]])



point2 = dijkstra(way,point_su,st1)

minh = 100000000
minh2 = ""
ddd = ["A","B"]
for i in range(2):
    for j in range(h_su):
        if(point2[h[i][j]] < minh and point2[h[i][j]] != -1):
            minh = point2[h[i][j]]
            minh2 = ddd[i]
if(minh2 == ""):
    print(-1)
else:
    print(minh2)
    print(minh)