import sys
li = list(range(1,21))
for i in range(10):
    a,b= map(int,input().split())
    li[a-1:b] = reversed(li[a-1:b])
print(*li)