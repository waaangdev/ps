import sys
a,b = map(int,input().split())
m = []
bir = []#바이러스
ang = [[0,-1],[0,1],[1,0],[-1,0]]
wall = [0,0,0]#벽
m_ax = a*b
brbr =0 
anjunmax = 0
anjun = 0
for i in range(a):
    m.append(list(map(int,sys.stdin.readline().strip().split())))
    for j in range(b):
        if(m[i][j] == 2):
            bir.append([i,j])
        if(m[i][j] == 0):
            anjun += 1
while 1:
    m2 = [i[:] for i in m]
    qwe = 0
    for i in range(3):
        if(m2[wall[i]//b][wall[i]%b] > 0):
            qwe = 1
            break
        else:
            m2[wall[i]//b][wall[i]%b] = 1
    if(qwe == 0):
        #바이러스 퍼짐 시뮬 코드
        bir2 = [list(i) for i in bir]
        anjun1 = anjun
        while 1:
            bir2_len = len(bir2)
            if(bir2_len == 0):
                break
            for i in range(bir2_len):
                for j in range(4):
                    if(bir2[0][0]+ang[j][0] >= 0 and bir2[0][0]+ang[j][0] < a and bir2[0][1]+ang[j][1] >= 0 and bir2[0][1]+ang[j][1] < b):
                        if(m2[bir2[0][0]+ang[j][0]][bir2[0][1]+ang[j][1]] == 0):
                            bir2.append([bir2[0][0]+ang[j][0],bir2[0][1]+ang[j][1]])
                            m2[bir2[0][0]+ang[j][0]][bir2[0][1]+ang[j][1]] = 2
                            anjun1 -= 1
                del bir2[0]
        anjunmax = max(anjunmax,anjun1)
    
    wall[0] += 1
    for i in range(3):
        if(wall[i] == m_ax):
            if(i == 2):
                brbr = 1
                break
            else:
                wall[i+1] += 1
                wall[i] = 0
    if(brbr == 1):
        break
print(anjunmax-3)