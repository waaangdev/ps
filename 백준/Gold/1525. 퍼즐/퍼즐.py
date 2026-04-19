"퍼즐"

import sys
from collections import deque

ang = [[0,1],[-1,0],[1,0],[0,-1]]
li = []
for i in range(3):
    li = li+ list(map(int,sys.stdin.readline().split()))
    for j in range(3):
        if(li[i*3+j] == 0):
            mx = i
            my = j
q = deque([[mx,my,li]])
bang = set([])
qwe = 0
for i in range(9):
    qwe+=li[i]*(10**i)
bang.add(qwe)
goal = [1,2,3,4,5,6,7,8,0]

r = -1
t = 0
if(li == goal):
    r = 0
else:
    while q:
        t += 1
        lenq = len(q)
        for _ in range(lenq):
            qpop = q.popleft()
            for i in range(4):
                if(qpop[0]+ang[i][0] > -1 and qpop[0]+ang[i][0] < 3 and qpop[1]+ang[i][1] > -1 and qpop[1]+ang[i][1] < 3):
                    qpop_li_dum = qpop[2][:]
                    qpop_li_dum[qpop[0]*3+qpop[1]] = qpop_li_dum[(qpop[0]+ang[i][0])*3+qpop[1]+ang[i][1]]
                    qpop_li_dum[(qpop[0]+ang[i][0])*3+qpop[1]+ang[i][1]] = 0
                    
                    qwe = 0
                    for j in range(9):
                        qwe+=qpop_li_dum[j]*(10**j)
                        
                    if(qwe not in bang):
                        bang.add(qwe)
                        q.append([qpop[0]+ang[i][0],qpop[1]+ang[i][1],qpop_li_dum])
                        if(qpop[0]+ang[i][0] == 2 and qpop[1]+ang[i][1] == 2):
                            if(qpop_li_dum == goal):
                                r = t
                                break
            if(r != -1):break
        if(r != -1):break
        #print(q,bang)
print(r)