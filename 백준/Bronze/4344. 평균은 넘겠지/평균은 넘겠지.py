a = int(input())
b = []
c = 0
d = 0
for j in range(a):
    c = 0
    d = 0
    b = list(map(int,input().split()))
    del b[0]
    for k in range(len(b)):
        c += b[k]
    c /= len(b)
    for k in range(len(b)):
        if (b[k] > c):
            d += 1 
    print(f"{d/len(b)*100:.3f}%")