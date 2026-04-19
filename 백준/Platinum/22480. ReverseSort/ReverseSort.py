"ReverseSort"

import sys
from collections import deque
import math
import random

#O(n!*n^2) 으로 해결 가능!!!!!!!!!!
#일단 나이브로 먼저 짜볼것...

n = int(sys.stdin.readline())
li = int(''.join(list(map(lambda x:str(int(x)-1),sys.stdin.readline().split()))))
bang = [dict(),dict()]
pow = [int(math.pow(10,i)) for i in range(10)]
pre = [[[[0 for i in range(10)] for i in range(10)]for i in range(10)]for i in range(10)]
ends = int("0123456789"[:n])
minr = 10

def sol():
    global minr 
    stqpop = [0 for i in range(n)]
    q = deque([[li,0],[ends,1]])
    bang[0][li] = 0
    bang[1][ends] = 0
    if(li == ends):return 0
    t = 0
    br = 1
    minr = 10
    while q and br:
        t +=1
        lenq = len(q)
        #if(t==5):break
        #print(lenq,len(bang))
        for _ in range(lenq):
            qpop = q.popleft()

            dum = qpop[0]
            for i in range(n):
                stqpop[n-i-1] = dum%10
                dum//=10
            for i2 in range(0,2):
                for i in range(1-i2,n-1):
                    qdum = qpop[0]
                    p = [i-1+i2,i+1]
                    while(p[0]!=-1 and p[1]!=n):
                        if(pre[p[0]][p[1]][stqpop[p[0]]][stqpop[p[1]]] ==0):
                            dum= 0
                            dum -= stqpop[p[0]]*pow[n-p[0]-1]
                            dum -= stqpop[p[1]]*pow[n-p[1]-1]
                            dum += stqpop[p[1]]*pow[n-p[0]-1]
                            dum += stqpop[p[0]]*pow[n-p[1]-1]
                            pre[p[0]][p[1]][stqpop[p[0]]][stqpop[p[1]]] = dum
                        qdum +=pre[p[0]][p[1]][stqpop[p[0]]][stqpop[p[1]]]
                        #qdum[p[0]],qdum[p[1]]=qdum[p[1]],qdum[p[0]]
                        if(qdum not in bang[qpop[1]]):
                            if(qdum in bang[1-qpop[1]]):
                                br = 0
                                minr = min(minr , t+bang[1-qpop[1]][qdum])
                                return (t+bang[1-qpop[1]][qdum])
                            bang[qpop[1]][qdum]=t
                            q.append([qdum,qpop[1]])
                        p = [p[0]-1,p[1]+1]
       # break
    return minr
print(sol())
# for i in range(5):
#     pre_r[i].sort()
#     dum = 0
#     for j in range(len(pre_r[i])):
#         dum,pre_r[i][j] = pre_r[i][j],hex(pre_r[i][j]-dum)[2:]
#     print(','.join(pre_r[i]))
#     print(len(pre_r[i]))