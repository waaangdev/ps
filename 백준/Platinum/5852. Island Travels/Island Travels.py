"Island Travels"

import sys
from collections import deque

def soon(st,bang):
    if(bang == pow(2,point_su)-1): 
        return 0,[]
    if(jegi[bang][st][0] != 0):
        return jegi[bang][st][0],jegi[bang][st][1]
    r = 100000000000000000000
    for i in range(point_su):
        if(bang & (1 << i) == 0 and way[st][i] != 0):
            s,s2 = soon(i,bang | (1 << i))
            if(s+way[st][i] < r):
                s1 = s2
                r = s+way[st][i]
                s3 = way[st][i]
                #print(i,bin(bang | (1 << i)),soon(i,bang | (1 << i))+way[st][i])
    jegi[bang][st] = [r, s1+[s3]]
    return r , s1+[s3]



m_h,m_w = map(int,sys.stdin.readline().split())

m = [[0 for i in range(m_w)] for i in range(m_h)]
ang = [[-1,0],[0,1],[1,0],[0,-1]]

for i in range(m_h):
    inp = sys.stdin.readline()
    for j in range(m_w):
        if(inp[j] == 'S'):
            m[i][j] = 1
        elif(inp[j] == 'X'):
            m[i][j] = 2

bang = [[True for i in range(m_w)] for i in range(m_h)]
count = 2
isl = []
for i in range(m_h):
    for j in range(m_w):
        if(bang[i][j] and m[i][j] == 2):
            isl.append([[i,j,0]])
            bang[i][j] = False
            m[i][j] = count
            q = deque([[i,j]])
            while q:
                qpop =  q.popleft()
                for k in range(4):
                    dum1 = qpop[0]+ang[k][0]
                    dum2 = qpop[1]+ang[k][1]
                    if(dum1 >= 0 and dum1 < m_h and dum2 >= 0 and dum2 < m_w):
                        if(bang[dum1][dum2] and m[dum1][dum2] == 2):
                            bang[dum1][dum2] = False
                            m[dum1][dum2] = count
                            q.append([dum1,dum2])
                            isl[count-2].append([dum1,dum2,0])
            count += 1
way = [[0 for i in range(count-2)] for j in range(count-2)]
for i in range(count-3):
    q = deque(isl[i])
    bang = [[100000000000000000000 for i in range(m_w)] for i in range(m_h)]
    t = 0
    while q:
        t+= 1
        for j in range(len(q)):
            qpop =  q.popleft()
            for k in range(4):
                dum1 = qpop[0]+ang[k][0]
                dum2 = qpop[1]+ang[k][1]
                if(dum1 >= 0 and dum1 < m_h and dum2 >= 0 and dum2 < m_w):
                    if(bang[dum1][dum2] > t-qpop[2] and m[dum1][dum2] != i+2 and m[dum1][dum2] != 0):
                        bang[dum1][dum2] = t-qpop[2]
                        q.append([dum1,dum2,qpop[2]+1*(m[dum1][dum2] != 1)])
                        if(m[dum1][dum2] != 1):
                            if(way[i][m[dum1][dum2]-2] == 0 or way[i][m[dum1][dum2]-2] > t-qpop[2]-1):
                                way[i][m[dum1][dum2]-2] = t-qpop[2]-1
                                way[m[dum1][dum2]-2][i] = t-qpop[2]-1
#print(way)
bang = 0
m = 0
isl = 0
point_su = count-2
jegi = [[[0,0] for i in range(point_su)] for j in range(0b111111111111111)]

mina= 10000000000000
for i in range(point_su):
    a,b = soon(i,(1<<i))
    mina = min(mina,a)
print(mina)