import sys
sys.setrecursionlimit(10000)

def f(b):
    global li2
    if(li2[b] != -1):
        return li2[b]
    if(b == 0):
        return 0
    li3 = [10000000 for i in range(len(li))]
    for i in range(len(li)):
        if(b-li[i] >= 0):
            li3[i] = f(b-li[i])+1

    li2[b] = min(li3)
    return min(li3)

a,b = map(int,input().split())
li = set([])
for i in range(a):
    li.add(int(input()))
li = list(li)
li2 = [-1 for i in range(b+1)]

r = f(b)
if(r >= 10000000):
    r = -1
print(r)