a,b = map(int,input().split())
bang = [0 for i in range(a)]
li = [[] for i in range(a)]
r = 0
def dfs(idx):
    bang[idx] = 1
    for i in li[idx]:
        if(bang[i]==0):dfs(i)

for i in range(b):
    c,d = map(int,input().split())
    li[c-1].append(d-1)
    li[d-1].append(c-1)
for i in range(a):
    if(bang[i] == 0):
        r+=1
        bang[i] = 1
        dfs(i)
print(r)