import sys
from collections import deque

a,b = map(int,sys.stdin.readline().split())
m = []
q = deque([])
end = []
ang = [[0,1],[-1,0],[1,0],[0,-1]]
li = ['0','1','2','3','4']
cnt = 0
for i in range(b):
    m.append(list(sys.stdin.readline()))
    for j in range(a):
        if(m[i][j] == 'S'):
            q = deque([[i,j,0b0]])
        if(m[i][j] == 'E'):
            end = [i,j]
        if(m[i][j] == 'X'):
            m[i][j] = str(cnt)
            cnt += 1

bang = [[0b0 for i in range(b)] for j in range(0b111111)]

r = 0
br = 0
while q:
    r+=1
    lenq = len(q)
    for i in range(lenq):
        qpop = q.popleft()
        for j in range(4):
            if(qpop[0]+ang[j][0] > -1 and qpop[0]+ang[j][0] < b and qpop[1]+ang[j][1] < a and qpop[1]+ang[j][1] > -1):
                if(m[qpop[0]+ang[j][0]][qpop[1]+ang[j][1]] != '#'):
                    if(not bang[qpop[2]][qpop[0]+ang[j][0]] & (1<<qpop[1]+ang[j][1])):
                        if(m[qpop[0]+ang[j][0]][qpop[1]+ang[j][1]] == 'E' and qpop[2] == (2**cnt)-1):
                            br = 1
                        if(m[qpop[0]+ang[j][0]][qpop[1]+ang[j][1]] in li):
                            dum = qpop[2] | (1<<int(m[qpop[0]+ang[j][0]][qpop[1]+ang[j][1]]))
                            q.append([qpop[0]+ang[j][0],qpop[1]+ang[j][1],dum])
                            bang[dum][qpop[0]+ang[j][0]] |= (1<<qpop[1]+ang[j][1])
                        else:
                            q.append([qpop[0]+ang[j][0],qpop[1]+ang[j][1],qpop[2]])
                            bang[qpop[2]][qpop[0]+ang[j][0]]|= (1<<qpop[1]+ang[j][1])
                            
            if(br == 1):break
        if(br == 1):break
    if(br == 1):break
if(br == 1):print(r)