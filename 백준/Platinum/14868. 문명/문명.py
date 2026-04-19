"문명"

import sys
from collections import deque

def union(x,y):
    global max_c
    x = find(x)
    y = find(y)
    
    if(x < y):
        bumo[y] =  x
        bumo_c[x] += bumo_c[y]
        max_c = max(max_c,bumo_c[x])
        bumo_c[y] += 0
    elif(x != y):
        bumo[x] =  y
        bumo_c[y] += bumo_c[x]
        max_c = max(max_c,bumo_c[y])
        bumo_c[x] = 0


def find(a):
    b = a
    while 1:
        if(a == bumo[a]):
            break
        a = bumo[a]
    r = a
    a = b
    while 1:
        if(a == bumo[a]):
            break
        bumo[a] = r
        a = bumo[a]
    return r

m_s,poi_su = map(int,sys.stdin.readline().split())
bumo = [i for i in range(poi_su)]
bumo_c = [1 for i in range(poi_su)]
m = [[-1 for i in range(m_s)] for i in range(m_s)]
ang = [[0,1],[1,0],[0,-1],[-1,0]]
q = deque([])
max_c = 0

for i in range(poi_su):
    inp1,inp2 = map(int,sys.stdin.readline().split())
    inp1 -= 1
    inp2 -= 1
    q.append([inp1,inp2])
    m[inp1][inp2] = i
    
    for j in range(4):
        dum1 = inp1+ang[j][0]
        dum2 = inp2+ang[j][1]
        if(dum1 < m_s and dum1 > -1 and dum2 < m_s and dum2 > -1):
            if(m[dum1][dum2] != -1):
                union(i,m[dum1][dum2])

t = 0
while (max_c != poi_su):
    t+=1
    for i in range(len(q)):
        qpop = q.popleft()
        dum = m[qpop[0]][qpop[1]]
        for j in range(4):
            dum1 = qpop[0]+ang[j][0]
            dum2 = qpop[1]+ang[j][1]
            if(dum1 < m_s and dum1 > -1 and dum2 < m_s and dum2 > -1):
                if(m[dum1][dum2] == -1):
                    m[dum1][dum2] = dum
                    q.append([dum1,dum2])
                    for k in range(4):
                        if(k != (j+2)%4 or k != (j+3)%4):
                            dum4 = dum1+ang[k][0]
                            dum5 = dum2+ang[k][1]
                            if(dum4 < m_s and dum4 > -1 and dum5 < m_s and dum5 > -1):
                                if(m[dum4][dum5] != -1):
                                    union(dum,m[dum4][dum5])
                else:
                    union(dum,m[dum1][dum2])
                
print(t)