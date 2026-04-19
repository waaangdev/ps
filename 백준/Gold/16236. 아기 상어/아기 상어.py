import sys
from collections import deque

d = int(input())

m = []
pl = [0,0]
ang = [[0,1],[-1,0],[1,0],[0,-1]]

for i in range(d):
    m.append(list(map(int,sys.stdin.readline().split())))
    for j in range(d):
        if(m[i][j] == 9):
            m[i][j] = 0
            pl = [i,j]
t = 0
pl_c = 2#크기
plexp = 0
while 1:

    li = deque([pl[:]])
    m2 = [[0 for j in range(d)] for i in range(d)]
    br = 0
    brl = [d,d]
    
    t2 = 0
    while 1:
        t2+=1
        if(len(li) == 0):
            break
        for i in range(len(li)):
            popo = li.popleft()
            
            for j in range(4):
                if(popo[0] + ang[j][0] >= 0 and popo[0] + ang[j][0] < d and popo[1] + ang[j][1] >= 0 and popo[1] + ang[j][1] < d):
                    if(m2[popo[0]+ ang[j][0]][popo[1]+ ang[j][1]] == 0):
                        if(m[popo[0]+ ang[j][0]][popo[1]+ ang[j][1]] <= pl_c):
                            li.append([popo[0]+ ang[j][0],popo[1]+ ang[j][1]])
                            m2[popo[0]+ ang[j][0]][popo[1]+ ang[j][1]] = 1
                            if(m[popo[0]+ ang[j][0]][popo[1]+ ang[j][1]] < pl_c and m[popo[0]+ ang[j][0]][popo[1]+ ang[j][1]] != 0):

                                if((popo[0]+ ang[j][0])*d+(popo[1]+ ang[j][1]) < brl[0]*d+brl[1]):
                                    brl = [popo[0]+ ang[j][0],popo[1]+ ang[j][1]]
                                    br = 1
        if(br == 1):break
    
    if(brl == [d,d]):
        break#엄상어 호출

    m[brl[0]][brl[1]] = 0
    plexp +=1
    if plexp == pl_c:
        plexp = 0
        pl_c +=1

   
    t += t2
    pl = brl[:]
print(t)