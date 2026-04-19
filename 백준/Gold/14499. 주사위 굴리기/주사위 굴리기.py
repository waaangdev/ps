n,m,y,x,k = map(int,input().split())
ma = []
r = [[0,0,0,0],
     [0,0]]
r1 = [[0,3],
     [0,4],
     [4,0]]
r2 = [0,0,0,0]
for _ in range(n):
    ma.append(list(map(int,input().split())))
g = list(map(int,input().split()))
for i in range(k):
    if ((g[i]-1)//2 == 0 and not (x - ((g[i]-1)%2 * 2 -1) == -1 or x - ((g[i]-1)%2 * 2 -1) == m)):
        x -= (g[i]-1)%2 * 2 -1
        r[0].insert(r1[2][(g[i]-1)%2], r[0][r1[0][(g[i]-1)%2]])
        del r[0][r1[1][(g[i]-1)%2]]
        if (ma[y][x] == 0):
            ma[y][x] = r[0][2]
        else:
            r[0][2] = ma[y][x]
            ma[y][x] = 0
        print(r[0][0])
    elif ((g[i]-1)//2 == 1 and not (y + ((g[i]-1)%2 * 2 -1) == -1 or y + ((g[i]-1)%2 * 2 -1) == n)):
        y += (g[i]-1)%2 * 2 -1
        r2 = [r[0][0],r[1][0],r[0][2],r[1][1]]
        r2.insert(r1[2][(g[i]-1)%2], r2[r1[0][(g[i]-1)%2]])
        del r2[r1[1][(g[i]-1)%2]]
        r[0][0] = r2[0]
        r[1][0] = r2[1]
        r[0][2] = r2[2]
        r[1][1] = r2[3]
        if (ma[y][x] == 0):
            ma[y][x] = r[0][2]
        else:
            r[0][2] = ma[y][x]
            ma[y][x] = 0
        print(r[0][0])