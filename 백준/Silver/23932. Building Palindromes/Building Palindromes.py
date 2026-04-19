import sys
from collections import deque
n = int(input())
for i in range(n):
    r = 0

    li = list(map(int,sys.stdin.readline().strip().split()))

    inp = sys.stdin.readline().strip()
    li2 = [[] for i in range(len(inp))]
    dum = [0 for i in range(26)]
    for j in range(len(inp)):
        dum[ord(inp[j])-ord('A')] += 1
        li2[j] = dum[:]

    for j in range(li[1]):
        inp2 = list(map(int,sys.stdin.readline().strip().split()))
        dum = li2[inp2[1]-1][:]
        if(inp2[0]!= 1):
            for k in range(26):
                dum[k] -= li2[inp2[0]-2][k]
        dum2 = 0
        for k in range(26):
            dum2+=dum[k]%2
        if(dum2 < 2):
            r+=1
    print(f"Case #{i+1}: {r}")
