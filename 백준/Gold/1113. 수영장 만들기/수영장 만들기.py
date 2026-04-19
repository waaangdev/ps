import sys
from collections import deque

a,b = map(int,input().split())
m = []
ang = [[0,1],[-1,0],[1,0],[0,-1]]

for i in range(a):
    m.append([int(i) for i in sys.stdin.readline().strip()])
m2 = [[1 for i in range(b)] for i in range(a)]
r = 0
for i in range(2,10):
    m3 = [[0 for i in range(b)] for i in range(a)]
    m4 = [[0 for i in range(b)] for i in range(a)]
    for j in range(a):
        for k in range(b):
            if(m3[j][k] == 0 and m[j][k] < i):
                m4 = [[0 for i in range(b)] for i in range(a)]
                li = deque([[j,k]])
                m4[j][k] = 1
                br = 0
                r1 = 1
                while 1:
                    if(len(li) == 0):
                        break
                    for l in range(len(li)):
                        popo = li.popleft()
                        
                        for o in range(4):
                            if(popo[0] + ang[o][0] >= 0 and popo[0] + ang[o][0] < a and popo[1] + ang[o][1] >= 0 and popo[1] + ang[o][1] < b):
                                if(m[popo[0]+ ang[o][0]][popo[1]+ ang[o][1]] < i):
                                    if(m4[popo[0]+ ang[o][0]][popo[1]+ ang[o][1]] == 0):
                                        li.append([popo[0]+ ang[o][0],popo[1]+ ang[o][1]])
                                        m4[popo[0]+ ang[o][0]][popo[1]+ ang[o][1]] = 1
                                        r1 += 1
                                        if(m2[popo[0]+ ang[o][0]][popo[1]+ ang[o][1]] < 0):
                                            br = 1
                            else:
                                br = 1
                if(br == 0):
                    r += r1
                    for l in range(a):
                        for o in range(b):
                            m3[l][o] += m4[l][o]
                else:
                    for l in range(a):
                        for o in range(b):
                            m3[l][o] -= m4[l][o]
    tmp = [i[:] for i in m3]
    m3 = [i[:] for i in m4]
    m2 = tmp
print(r)