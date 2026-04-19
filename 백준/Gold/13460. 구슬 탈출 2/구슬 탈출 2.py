import sys
from collections import deque

a,b = map(int,input().split())
m = []

mab = [[0,0],[0,0]]

for i in range(a):
    m.append([j for j in sys.stdin.readline().strip()])
    for j in range(b):
        if(m[i][j] == 'B'):
            mab[1] = [i,j]
            m[i][j] = '.'
        if(m[i][j] == 'R'):
            mab[0] = [i,j]
            m[i][j] = '.'

ang = [[0,-1],[1,0],[0,1],[-1,0]]
m2 = [[[-1,-1,-1,-1] for i in range(b)] for j in range(a)]
m3 = [[0 for i in range(b)] for j in range(a)]
m4 = [[[[0 for i in range(b)] for j in range(a)] for k in range(b)] for l in range(a)]

li = deque([[i[:] for i in mab]])

tt =0

for t in range(10):
    lenli = len(li)
    if(lenli == 0):
        break
    for i in range(lenli):
        popo = li.popleft()
        
        for j in range(4):
            if(j == 0): fir = (popo[0][1] > popo[1][1]) * 1
            if(j == 1): fir = (popo[0][0] < popo[1][0]) * 1
            if(j == 2): fir = (popo[0][1] < popo[1][1]) * 1
            if(j == 3): fir = (popo[0][0] > popo[1][0]) * 1
            
            popo2 = [i[:] for i in popo]
            br = 0
            
            for k in range(2):
                if(m2[popo2[(fir+k)%2][0]][popo2[(fir+k)%2][1]][j] == -1):
                    bloc = 0
                    while 1:
                        popo2[(fir+k)%2][0] += ang[j][0]
                        popo2[(fir+k)%2][1] += ang[j][1]
                        bloc += 1
                        if(m[popo2[(fir+k)%2][0]][popo2[(fir+k)%2][1]] == 'O'):
                            br = max(br,(fir+k)%2+1)
                            break
                        if(m[popo2[(fir+k)%2][0]][popo2[(fir+k)%2][1]] == '#'):
                            
                            m2[popo[(fir+k)%2][0]][popo[(fir+k)%2][1]][j] = bloc-1
                            popo2[(fir+k)%2][0] -= ang[j][0]
                            popo2[(fir+k)%2][1] -= ang[j][1]
                            break
                        
                else:
                    popo2[(fir+k)%2][0] += ang[j][0]*m2[popo2[(fir+k)%2][0]][popo2[(fir+k)%2][1]][j]
                    popo2[(fir+k)%2][1] += ang[j][1]*m2[popo2[(fir+k)%2][0]][popo2[(fir+k)%2][1]][j]
                
                
                if(popo2[0] == popo2[1]):
                    popo2[(fir+k)%2][0] -= ang[j][0]
                    popo2[(fir+k)%2][1] -= ang[j][1]
                    
            if(br == 1):
                break
            if(br == 0 and m4[popo2[0][0]][popo2[0][1]][popo2[1][0]][popo2[1][1]] == 0):
                m4[popo2[0][0]][popo2[0][1]][popo2[1][0]][popo2[1][1]] = 1
                li.append(popo2)
        if(br == 1):break
    #print(li)
    if(br == 1):
        tt = t
        break
if(br == 1):
    print(tt+1)
else:
    print(-1)