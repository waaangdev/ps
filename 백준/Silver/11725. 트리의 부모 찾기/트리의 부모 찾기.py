import sys
sys.setrecursionlimit(100001)
a = int(input())
b= a-1
bang = [0 for i in range(a)]
li = [[] for i in range(a)]
r = [0 for i in range(a)]
def dfs(idx):
    bang[idx] = 1
    for i in li[idx]:
        if(bang[i]==0):
            r[i] = idx
            dfs(i)

for i in range(b):
    c,d = map(int,sys.stdin.readline().strip().split())
    li[c-1].append(d-1)
    li[d-1].append(c-1)
bang[0]=1
dfs(0)

print("\n".join(list(map(lambda x: str(x+1),r[1:]))))