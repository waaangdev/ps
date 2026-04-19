import sys
a,b = map(int,input().split())
c = {}
c1 = {}
for i in range(a):
    q = sys.stdin.readline().strip()
    c[q] = i
    c1[str(i)] = q
for i in range(b):
    d = (sys.stdin.readline().strip())
    try:
        d = int(d)
    except ValueError:
        print(int(c.get(d,0))+1)
    else:
        print(c1.get(str(d-1),0))