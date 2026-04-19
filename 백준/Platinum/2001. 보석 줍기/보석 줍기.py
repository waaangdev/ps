import sys
from collections import deque

a,b,c = map(int,input().split())

li1 = [-1 for i in range(a)]

for i in range(c):
    li1[int(sys.stdin.readline().strip())-1] = i

m1 = [[-1 for _ in range(a)] for _ in range(a)]
for i in range(b):
    inp = list(map(int,sys.stdin.readline().strip().split()))
    m1[inp[0]-1][inp[1]-1] = inp[2]
    m1[inp[1]-1][inp[0]-1] = inp[2] 



li = deque([[0,0,0b000000000000000]])
li2 = [0b0 for _ in range(16385)]
max_ = 0
while 1:
    lenli = len(li)
    if(lenli == 0):
        break
    for i in range(lenli):
        popo = li.popleft()

        next_ = 0b0
        ne2 = 0
        if(li1[popo[0]] != -1):
            if(popo[2] & (1 << (li1[popo[0]])) == 0):
                next_ = 1 << (li1[popo[0]])
                ne2 = 1
        if(popo[0] == 0): max_ = max(max_,popo[1]+ne2)

        for j in range(a):
            if(m1[popo[0]][j] >= popo[1]): 
                if(li2[popo[2]] & (1 << j) == 0):
                    li2[popo[2]] |= (1<<(j))
                    li.append([j,popo[1],popo[2]])
            if(m1[popo[0]][j] >= popo[1]+ ne2): 
                if(li2[popo[2]| next_] & (1 << j) == 0):
                    li2[popo[2]| next_] |= (1<<(j))
                    li.append([j,popo[1] + ne2,popo[2] | next_])
print(max_)