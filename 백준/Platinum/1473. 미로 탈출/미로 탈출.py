import sys
from collections import deque

a,b = map(int,sys.stdin.readline().split())
ang = [[0,1],[1,0],[0,-1],[-1,0]]
dum = {'C':1,'D':0}
m = []
for i in range(a):
    m.append(sys.stdin.readline())

q = deque([[0,0,0b0]])
bang = {}
br = 0
t = 0
while q:
    t+=1
    #print(q)
    for i in range(len(q)):
        qpop = q.popleft()
        dum3 = m[qpop[0]][qpop[1]]
        for j in range(4):
            if(qpop[0]+ang[j][0] < a and qpop[1]+ang[j][1] < b and qpop[0]+ang[j][0] > -1 and qpop[1]+ang[j][1] > -1):
                dum2 = m[qpop[0]+ang[j][0]][qpop[1]+ang[j][1]]
                dum5 = False
                dum6 = False
                if(dum2 != 'B'):
                    dum5 = True
                    dum6 = True
                    if(dum3 != 'A'):
                        dum5 = (dum[dum3]+1*(qpop[2] & (1<<(qpop[0])*b+(qpop[1])) != 0))%2 == j%2
                    if(dum2 != 'A'):
                        dum6 = (dum[dum2]+1*(qpop[2] & (1<<(qpop[0]+ang[j][0])*b+(qpop[1]+ang[j][1])) != 0))%2 == j%2
                if(dum5 and dum6):
                    if(qpop[2] not in bang):
                        bang[qpop[2]] = []
                    if([qpop[0]+ang[j][0],qpop[1]+ang[j][1]] not in bang[qpop[2]]):
                        q.append([qpop[0]+ang[j][0],qpop[1]+ang[j][1],qpop[2]])
                        bang[qpop[2]].append([qpop[0]+ang[j][0],qpop[1]+ang[j][1]])
                        if([qpop[1]+ang[j][1],qpop[0]+ang[j][0]] == [b-1,a-1]):
                            br = 1
                            break
        if(br):break
        dum4 = qpop[2]
        for j in range(2):
            st = ang[j*-1+1][:]
            st[j] *= qpop[j]
            for k in range(10):
                if((j == 0 and st[j*-1+1] == b) or (j == 1 and st[j*-1+1] == a)):
                    break
                #print(st)
                if(dum4 & (1<<(st[0]*b+st[1])) == 0):
                    dum4 |= (1<<(st[0]*b+st[1]))
                else:
                    dum4 &= ~(1<<(st[0]*b+st[1]))
                st[j*-1+1] += 1
                
        #print(bin(dum4),qpop)
        if(dum4 not in bang):
            bang[dum4] = []
        if([qpop[0],qpop[1]] not in bang[dum4]):
            q.append([qpop[0],qpop[1],dum4])
            bang[dum4].append([qpop[0],qpop[1]])
    if(br):break
if(br == 0):t = -1
print(t)
