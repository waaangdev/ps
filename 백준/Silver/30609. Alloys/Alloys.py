import sys
from collections import deque
n=int(input())
q=deque()
li = []
for i in range(n):
    a,b,c = input().split()
    li.append([float(b),float(c),a])
li.sort()
for i in li:
   while (1):
       if(len(q)==0):
           q.append(i)
           break
       qpop = q.pop()
       if(qpop[1] >= i[1]):
           q.append(qpop)
           q.append(i)
           break
       else:
           if(len(q)==0):
               q.append(i)
               break
q=list(q)
q.sort(key=lambda x:x[2])
print(" ".join([i[2] for i in q]))