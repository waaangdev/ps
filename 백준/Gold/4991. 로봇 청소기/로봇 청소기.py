import sys
from collections import deque

ang = [[0,1],[-1,0],[0,-1],[1,0]]
while 1:
    b,a = map(int,input().split())
    if(a == 0 and b==0):
        break
    m1 = [[-1 for i in range(10)] for j in range(11)]
    m = []
    li5 = []
    count = 0
    for i in range(a):
        m.append(list(sys.stdin.readline().strip()))
        for j in range(b):
            if(m[i][j] == 'o'):
                li5.insert(0,[i,j])

            if(m[i][j] == '*'):
                m[i][j] = str(count)
                count += 1
                li5.append([i,j])
    for k in range(a):
        for l in range(b):
            if(m[k][l] == 'o'):
                li = deque([[0,0,0b10000000000]])
                min_ = -1
                max_ = 0
                bang = 0b100000000000
                for _ in range(count):
                    lenli = len(li)
                    if(lenli == 0):
                        r = -1
                        break
                    for i in range(lenli):
                        popo = li.popleft()
                        if(bang & (1 << (popo[0])) == 0):
                            bang |= (1 << (popo[0])) 
                            t = 0
                            li2 = deque([li5[popo[0]]])
                            m22 = [0b1000000000000000000000 for _ in range(a)]
                            m22[li5[popo[0]][0]] |= (1<<((li5[popo[0]][1])))
                            while 1:
                                t+=1
                                lenli2 = len(li2)
                                if(lenli2 == 0):
                                    r = -1
                                    break
                                for i1 in range(lenli2):
                                    popo2 = li2.popleft()
                                    for j1 in range(4):
                                        if(popo2[0]+ang[j1][0] < a and popo2[0]+ang[j1][0] > -1 and popo2[1]+ang[j1][1] < b and popo2[1]+ang[j1][1] > -1):
                                            if(m[popo2[0]+ang[j1][0]][popo2[1]+ang[j1][1]] != 'x'):
                                                if(m22[popo2[0]+ang[j1][0]] & (1 << ((popo2[1]+ang[j1][1]))) == 0):
                                                    m22[popo2[0]+ang[j1][0]] |= (1<<((popo2[1]+ang[j1][1])))
                                                    li2.append([popo2[0]+ang[j1][0],popo2[1]+ang[j1][1]])
                                                    if((ord(m[popo2[0]+ang[j1][0]][popo2[1]+ang[j1][1]]) >= 48 and ord(m[popo2[0]+ang[j1][0]][popo2[1]+ang[j1][1]]) <= 57)):
                                                        m1[popo[0]][int(m[popo2[0]+ang[j1][0]][popo2[1]+ang[j1][1]])] = t
                        for j in range(10):
                            if(m1[popo[0]][j] != -1):
                                #if(m2[(popo[2] & (1 << 0) != 0)*1][(popo[2] & (1 << 1) != 0)*1][(popo[2] & (1 << 2) != 0)*1][(popo[2] & (1 << 3) != 0)*1][(popo[2] & (1 << 4) != 0)*1][(popo[2] & (1 << 5) != 0)*1][(popo[2] & (1 << 6) != 0)*1][(popo[2] & (1 << 7) != 0)*1][(popo[2] & (1 << 8) != 0)*1][(popo[2] & (1 << 9) != 0)*1][popo[0]] & (1 << (j)) == 0):
                                if(popo[2] & (1 << j) == 0):
                                    #m2[(popo[2] & (1 << 0) != 0)*1][(popo[2] & (1 << 1) != 0)*1][(popo[2] & (1 << 2) != 0)*1][(popo[2] & (1 << 3) != 0)*1][(popo[2] & (1 << 4) != 0)*1][(popo[2] & (1 << 5) != 0)*1][(popo[2] & (1 << 6) != 0)*1][(popo[2] & (1 << 7) != 0)*1][(popo[2] & (1 << 8) != 0)*1][(popo[2] & (1 << 9) != 0)*1][popo[0]] |= (1<<(j))
                                    next_ = 1 << (j)
                                    li.append([j+1,popo[1] + m1[popo[0]][j],popo[2] | next_])
                                    if(max_ <= popo[2] | next_): 
                                        if(max_ < popo[2] | next_):
                                            min_ = -1
                                        max_ = popo[2] | next_
                                        min_ = min(min_,popo[1] + m1[popo[0]][j])
                                        if(min_ == -1): min_ = popo[1] + m1[popo[0]][j]

    if(len(li) == 0):
        print(-1)
    else:
        print(min_)