import sys
a = int(input())
m = []
m1 = [[0 for j in range(a)] for i in range(a)]
for i in range(a):
    m.append(sys.stdin.readline().strip())
ang = [[-1,0],[0,1],[0,-1],[1,0]]
nsm = 0
for i in range(a):
    for j in range(a):
        if(m1[i][j] == 0):
            gam = [[i,j]]
            rgb = m[i][j]
            nsm +=1
            while len(gam) != 0:
                le = len(gam)
                for k in range(le):
                    m1[gam[0][0]][gam[0][1]] = 1
                    for l in range(4):
                        if(gam[0][0]+ang[l][0] > -1 and gam[0][0]+ang[l][0] < a and gam[0][1]+ang[l][1] > -1 and gam[0][1]+ang[l][1] < a):
                            if(m[gam[0][0]+ang[l][0]][gam[0][1]+ang[l][1]] == rgb and m1[gam[0][0]+ang[l][0]][gam[0][1]+ang[l][1]] == 0):
                                gam.append([gam[0][0]+ang[l][0],gam[0][1]+ang[l][1]])
                                m1[gam[0][0]+ang[l][0]][gam[0][1]+ang[l][1]] = 1
                    del gam[0]
sm = 0
m1 = [[0 for j in range(a)] for i in range(a)]
for i in range(a):
    for j in range(a):
        if(m1[i][j] == 0):
            gam = [[i,j]]
            rgb = (m[i][j] == 'B')
            sm +=1
            while len(gam) != 0:
                le = len(gam)
                for k in range(le):
                    m1[gam[0][0]][gam[0][1]] = 1
                    for l in range(4):
                        if(gam[0][0]+ang[l][0] > -1 and gam[0][0]+ang[l][0] < a and gam[0][1]+ang[l][1] > -1 and gam[0][1]+ang[l][1] < a):
                            if((m[gam[0][0]+ang[l][0]][gam[0][1]+ang[l][1]]=='B') == rgb and m1[gam[0][0]+ang[l][0]][gam[0][1]+ang[l][1]] == 0):
                                gam.append([gam[0][0]+ang[l][0],gam[0][1]+ang[l][1]])
                                m1[gam[0][0]+ang[l][0]][gam[0][1]+ang[l][1]] = 1
                    del gam[0]
print(nsm,sm)                             