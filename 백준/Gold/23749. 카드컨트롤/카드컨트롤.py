import sys
from collections import deque
import random
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))


n = int(sys.stdin.readline())
li1 = ''.join(sys.stdin.readline().split())
li = []
for i in li1:
    if(i=="O"):
        li.append(1)
    else:
        li.append(0)
def score(li):
    return sum(li[::2])-sum(li[1::2])

if(score(li) > 0):
    print(0)
else:
    q = deque([li])
    t = 1
    bang = [0 for i in range(2**11)]
    r = 0
    while q and r==0:
        lenq = len(q)
        for i in range(lenq):
            qpop = q.popleft()
            for j in range(1,len(qpop)):
                li2 = qpop[:]
                dum = li2[j]
                del li2[j]
                li2 = [dum]+li2

                dum2 = sum([li2[k]*2**k for k in range(len(li2))])
                if(bang[dum2] == 0):
                    if(score(li2)>0):
                        r =t
                        break
                    bang[dum2] = 1

                    q.append(li2)



        t+=1
    print(r)