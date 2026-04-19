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

point_su,way_su = map(int,sys.stdin.readline().split())

way = [[] for i in range(point_su)]

for i in range(way_su):
    inp = list(map(int,sys.stdin.readline().split()))
    way[inp[0]-1].append([inp[1]-1,inp[2]])
    way[inp[1]-1].append([inp[0]-1,inp[2]])

st1,st2 = map(int,sys.stdin.readline().split())
st1-=1
st2-=1

point = dijkstra(way,point_su,st1)
point2 = dijkstra(way,point_su,st2)

r = -1
r1 = -1
rr = -2

for i in range(point_su):
    if(i != st1 and i != st2 and (r == -1 or r > point[i]+point2[i]) and point[i] != -1 and point2[i] != -1):
        r = point[i]+point2[i]

for i in range(point_su):
    if(point[i]+point2[i] == r and point[i] <= point2[i] and i != st1 and i != st2 and point[i] != -1 and point2[i] != -1):
        if(r1 == -1 or r1 > point[i]):
            r1 = point[i]
            rr = i
            
print(rr+1)