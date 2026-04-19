import sys
from collections import deque
a,b,z = list(map(int, sys.stdin.readline().split()))
m= []
fo = [[-1,0,0],[1,0,0],[0,-1,0],[0,1,0],[0,0,1],[0,0,-1]]
for j in range(z):
    m.append([])
    for i in range(b):
        m[j].append(list(map(int,sys.stdin.readline().split())))
li = deque([])
tim = 0
zro = 0
zro1 = 0
for k in range(z):
    for i in range(b):
        for j in range(a):
            if(m[k][i][j] == 1):
                li.append([i,j,k])
                zro1 += 1
            if(m[k][i][j] == 0):
                zro += 1
if(zro == 0):
    print(0)
elif(zro1 == 0):
    print(-1)
else:
    while 1:
        tim+=1
        le = len(li)
        for i in range(le):
            for k in range(6):
                if(li[0][0]+fo[k][0] < b and li[0][0]+fo[k][0] >= 0 and li[0][1]+fo[k][1] < a and li[0][1]+fo[k][1] >= 0 and li[0][2]+fo[k][2] < z and li[0][2]+fo[k][2] >= 0):
                    if(m[li[0][2]+fo[k][2]][li[0][0]+fo[k][0]][li[0][1]+fo[k][1]] == 0):
                        m[li[0][2]+fo[k][2]][li[0][0]+fo[k][0]][li[0][1]+fo[k][1]] = 1
                        li.append([li[0][0]+fo[k][0] ,li[0][1]+fo[k][1],li[0][2]+fo[k][2]])
            li.popleft()
        if(len(li) == 0):
            zro = 0
            for k in range(z):
                for i in range(b):
                    for j in range(a):
                        if(m[k][i][j] == 0):
                            zro = 1
                            break
                    if(zro == 1):
                        break
            if(zro == 0):
                print(tim-1)
                break
            else:
                print(-1)
                break