import sys
from collections import deque
import random
import math
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

sys.setrecursionlimit(100001)

n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
if(n == 1):
    print(1)
else:
    d = dict()

    li2 = sorted([(li[i],i) for i in range(n)])

    li3 = [0 for i in range(n)]
    for i in range(n):
        li3[li2[i][1]] = i+1

    conn = [[0,0,1]]

    for i in range(n):
        conn.append([li2[i][0],i,i+2])

    conn.append([0,n,n+1])

    #print(li2)
    #print(li3)

    #print(conn)
    def dins(num):
        if(num in d):
            d[num]+=1
        else:
            d[num]=1
    def ddel(num):
        d[num]-=1
        if(d[num] == 0):
            del d[num]

    rl = []

    for i in range(1,n):
        dins(conn[i+1][0]-conn[i][0])

    if(len(d) == 1):
        rl.append(1)
    else:
        rl.append(0)


    c = n-1
    for i in li3[:1:-1]:
        #print(conn,d)
        if(conn[conn[i][1]][0]!=0):ddel(abs(conn[i][0]-conn[conn[i][1]][0]))
        if(conn[conn[i][2]][0]!=0):ddel(abs(conn[i][0]-conn[conn[i][2]][0]))

        conn[conn[i][1]][2] = conn[i][2]
        conn[conn[i][2]][1] = conn[i][1]
        c-=1
        if(conn[conn[i][1]][0]!=0 and conn[conn[i][2]][0]!=0):
            dum = abs(conn[conn[i][2]][0]-conn[conn[i][1]][0])

            dins(dum)
        if(len(d)==1):
            rl.append(1)
        else:
            rl.append(0)
    rl.append(1)
    print('\n'.join([str(i) for i in rl[::-1]]))