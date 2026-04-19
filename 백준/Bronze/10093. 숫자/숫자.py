n,m = map(int,input().split())
a = 0
if (n > m):
    a = m
    m = n
    n = a
r = []
for i in range(n+1,m):
    r.append(i)
print(len(r))
if (abs(m - n) >1):
    for i in range(len(r)-1):
       print(r[i],end=' ')
    print(r[len(r)-1])