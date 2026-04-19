import sys
n = int(input())
li = list(map(int,sys.stdin.readline().strip().split()))
li2 = [[0 for i in range(n)] for i in range(n)]
for i in range(n):
    p1 = i
    p2 = i
    while(p1 > -1 and p2 < n and li[p1] == li[p2]):
        li2[p1][p2] = 1
        p1-=1
        p2+=1
    p1 = i
    p2 = i+1
    while(p1 > -1 and p2 < n and li[p1] == li[p2]):
        li2[p1][p2] = 1
        p1-=1
        p2+=1

m = int(input())
for i in range(m):
    inp = list(map(int,sys.stdin.readline().strip().split()))
    print(li2[inp[0]-1][inp[1]-1])