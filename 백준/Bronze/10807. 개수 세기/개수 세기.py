a = int(input())
b = list(map(int,input().split()))
c = int(input())
d = 0
for i in range(len(b)):
    if b[i] == c:
        d += 1
print(d)