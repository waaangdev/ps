n1 = int(input())
m = [0 for i in range(n1)]
for i in range(n1):
    m[i] = input()
def a(n,r,c):
    if(n == 1):
        return m[c][r]
    q = a(n//2,r,c)
    w = a(n//2,r+n//2,c)
    e = a(n//2,r,c+n//2)
    r =a(n//2,r+n//2,c+n//2)
    if(q == w and w == e and e == r and len(q) == 1):
        return q
    return "("+q+w+e+r+")"
print(a(n1,0,0))