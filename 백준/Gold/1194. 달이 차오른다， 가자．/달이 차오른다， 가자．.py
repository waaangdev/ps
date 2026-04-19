import sys
from collections import deque

ang = [[0,1],[-1,0],[0,-1],[1,0]]

m = []
a,b = map(int,input().split())

for i in range(a):
    m.append(list(sys.stdin.readline().strip()))
    for j in range(b):
        if(m[i][j] == '0'):
            li = deque([[i,j,0b000000]])
    
m2 = [[[[[[[0b00000000000000000000000000000000000000000000000000 for j in range(a)] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)]

r = 0
br = 0

while 1:
    r+=1
    lenli = len(li)
    if(lenli == 0):
        r = -1
        break
    for i in range(lenli):
        popo = li.popleft()
        for j in range(4):
            if(popo[0]+ang[j][0] < a and popo[0]+ang[j][0] > -1 and popo[1]+ang[j][1] < b and popo[1]+ang[j][1] > -1):
                
                popo2 = [0,0]
                popo2[0] = (popo[0]+ang[j][0])
                popo2[1] = (popo[1]+ang[j][1])
                
                if(m[popo2[0]][popo2[1]] != '#'):
                    qwe = 0
                    if((ord(m[popo2[0]][popo2[1]]) < 65 or ord(m[popo2[0]][popo2[1]]) > 70)):
                        qwe = 1
                    elif(popo[2] & (1<<(ord(m[popo2[0]][popo2[1]]) - 65+1))):
                        qwe = 1
                    if(qwe == 1):
                        if(m2[(popo[2] & (1 << 1) != 0)*1][(popo[2] & (1 << 2) != 0)*1][(popo[2] & (1 << 3) != 0)*1][(popo[2] & (1 << 4) != 0)*1][(popo[2] & (1 << 5) != 0)*1][(popo[2] & (1 << 6) != 0)*1][popo2[0]] & (1 << (popo2[1]+1)) == 0):
                            m2[(popo[2] & (1 << 1) != 0)*1][(popo[2] & (1 << 2) != 0)*1][(popo[2] & (1 << 3) != 0)*1][(popo[2] & (1 << 4) != 0)*1][(popo[2] & (1 << 5) != 0)*1][(popo[2] & (1 << 6) != 0)*1][popo2[0]] |= (1<<(popo2[1]+1))
                            next_  = 0
                            if((ord(m[popo2[0]][popo2[1]]) >= 97 and ord(m[popo2[0]][popo2[1]]) <= 102)):
                                next_ = 1 << (ord(m[popo2[0]][popo2[1]]) - 97+1)
                            li.append([popo2[0],popo2[1],popo[2] | next_])
                            if(m[popo2[0]][popo2[1]] == '1'):
                                br = 1
                                break
        if(br == 1):break
    if(br == 1):break
print(r)