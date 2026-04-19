import sys
from collections import deque
a,b = map(int,input().split())
m = []
for _ in range(a):
    m.append([int(i) for i in sys.stdin.readline().strip()])

ang = [[0,1],[1,0],[-1,0],[0,-1]]

m32 = [0 for j in range(a*b+2)] #5

for i in range(a):
    for j in range(b):
        if(m[i][j] == 0):
            kgi = 1
            li = deque([[i,j]])
            m[i][j] = i*b+j+2
            while 1:
                lenli = len(li)
                if(lenli == 0):
                    break
                for k in range(lenli):
                    popl = li.popleft()
                    for l in range(4):
                        if(popl[0]+ang[l][0] >= 0 and popl[0]+ang[l][0] < a and popl[1]+ang[l][1] >= 0 and popl[1]+ang[l][1] < b):
                            if(m[popl[0]+ang[l][0]][popl[1]+ang[l][1]] == 0):
                                li.append([popl[0]+ang[l][0],popl[1]+ang[l][1]])
                                m[popl[0]+ang[l][0]][popl[1]+ang[l][1]] = i*b+j+2
                                kgi +=1
            m32[i*b+j+2] = kgi          #2*1+0+2
for i in range(a):
    for j in range(b):
        kgi = -1
        if(m[i][j] == 1):
            m4 = []
            kgi = 0
            for l in range(4):
                if(i+ang[l][0] >= 0 and i+ang[l][0] < a and j+ang[l][1] >= 0 and j+ang[l][1] < b):
                    if(not m[i+ang[l][0]][j+ang[l][1]] in m4):
                        m4.append(m[i+ang[l][0]][j+ang[l][1]])
                        kgi+=m32[m[i+ang[l][0]][j+ang[l][1]]]
        print((kgi+1)%10,end = '')
    print()