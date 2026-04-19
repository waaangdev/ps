a = int(input())
b = list(map(int,input().split()))
c= b[0]
r = 0
rr = 1
for i in range(a):
    if(b[i] > c):
        c = b[i]
        r = 0
    r += 1
    rr = max(rr,r)
print(rr-1)