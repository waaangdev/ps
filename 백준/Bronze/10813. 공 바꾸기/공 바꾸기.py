a,b= map(int,input().split())
li = [i+1 for i in range(a)]
for i in range(b):
    c,d = map(int,input().split())
    e = li[c-1]
    li[c-1] = li[d-1]
    li[d-1] = e
print(*li)