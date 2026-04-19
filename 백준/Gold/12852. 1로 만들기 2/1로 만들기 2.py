import sys
from collections import deque

a = int(input())

li = deque([[a,[a]]])
br = 0
t = 0
li2 = [0 for i in range(a)]
while 1:
    if len(li) == 0:
        break
    t+=1
    for i in range(len(li)):
        popo = li.popleft()
        if(popo[0] == 1):
            br = 1
            r = popo[1]
            break
        if(popo[0]%2 == 0):
            if(li2[popo[0]//2] == 0):
                li.append([popo[0]//2,popo[1]+[popo[0]//2]])
                li2[popo[0]//2] = 1
        if(popo[0]%3 == 0):
            if(li2[popo[0]//3] == 0):
                li.append([popo[0]//3,popo[1]+[popo[0]//3]])
                li2[popo[0]//3] = 1
        if(li2[popo[0]-1] == 0):
            li.append([popo[0]-1,popo[1]+[popo[0]-1]])
            li2[popo[0]-1] = 1
    if(br == 1):break
print(t-1)
print(*r)