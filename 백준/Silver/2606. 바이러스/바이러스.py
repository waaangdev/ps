a = int(input())
b = int(input())
way = [[] for i in range(a+1)]
bang = [0 for i in range(a+1)]
for i in range(b):
    inp = list(map(int,input().split()))
    way[inp[0]].append(inp[1])
    way[inp[1]].append(inp[0])
q = [1]
bang[1] = 1
r = 0
while q:
    r+=1
    for i in way[q[0]]:
        if(bang[i] == 0):
            bang[i] = 1
            q.append(i)
    del q[0]
print(r-1)