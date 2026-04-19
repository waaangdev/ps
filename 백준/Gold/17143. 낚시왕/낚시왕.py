import sys
from collections import deque

a,b,c = map(int,input().split())
m = [0 for i in range(10000)]
m3 = [[-1 for i in range(b)] for j in range(a)]
m2 = []
cmax = a

for i in range(c):
    inp = list(map(int,sys.stdin.readline().strip().split()))
    
    m[inp[4]-1] = [inp[0]-1,inp[1]-1,inp[2],inp[3]-1,inp[4]-1]
    m2.append(inp[4]-1)
    m3[inp[0]-1][inp[1]-1] = inp[4]-1
    if(inp[1]-1 == 0):
        cmax = min(cmax,inp[0]-1)
    
m2 = sorted(m2)

ang = [[-1,0],[1,0],[0,1],[0,-1]]

r = 0

for i in range(b):
    if(cmax != a):
        m[m3[cmax][i]] = 0
        r+=m3[cmax][i]+1
        m3[cmax][i] = -1
    cmax = a
    m4 = [[-1 for i in range(b)] for j in range(a)]
    for j in range(c):
        ppap = m[m2[j]]
        if(ppap != 0):
            if(m3[ppap[0]][ppap[1]] == ppap[4]):
                
                nextang = ppap[3]

                ppap[0] += ((ppap[2]*ang[ppap[3]][0]))

                while (ppap[0] < 0 or ppap[0] >= a):
                    if(ppap[0] < 0):
                        ppap[0] *= -1
                    elif(ppap[0] >= a):
                        ppap[0] -= (a-1)
                        ppap[0] = (a-1)-ppap[0]
                    if(nextang == 0):nextang = 1
                    elif(nextang == 1):nextang = 0
                    elif(nextang == 2):nextang = 3
                    elif(nextang == 3):nextang = 2

                ppap[1] += ((ppap[2]*ang[ppap[3]][1]))

                while (ppap[1] < 0 or ppap[1] >= b):
                    if(ppap[1] < 0):
                        ppap[1] *= -1
                    elif(ppap[1] >= b):
                        ppap[1] -= (b-1)
                        ppap[1] = (b-1)-ppap[1]
                    if(nextang == 0):nextang = 1
                    elif(nextang == 1):nextang = 0
                    elif(nextang == 2):nextang = 3
                    elif(nextang == 3):nextang = 2
                ppap[3] = nextang
                m4[ppap[0]][ppap[1]] = ppap[4]
                
                if(ppap[1] == i+1):
                    cmax = min(cmax,ppap[0])
            else:
                ppap = 0
    m3 = [[k for k in j] for j in m4]
                
print(r)