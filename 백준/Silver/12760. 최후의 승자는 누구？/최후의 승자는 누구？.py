import sys
from collections import deque
a,b = map(int,input().split())
sc = [0 for i in range(a)]
m = []
for i in range(a):
    m.append(deque(sorted(list(map(int,input().split())))))
for i in range(b):
    c = 0
    m2 = [] 
    for j in range(a):
        e = m[j].popleft()
        if(e > c):
            m2 = [j]
            c = e
        elif(c==e):
            m2.append(j)
    for j in range(len(m2)):
        sc[m2[j]] +=1
m2 = [] 
c = 0
for j in range(a):
    e = sc[j]
    if(e > c):
        m2 = [j+1]
        c = e
    elif(c==e):
        m2.append(j+1)
m2.sort()
print(*m2)