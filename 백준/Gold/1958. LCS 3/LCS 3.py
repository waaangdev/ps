a = input()
b = input()
c = input()
m = [[[0 for i in range(len(c))] for i in range(len(b))] for j in range(len(a))]
lcs = 0
lcs2 = ""
for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(c)):
            if(a[i] == b[j] == c[k]):
                if(i == 0 or j == 0 or k == 0):
                    m[i][j][k] = 1
                else:
                    m[i][j][k] = m[i-1][j-1][k-1]+1
                if(lcs < m[i][j][k]): 
                    lcs = m[i][j][k] 
            else:
                m[i][j][k] = max(m[i][j-1][k],m[i-1][j][k],m[i][j][k-1])
            
lx = len(a)-1
ly = len(b)-1
lz = len(c)-1
ll = m[lx][ly][lz]
while 1:
    qwe = 0
    if(lx != 0):
        if(m[lx-1][ly][lz] == ll):
            lx -=1
            qwe = 1
    if(ly != 0 and qwe == 0):
        if(m[lx][ly-1][lz] == ll):
            ly -=1
            qwe = 1
    if(lz != 0 and qwe == 0):
        if(m[lx][ly][lz-1] == ll):
            lz -=1
            qwe = 1
    if(qwe == 0):
        lcs2 = b[ly]+lcs2
        lx -=1
        ly -=1
        lz -=1
        ll = m[lx][ly][lz]
    if(lx == -1 or ly == -1 or lz == -1 or m[lx][ly][lz] == 0):
        break
print(lcs)