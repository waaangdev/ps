a = int(input())
m = []
for i in range(a):
    m.append(list(map(int,input().split())))
for i in range(1,a):
    for j in range(len(m[i])):
        if(j == 0):
            m[i][j] += m[i-1][j]
        elif(j == len(m[i])-1):
            m[i][j] += m[i-1][j-1]
        else:
            m[i][j] += max(m[i-1][j],m[i-1][j-1])
r = 0
for j in range(len(m[len(m)-1])):
    r = max(r,m[len(m)-1][j])
print(r)