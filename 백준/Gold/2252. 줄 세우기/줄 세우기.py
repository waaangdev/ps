from collections import deque
import sys
n,m = map(int,input().split())
li = [[] for i in range(n)]
li2 = [0 for i in range(n)]
for i in range(m):
    inp =  list(map(int,sys.stdin.readline().strip().split()))
    li2[inp[0]-1] += 1
    li[inp[1]-1].append(inp[0]-1)
    
li3=[]
li3 = deque([])
lele = 0
for i in range(n):
    if(li2[i] == 0):
        li3.append(i)
        lele += 1
r = []
while 1:
    
    if(lele == 0):
        break
    pop = li3.popleft()
    lele -= 1
    for i in range(len(li[pop])):
        li2[li[pop][i]] -= 1
        if(li2[li[pop][i]] == 0):
            li3.append(li[pop][i])
            lele += 1

    r.append(pop+1)
print(*reversed(r))