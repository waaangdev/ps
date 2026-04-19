"1600-말이 되고픈 원숭이.미해결"

import sys
from collections import deque

horse = int(sys.stdin.readline())

mx,my = map(int,sys.stdin.readline().split())
m = []
for i in range(my):
    m.append(list(map(int,sys.stdin.readline().split())))

mbang = [[[m[i][j] for j in range(mx)] for i in range(my)] for _ in range(31)]

ang = [[0,1],[0,-1],[-1,0],[1,0],[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[-2,1],[2,-1],[-2,-1]]

q = deque([[0,0,0]])
lenq = 1
r = 0
br = 0
if(mx+my != 2):
    while lenq != 0:
        r+=1
        for _ in range(lenq):
            popo = q.popleft()
            lenq -= 1
            
            for i in range(12):
                popo2 = [popo[0]+ang[i][0],popo[1]+ang[i][1],popo[2]+(1)*(i>3)]
                if(popo[2] != horse or i < 4):
                    if(popo2[0] >= 0 and popo2[0] < my and popo2[1] >= 0 and popo2[1] < mx):

                        if(mbang[popo2[2]][popo2[0]][popo2[1]] == 0):
                            mbang[popo2[2]][popo2[0]][popo2[1]] = 1
                            q.append(popo2)
                            lenq += 1
                            if([popo2[0],popo2[1]] == [my-1,mx-1]):
                                br = 1
                                break
            if(br):
                break
        if(br):
            break
if(mx+my == 2):
    br = 1          
if(br == 0):
    print(-1)
else:
    print(r)
    