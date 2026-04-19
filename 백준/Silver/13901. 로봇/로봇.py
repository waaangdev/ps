a,b = map(int,input().split())
m = [[0 for i in range(b)] for i in range(a)]
c = int(input())
for i in range(c):
    d,e = map(int,input().split())
    m[d][e] = 1
y,x = map(int,input().split())
od = list(map(int,input().split()))
ang = [[-1,0],[1,0],[0,-1],[0,1]]
while 1:
    dix = x
    diy = y
    i = 0
    while i < len(od):
        el = 1
        if(y+ang[od[i]-1][0] > -1 and y+ang[od[i]-1][0] < a and x+ang[od[i]-1][1] > -1 and x+ang[od[i]-1][1] < b):
            if(m[y+ang[od[i]-1][0]][x+ang[od[i]-1][1]] == 0):
                el = 0
                m[y][x] = 1
                y+=ang[od[i]-1][0]
                x+=ang[od[i]-1][1]
        i +=el
    if(x == dix and y ==diy):
        break
print(y,x)