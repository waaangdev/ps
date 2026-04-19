a = int (input())
b = int (input())
c = int (input())
d = str(a*b*c)
f = [0,0,0,0,0,0,0,0,0,0]
for i in range(len(d)):
    f[int(d[i])] += 1
for i in f:
    print(i)