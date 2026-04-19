import sys
li = [[] for i in range(4)]
n = int(input())
for i in range(n):
    inp = list(map(int,sys.stdin.readline().split()))
    for j in range(4):
        li[j]+=[inp[j]]
li2 = {}
for j in range(n):
    for k in range(n):
        dum = li[0][j]+li[1][k]
        if(dum in li2):
            li2[dum]+=1
        else:
            li2[dum]=1
r = 0
for j in range(n):
    for k in range(n):
        dum = -li[2][j]-li[3][k]
        if(dum in li2):
            r+=li2[dum]
print(r)