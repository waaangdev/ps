"휴대폰 자판"

import sys 
from collections import deque
inp = ["" for i in range(100000)]
while True:
    try:
        a = int(sys.stdin.readline())
    except:
        break
    tri = [[],{}]
    for i in range(a):
        inp[i] = sys.stdin.readline().strip()
        point = tri
        leninp = len(inp[i])
        for j in range(leninp):
            if(inp[i][j] in point[1]):
                point = point[1][inp[i][j]]
                if(j == leninp-1):
                    point[1]['end'] = 1
                
            else:
                point[0].append(inp[i][j])
                if(j == leninp-1):
                    point[1][inp[i][j]] = [[],{'end':1}]
                else:
                    point[1][inp[i][j]] = [[],{}]
                point = point[1][inp[i][j]]
    #print(tri)
    q = deque([[tri,1]])
    r= 0
    dum =0
    once = 1
    while q:
        dum = 0
        #print(q)
        qpop = q.popleft()
        if('end' in qpop[0][1]):
            r+=qpop[1]
            #print(qpop[1])
            dum = 1
        if(len(qpop[0][0]) > 1):
            dum = 1
        for i in qpop[0][0]:
            q.append([qpop[0][1][i],qpop[1]+max(0,dum-once)])
        once = 0
        
    r /= a
    print(str(round(r,2)).ljust(4,"0"))