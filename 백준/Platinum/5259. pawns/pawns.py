"pawns"

import sys
from collections import deque

mx = int(sys.stdin.readline())

m = list(map(int,sys.stdin.readline().split()))

bw = [0b0,0b0]


bw_c = [0,0]

for i in range(mx):
    if(m[i] != 0):
        bw[(m[i]-1)*-1+1] |= (1<<i)
        bw_c[(m[i]-1)*-1+1] +=1
q = deque([(bw[0],bw[1],())])

bw_goal = [0,0]
for j in range(bw_c[0]): 
    bw_goal[0] |= (1<<(mx-1-j))
for j in range(bw_c[1]):
    bw_goal[1] |= (1<<(j))

t = 0
r = 0
bang = set([])
qwe = bw[0]*(2**15)+bw[1]
bang.add(qwe)
while 1:
    t+=1
    for i in range(len(q)):
        qpop = q.popleft()
        
        for i in range(mx):
            for j in range(2):
                if((j == 0 and i < mx-1) or (j == 1 and i > 0)):
                    if(qpop[j] & (1<<i) != 0):
                        boo = 0
                        if(qpop[j*-1+1] & (1<<(i+1-2*(j==1))) == 0 and qpop[j] & (1<<(i+1-2*(j==1))) == 0):
                            bw2 = qpop[j] & ~(1<<i)
                            bw2 |= (1<<(i+1-2*(j==1)))
                            boo = 1
                        elif((j == 0 and i < mx-2) or (j == 1 and i > 1)):
                            if(qpop[j*-1+1] & (1<<(i+2-4*(j==1))) == 0 and qpop[j] & (1<<(i+2-4*(j==1))) == 0):
                                bw2 = qpop[j] & ~(1<<i)
                                bw2 |= (1<<(i+2-4*(j==1)))
                                boo = 1
                        if(boo==1):
                            if(j == 0):
                                qwe = bw2*(2**15)+qpop[1]
                                if(qwe not in bang):
                                    q.append([bw2,qpop[1],tuple(list(qpop[2])+[i+1])])
                                    bang.add(qwe)
                                    if(bw2 == bw_goal[0] and qpop[1] == bw_goal[1]):
                                        r = list(qpop[2])+[i+1]
                                        break
                            else:
                                qwe = qpop[0]*(2**15)+bw2
                                if(qwe not in bang):
                                    q.append([qpop[0],bw2,tuple(list(qpop[2])+[i+1])])
                                    bang.add(qwe)
                                    if(bw2 == bw_goal[1] and qpop[0] == bw_goal[0]):
                                        r = list(qpop[2])+[i+1]
                                        break
            if(r!=0):
                break
        if(r!=0):
            break
    if(r!=0):
        break
print(t)
print(*r)