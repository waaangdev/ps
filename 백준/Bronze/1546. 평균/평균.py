a = int(input())
b = list(map(int,input().split()))
c = max(b)
b = [i/c *100 for i in b]
d = 0
for i in range(len(b)):
    d += b[i]
print(d/len(b))