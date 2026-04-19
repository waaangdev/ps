import sys
from collections import deque

inp = sys.stdin.readline().rstrip()
a = 0
for i in range(len(inp)):
    a+=int(inp[i])*(2**(len(inp)-i-1))
    
inp = sys.stdin.readline().rstrip()
b = 0
for i in range(len(inp)):
    b+=int(inp[i])*(2**(len(inp)-i-1))
q = deque([a])
bang = [True] * (0b11111111111) 


r = 0
while q:
    lenq = len(q)
    r+=1
    for i in range(lenq):
        qpop = q.popleft()
        if(qpop == b):
            break
        if(qpop+1 < len(bang)):
            if(bang[qpop+1]):
                q.append(qpop+1)
                bang[qpop+1] = False
        if(qpop > 0):
            if(bang[qpop-1]):
                q.append(qpop-1)
                bang[qpop-1] = False

        for j in range(len(bin(qpop))-3):
            if(qpop & (1<<j) == 0 and (qpop | (1<<j)) < len(bang)):
                if(bang[qpop | (1<<j)]):
                    q.append(qpop | (1<<j))
                    bang[qpop | (1<<j)] = False
            if(qpop & (1<<j) != 0):
                if(bang[qpop & ~(1<<j)]):
                    q.append(qpop & ~(1<<j))
                    bang[qpop & ~(1<<j)] = False
    if(qpop == b):
        break
print(r-1)