a = int(input())
for i in range(a):
    b = int(input())
    m = []
    m.append(list(map(int,input().split())))
    m.append(list(map(int,input().split())))
    m[0].insert(0,0)
    m[1].insert(0,0)
    for j in range(b):
        for k in range(2):
            if(j!=0):
                m[k][j+1] += max(m[(k-1)*-1][j-1],m[(k-1)*-1][j])
    print(max(m[0][b],m[1][b]))
