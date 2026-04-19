n,m = map(int,input().split())
li = sorted(list(map(int,input().split())))
li2 = sorted(list(map(int,input().split())))
bang = [0]*m
r = 0

for i in li:
    d1 = abs(i-li2[0])
    di = 0
    for j in range(m):
        if(abs(i-li2[j]) < d1):
            d1 = abs(i-li2[j])
            di = j
    r += bang[di]
    bang[di] = 1
print(r)
    