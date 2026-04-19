import sys
from collections import deque
a = list(map(int, sys.stdin.readline().split()))
m= []
fo = [
    [1,0,0,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,0,0,1]
]
for i in range(a[10]):
    m.append([])
    for i1 in range(a[9]):
        m[i].append([])
        for i2 in range(a[8]):
            m[i][i1].append([])
            for i3 in range(a[7]):
                m[i][i1][i2].append([])
                for i4 in range(a[6]):
                    m[i][i1][i2][i3].append([])
                    for i5 in range(a[5]):
                        m[i][i1][i2][i3][i4].append([])
                        for i6 in range(a[4]):
                            m[i][i1][i2][i3][i4][i5].append([])
                            for i7 in range(a[3]):
                                m[i][i1][i2][i3][i4][i5][i6].append([])
                                for i8 in range(a[2]):
                                    m[i][i1][i2][i3][i4][i5][i6][i7].append([])
                                    for i9 in range(a[1]):
                                        m[i][i1][i2][i3][i4][i5][i6][i7][i8].append(list(map(int,sys.stdin.readline().split())))
li = deque([])
tim = 0
zro = 0
zro1 = 0
for i in range(a[10]):
    for i1 in range(a[9]):
        for i2 in range(a[8]):
            for i3 in range(a[7]):
                for i4 in range(a[6]):
                    for i5 in range(a[5]):
                        for i6 in range(a[4]):
                            for i7 in range(a[3]):
                                for i8 in range(a[2]):
                                    for i9 in range(a[1]):
                                        for i0 in range(a[0]):
                                            if(m[i][i1][i2][i3][i4][i5][i6][i7][i8][i9][i0] == 1):
                                                li.append([i0,i9,i8,i7,i6,i5,i4,i3,i2,i1,i])
                                                zro1 += 1
                                            else:
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
            for k in range(11):
                for l in range(-1,2,2):
                    if(li[0][k]+fo[k][k]*l < a[k] and li[0][k]+fo[k][k]*l >= 0):
                        if(m[li[0][10]+fo[k][10]*l][li[0][9]+fo[k][9]*l][li[0][8]+fo[k][8]*l][li[0][7]+fo[k][7]*l][li[0][6]+fo[k][6]*l][li[0][5]+fo[k][5]*l][li[0][4]+fo[k][4]*l][li[0][3]+fo[k][3]*l][li[0][2]+fo[k][2]*l][li[0][1]+fo[k][1]*l][li[0][0]+fo[k][0]*l] == 0):
                            m[li[0][10]+fo[k][10]*l][li[0][9]+fo[k][9]*l][li[0][8]+fo[k][8]*l][li[0][7]+fo[k][7]*l][li[0][6]+fo[k][6]*l][li[0][5]+fo[k][5]*l][li[0][4]+fo[k][4]*l][li[0][3]+fo[k][3]*l][li[0][2]+fo[k][2]*l][li[0][1]+fo[k][1]*l][li[0][0]+fo[k][0]*l] = 1
                            li.append([li[0][0]+fo[k][0]*l,li[0][1]+fo[k][1]*l,li[0][2]+fo[k][2]*l,li[0][3]+fo[k][3]*l,li[0][4]+fo[k][4]*l,li[0][5]+fo[k][5]*l,li[0][6]+fo[k][6]*l,li[0][7]+fo[k][7]*l,li[0][8]+fo[k][8]*l,li[0][9]+fo[k][9]*l,li[0][10]+fo[k][10]*l])
            li.popleft()
        if(len(li) == 0):
            zro = 0
            for i in range(a[10]):
                for i1 in range(a[9]):
                    for i2 in range(a[8]):
                        for i3 in range(a[7]):
                            for i4 in range(a[6]):
                                for i5 in range(a[5]):
                                    for i6 in range(a[4]):
                                        for i7 in range(a[3]):
                                            for i8 in range(a[2]):
                                                for i9 in range(a[1]):
                                                    for i0 in range(a[0]):
                                                        if(m[i][i1][i2][i3][i4][i5][i6][i7][i8][i9][i0] == 0):
                                                            zro = 1
                                                            break
                                                if(zro == 1):
                                                    break
                                            if(zro == 1):
                                                break
                    if(zro == 1):
                        break
                if(zro == 1):
                    break
                   
            if(zro == 0):
                print(tim-1)
                break
            else:
                print(-1)
                break