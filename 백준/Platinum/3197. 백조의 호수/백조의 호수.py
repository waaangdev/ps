import sys
from collections import deque

a,b = map(int,input().split())

bing_m = [0b0 for _ in range(a)]
bing_ga_q = deque([])

bak_st = []

ang = [[0,1],[-1,0],[0,-1],[1,0]]

for i in range(a+1):
    if(i != a):
        inp = sys.stdin.readline().strip()
        for j in range(b):
            if(inp[j] == 'X'):
                bing_m[i] |= (1 << (j))
            elif(inp[j] == 'L'):
                bak_st.append([i,j])
                bing_ga_q.append([(i),j])
            else:
                bing_ga_q.append([(i),j])
                
                    
bak_q = [deque([bak_st[0]]),deque([])]
bak_m = [0b0 for _ in range(a)]
t= 0
br = 0
dum3 = 0
while 1:
    t+=1

    lenbingq = len(bing_ga_q)
    for _ in range(lenbingq):
        popo = bing_ga_q.popleft()
        
        for k in range(4):
            if(popo[0]+ang[k][0] < a and popo[0]+ang[k][0] >= 0 and popo[1]+ang[k][1] < b and popo[1]+ang[k][1] >= 0):
                if(bing_m[popo[0]+ang[k][0]] & (1<<popo[1]+ang[k][1]) != 0):
                    bing_ga_q.append([popo[0]+ang[k][0],popo[1]+ang[k][1]])
                    bing_m[popo[0]+ang[k][0]] &= ~(1<<(popo[1]+ang[k][1]))


    dum2 = 0
    while 1:    
        lenbakq = len(bak_q[dum3])
        if(lenbakq == 0):break
        for _ in range(lenbakq):
            popo = bak_q[dum3].pop()

            dum = 0
            for k in range(4):
                if((popo[0])+ang[k][0] < a and (popo[0])+ang[k][0] >= 0 and popo[1]+ang[k][1] < b and popo[1]+ang[k][1] >= 0):
                    if(bak_m[(popo[0])+ang[k][0]] & (1<<(popo[1]+ang[k][1])) == 0):
                        if(bing_m[(popo[0])+ang[k][0]] & (1<<(popo[1]+ang[k][1])) == 0):
                            bak_q[dum3].appendleft([(popo[0])+ang[k][0],popo[1]+ang[k][1]])
                            bak_m[popo[0]+ang[k][0]] |= (1<<(popo[1]+ang[k][1]))
                        else:
                            bak_q[(dum3-1)*-1].append([(popo[0]),popo[1]])
                
            if(popo[0] == bak_st[1][0] and popo[1] == bak_st[1][1]):
                br = 1
                break


        if(br == 1):break
        
    if(br == 1):break
    
    dum3 = (dum3-1)*-1
    
print(t)