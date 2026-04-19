#abbc
import sys
from collections import deque

def ss(s):
    dp = deque([(0,0,0,0)])
    for i in range(len(s)):
        dp = deque(set(dp))

        if(s[i]=="A"):
            ldp = len(dp)
            for j in range(ldp):
                dum = list(dp.popleft())
                dum[0]+=1
                dp.append(tuple(dum))
        if(s[i]=="B"):
            ldp = len(dp)
            for j in range(ldp):
                dum = list(dp.popleft())
                dum2 = dum[:]
                if(dum[0]!=0):
                    dum[0]-=1
                    dum[3]+=1
                    dp.append(tuple(dum))
                dum2[1]+=1
                dp.append(tuple(dum2))
        if(s[i]=="C"):
            ldp = len(dp)
            for j in range(ldp):
                dum = list(dp.popleft())
                dum2 = dum[:]
                if(dum[1]!=0):
                    dum[1]-=1
                    dum[3]+=1
                    dp.append(tuple(dum))
                else:
                    dum2[2]+=1
                    dp.append(tuple(dum2))
    return (max(list(map(lambda x:x[3],list(dp)))))

def sol2(s):
    li = list(s)

    r= 0
    la = deque([])
    for i in range(len(li)):
        if(li[i] == "B"):
            la.append(i)
        if(li[i] == "C"):
            if(la):
                dum = la.popleft()
                r+=1
                li[dum] = 'D'
                li[i] = 'D'

    la = deque([])
    for i in range(len(li)):
        if(li[i] == "A"):
            la.append(i)
        if(li[i] == "B"):
            if(la):
                dum = la.pop()
                r+=1
                li[dum] = 'D'
                li[i] = 'D'
    return r

inp = (sys.stdin.readline().strip())
print(sol2(inp))
# for _ in range(int(input())):
#     inp = (sys.stdin.readline().strip())
#     if(ss(inp)!=sol2(inp)):
#         print(sol2(inp),ss(inp))
#         break