from collections import deque
import sys
a = list(map(int,input().split()))
ang =[[1,0],[0,1]]
bing = []
for i in range(a[0]):
    c =input().split()
    for j in range(a[1]):
        if(c[j] != "0"):
            bing.append([i,j,int(c[j])])
time = 0
le = len(bing)
over = 0
while over == 0:
    time +=1
    m = [[0 for i in range(a[1])] for i in range(a[0])]
    for i in range(len(bing)):
        if(bing[i][2] != 0):
          m[bing[i][0]][bing[i][1]] = 1
    for i in range(len(bing)):
        if(bing[i][2] != 0):
            for j in range(2):
                for k in range(-1,2,2):
                    if(m[bing[i][0]+ang[j][0]*k][bing[i][1]+ang[j][1]*k] == 0):
                        bing[i][2] -=1
            if(bing[i][2] <= 0):
                bing[i][2] =0  
                le -= 1
    m = [[0 for i in range(a[1])] for i in range(a[0])]
    for i in range(len(bing)):
        if(bing[i][2] != 0):
            m[bing[i][0]][bing[i][1]] = 1
    if(le == 0):
        print(0)
        break
    for i in range(len(bing)):
        if(bing[i][2] != 0):
            gam = deque([[bing[i][0],bing[i][1]]])
            m[gam[0][0]][gam[0][1]] = 0
            gam2 = 1
            while 1:
                lele = len(gam)
                for j in range(lele):
                    for k in range(2):
                        for l in range(-1,2,2):
                            if(m[gam[0][0]+ang[k][0]*l][gam[0][1]+ang[k][1]*l] == 1):
                                gam.append([gam[0][0]+ang[k][0]*l,gam[0][1]+ang[k][1]*l])
                                m[gam[0][0]+ang[k][0]*l][gam[0][1]+ang[k][1]*l] = 0
                                gam2 +=1
                    gam.popleft()
                if(len(gam) == 0):
                    break
            if(gam2 != le):
                print(time)
                over = 1
                
            break