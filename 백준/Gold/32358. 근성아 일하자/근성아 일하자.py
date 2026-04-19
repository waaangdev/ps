import sys
from collections import deque
import random
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))


n = int(sys.stdin.readline())
li = []
x = 0
r = 0
for i in range(n):
    inp = list(map(int,sys.stdin.readline().split()))
    if(inp[0] == 1):
        li.append(inp[1])
    elif(li!=[]):
        li.sort()
        conn = [[0,0,1]]
        mind = abs(x-li[0])
        st = 1
        for j in li:
            conn+=[[j,len(conn)-1,len(conn)+1]]
            if(abs(x-j) < mind):
                st = len(conn)-1
                mind = abs(x-j)
        conn += [[0,len(conn)-1,len(conn)]]
        #print(conn,mind)
        r+=mind
        x = conn[st][0]
        lli = len(li)
        for _ in range(lli-1):
            conn[conn[st][1]][2] = conn[st][2]
            conn[conn[st][2]][1] = conn[st][1]
            if(conn[st][2]==len(conn)-1 or ((abs(conn[conn[st][1]][0] - x) <= abs(conn[conn[st][2]][0] - x)) and conn[st][1]!=0)):
                r+=abs(conn[conn[st][1]][0] - x)
                x = conn[conn[st][1]][0]
                st = conn[st][1]
            else:
                r+=abs(conn[conn[st][2]][0] - x)
                x = conn[conn[st][2]][0]
                st = conn[st][2]
            #print(r,st,x,conn)
        
        li = []
print(r)