import math
p,a,b,c,d,n = map(int,input().split())
f = lambda x:(p*(math.sin(a*x+b) + math.cos(c*x+d) + 2))
r = 0
m = f(1)
for i in range(1,n):
    m = max(m,f(i))
    r = max(r, m-f(i+1))
print(r)