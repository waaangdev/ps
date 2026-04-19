"달리기"

import sys
from collections import deque

m_h,m_w,move = map(int,sys.stdin.readline().split())
m = []
for i in range(m_h):
    m.append(sys.stdin.readline())
st1,st2,end1,end2 = map(int,sys.stdin.readline().split())

st = [st1-1,st2-1]
end = [end1-1,end2-1]
bang = [[1000*1000 for i in range(m_w)] for i in range(m_h)]
q = deque([st])
br = 0
ang = [[1,0],[0,-1],[-1,0],[0,1]]
t= 0

while q:
    t+=1
    #print(q)
    for _ in range(len(q)):
        qpop = q.popleft()
        for i in range(4):
            for j in range(1,move+1):
                #print(j)
                if(qpop[0]+ang[i][0]*j < 0 or qpop[1]+ang[i][1]*j < 0 or qpop[0]+ang[i][0]*j >= m_h or qpop[1]+ang[i][1]*j >= m_w):break
                if(m[qpop[0]+ang[i][0]*j][qpop[1]+ang[i][1]*j] == '#'):break
                if(bang[qpop[0]+ang[i][0]*j][qpop[1]+ang[i][1]*j] < t): break
                if(bang[qpop[0]+ang[i][0]*j][qpop[1]+ang[i][1]*j] > t):
                    q.append([qpop[0]+ang[i][0]*j,qpop[1]+ang[i][1]*j])
                    bang[qpop[0]+ang[i][0]*j][qpop[1]+ang[i][1]*j] = t
                    if([qpop[0]+ang[i][0]*j,qpop[1]+ang[i][1]*j] == end):
                        br = 1
                        break
            if(br):break
        if(br):break
    if(br):break
if(br == 0):t = -1
print(t)