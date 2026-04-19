import sys
from collections import deque

a,b = map(int,input().split())
m = []
ang = [[-1,0],[0,-1],[0,1],[1,0]]
for i in range(a):
    m.append(sys.stdin.readline().strip())
r = 1
li = deque([[0,0,[0 for i in range(26)],1]])
li[0][2][ord(m[li[0][0]][li[0][1]])-65] = 1
while 1:
    lele = len(li)
    if (lele == 0):
        break
    for i in range(len(li)):
        qwe = li.popleft()
        for j in range(4):
            if(qwe[0] + ang[j][0] >= 0 and qwe[0] + ang[j][0] < a and qwe[1] + ang[j][1] >= 0 and qwe[1] + ang[j][1] < b):
                if(qwe[2][ord(m[qwe[0] + ang[j][0]][qwe[1] + ang[j][1]])-65] == 0):
                    qwe[2][ord(m[qwe[0] + ang[j][0]][qwe[1] + ang[j][1]])-65] = 1
                    r = max(r,qwe[3]+1)
                    li.appendleft([qwe[0] + ang[j][0],qwe[1] + ang[j][1],qwe[2][:],qwe[3]+1])
                    qwe[2][ord(m[qwe[0] + ang[j][0]][qwe[1] + ang[j][1]])-65] = 0
    if(r == a*b):
        break
print(r)