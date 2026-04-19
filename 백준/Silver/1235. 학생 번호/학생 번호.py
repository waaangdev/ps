import sys
sys.setrecursionlimit(10001)

n = int(input())
strs = []
for _ in range(n):
    st = sys.stdin.readline().strip()
    strs.append(st)
le = len(st)

def sol(li,n):
    dum = [[] for i in range(10)]
    r = 0
    for i in li:
        dum[ord(strs[i][n])-ord('0')].append(i)
    for i in range(10):
        if(len(dum[i])>1):
            r = max(r,sol(dum[i],n-1))
    return r+1

print(sol([i for i in range(n)],le-1))