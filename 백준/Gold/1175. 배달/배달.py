import sys
from collections import deque

a,b = map(int,input().split())
m = []
pl = []
ang = [[0,1],[-1,0],[1,0],[0,-1]]
for i in range(a):
    m.append([i for i in sys.stdin.readline().strip()])
    for j in range(b):
        if m[i][j] == 'S':
            pl = [i,j]

t = 0



li = deque([[pl[0],pl[1],10,10]])
br = 0
m2 = [[[0,0,0,0] for j in range(b)] for i in range(a)]

m3 = [[[[0,0,0,0,0] for j in range(b)] for i in range(a)]+[0] for _ in range(8)]
while 1:
    t+=1
    
    if(len(li) == 0):
        break
    for i in range(len(li)):
        popo = li.popleft()
        for j in range(4):
            if(j != popo[2]):
                if(popo[0] + ang[j][0] >= 0 and popo[0] + ang[j][0] < a and popo[1] + ang[j][1] >= 0 and popo[1] + ang[j][1] < b):
                    if(popo[3] == 10):
                        if(m[popo[0]+ ang[j][0]][popo[1]+ ang[j][1]] != '#'):
                            if(m2[popo[0]+ ang[j][0]][popo[1]+ ang[j][1]][j] == 0):
                                m2[popo[0]+ ang[j][0]][popo[1]+ ang[j][1]][j] = 1
                                if(m[popo[0]+ ang[j][0]][popo[1]+ ang[j][1]] == 'C'):
                                    if(m3[j][a] == 0):
                                        m3[j][popo[0]+ ang[j][0]][popo[1]+ ang[j][1]][4] = 1
                                        m3[j][a] = 1
                                        li.append([popo[0]+ ang[j][0],popo[1]+ ang[j][1],j,j])
                                    else:
                                        m3[j+4][popo[0]+ ang[j][0]][popo[1]+ ang[j][1]][4] = 1
                                        m3[j+4][a] = 1
                                        li.append([popo[0]+ ang[j][0],popo[1]+ ang[j][1],j,j+4])
                                else:
                                    li.append([popo[0]+ ang[j][0],popo[1]+ ang[j][1],j,10])
                    else:
                        if(m[popo[0]+ ang[j][0]][popo[1]+ ang[j][1]] != '#'):
                            if(m3[popo[3]][popo[0]+ ang[j][0]][popo[1]+ ang[j][1]][j] == 0):
                                m3[popo[3]][popo[0]+ ang[j][0]][popo[1]+ ang[j][1]][j] = 1
                                if(m[popo[0]+ ang[j][0]][popo[1]+ ang[j][1]] == 'C' and m3[popo[3]][popo[0]+ ang[j][0]][popo[1]+ ang[j][1]][4] == 0):
                                    br = 1
                                else:
                                    li.append([popo[0]+ ang[j][0],popo[1]+ ang[j][1],j,popo[3]])
    if(br != 0):break
if(br != 0):
    print(t)
else:
    print(-1)
            

