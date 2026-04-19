import sys
a = int(input())
li = {}
li3 = []
for i in range(a):
    li2 = list(map(int,sys.stdin.readline().split()))
    if(li2[0] in li):
        li[li2[0]].append(li2[1])
    else:
        li[li2[0]] = [li2[1]]
        li3.append(li2[0])
li3.sort()
for i in li3:
    li[i].sort()
    for j in li[i]:
        print(i,j)