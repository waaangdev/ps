a = int(input())
m = []
for i in range(a):
    m.append(list(map(int,input().split())))
for i in range(1,a):
    for j in range(3):
        m[i][j] += min(m[i-1][(j+1)%3],m[i-1][(j-1)%3])
print(min(min(m[a-1][0],m[a-1][1]),m[a-1][2]))