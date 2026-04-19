a,b = map(int,input().split())
s = [[0 for j in range(100)] for i in range(100)]
for i in range(a):
    c1,c2,d1,d2 = map(int,input().split())
    for j in range(c1,d1+1):
        for k in range(c2,d2+1):
            s[k-1][j-1]+=1
r = 0
for i in range(100):
    for j in range(100):
        if(s[i][j] > b): r+=1
print(r)