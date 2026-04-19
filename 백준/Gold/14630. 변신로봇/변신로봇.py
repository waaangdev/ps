"연예인은 힘들어"

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

n = int(sys.stdin.readline())

point = []
way = [[] for i in range(n)]

for i in range(n):
    point.append(sys.stdin.readline().strip())

for i in range(n):
    for j in range(n):
        dum = 0
        for k in range(len(point[i])):
            dum += (int(point[i][k])-int(point[j][k]))**2
        way[i].append([j,dum])

st1,st2 = map(int,sys.stdin.readline().split())
st1-=1
st2-=1

point2 = dijkstra(way,n,st1)
            
print(point2[st2])