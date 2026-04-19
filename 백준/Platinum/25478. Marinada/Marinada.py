"Marinada"

import sys
from collections import deque

def soon(st,bang):
    if(bang == pow(2,point_su)-1):
        return way[st][0]
    if(jegi[bang][st] != 0):
        return jegi[bang][st]
    r = 1000000000000000000
    for i in range(2,point_su+2):
        if(bang & (1 << (i-2)) == 0 and i != st):
            r = min(r,soon(i,bang | (1 << (i-2)))+way[st][i])
    jegi[bang][st] = r
    return r
    
sys.setrecursionlimit(10000)

m_sero,m_garo,point_su = map(int,sys.stdin.readline().split())

way = [[0 for i in range(point_su+2)] for i in range(point_su+2)]
jegi = [[0 for j in range(point_su+2)] for i in range(pow(2,point_su+2))]
m = [[-1 for i in range(m_garo)] for i in range(m_sero)]
count = 2
ang = [[1,0],[0,-1],[0,1],[-1,0]]
key = deque([])

for i in range(m_sero):
    inp =  sys.stdin.readline()
    for j in range(m_garo):
        if(inp[j] == 'I'):
            m[i][j] = 0
        elif(inp[j] == 'U'):
            key.appendleft([i,j])
            m[i][j] = 1
        elif(inp[j] == 'N'):
            m[i][j] = count
            key.append([i,j])
            count += 1
        elif(inp[j] == '#'):
            m[i][j] = -2

for k in range(point_su+1):
    q = deque([key.popleft()])
    bang1 = [[True for i in range(m_garo)] for j in range(m_sero)]
    time = 0
    while q:
        time +=1
        for i in range(len(q)):
            popq = q.popleft()
            for j in range(4):
                dum_a = popq[0]+ang[j][0]
                dum_b = popq[1]+ang[j][1]
                if(dum_a < m_sero and dum_a >= 0 and dum_b < m_garo and dum_b >= 0):
                    dum = m[dum_a][dum_b]
                    if(bang1[dum_a][dum_b] and dum != -2):
                        bang1[dum_a][dum_b] = False
                        if(dum != -1):
                            way[k+1][dum] = time
                            way[dum][k+1] = time
                        q.append([dum_a,dum_b])
#print(way)
print(soon(1,0))