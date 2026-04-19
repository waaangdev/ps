a,b = map(int,input().split())
li2 = list(map(int,input().split()))
li1 = list(map(int,input().split()))
for i in range(b):
    new = [0 for j in range(a)]
    for j in range(a):
        new[li1[j]-1] = li2[j]
    li2 = new[:]
print(*li2)