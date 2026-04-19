def s(a):
    a1 = ["" for i in range(len(a)*3)]
    for i in range(len(a1)):
        for j in range(3):
            if j == 1 and int(i/(len(a))) == 1: a1[i] += ' ' * len(a[i%len(a)])
            else: a1[i] += a[i%len(a)]
    if len(a1) != n: a1 = s(a1)
    return a1

n = int(input())
r = s(['*'])
for i in range(n):
    print(r[i])