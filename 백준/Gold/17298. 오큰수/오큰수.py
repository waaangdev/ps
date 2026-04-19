from collections import deque
input()
a = list(map(int,input().split()))
li = deque([])
li2 = []
for i in range(len(a)-1,-1,-1):
    if(len(li) == 0):
        li = deque([a[i]])
        c = -1
    else:
        b = len(li)
        for j in range(b):
            if(li[0] <= a[i]):
                li.popleft()
            else:
                c = li[0]
                li.appendleft(a[i])
                break
        if(len(li) == 0):
            li = deque([a[i]])
            c = -1
    li2.append(c)
print(*reversed(li2))