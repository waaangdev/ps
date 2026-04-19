a = int(input())
li = list(map(int,input().split()))
lis = sorted(li)
r = [0,0]

li2 = []
dum = []
for i in range(a-1):
    if(li[i]%2 != li[i+1]%2):
        dum +=[li[i]]
        li2 += sorted(dum)
        dum = []
    else:
        dum +=[li[i]]
dum +=[li[a-1]]
li2 += sorted(dum)
if(li2 != lis):
    r[1] = 1

dum = [0,0]
for i in range(a):
    if(li[i] >= dum[li[i]%2]):
        dum[li[i]%2] = li[i]
    else:
        r[0] = 1

print(["So Lucky","Unlucky"][r[0]])
print(["So Lucky","Unlucky"][r[1]])