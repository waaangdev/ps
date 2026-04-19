import sys
from collections import deque

# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

#3152

li = list(map(int,sys.stdin.readline().split()))
p = li[0]
li = li[1:]
rl = [0,0,0,0]
ri = -1

for x2 in li:
    ri+=1
    li = [0 for i in range(40)]
    x = x2
    for i in range(40):
        dum = x%p**(i+1)
        x-=dum
        li[i] = dum//p**(i)
        if(x <= 0):break
    #print(li)
    if(max(li) > 2):
        rl[ri] = 0
        continue
    if((li.count(1) ==1) and sum(li)!=1):
        rl[ri]=1
    if(li.count(1) ==2 and sum(li)==2):
        rl[ri]=1

print(*rl)