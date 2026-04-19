maps = []
for i in range(5):
    maps.append(list(map(int,input().split())))

maps_b = [[0 for i in range(5)] for i in range(5)]
def sol(x,y,left):
    if(left == 0):
        return (maps[x][y]==1)*1
    r = 0
    maps_b[x][y] = 1

    for i in [[-1,0],[1,0],[0,1],[0,-1]]:
        if(x+i[0] < 5 and x+i[0] > -1):
            if(y+i[1] < 5 and y+i[1] > -1):
                if(maps[x+i[0]][y+i[1]] != -1 and maps_b[x+i[0]][y+i[1]] == 0):
                   r = max(r,sol(x+i[0],y+i[1],left-1))

    maps_b[x][y] = 0
    return r+(maps[x][y]==1)*1
inp = list(map(int,input().split()))
print((sol(inp[0],inp[1],3)>=2)*1)