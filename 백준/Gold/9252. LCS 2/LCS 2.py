a = input()
b = input()
m = [[0 for i in range(len(b))] for j in range(len(a))]
lcs = 0
lcs2 = ""
for i in range(len(a)):
    for j in range(len(b)):
        if(a[i] == b[j]):
            if(i == 0 or j == 0):
                m[i][j] = 1
            else:
                m[i][j] = m[i-1][j-1]+1
            if(lcs < m[i][j]): 
                lcs = m[i][j] 
        else:
            m[i][j] = max(m[i][j-1],m[i-1][j])
            
lx = len(a)-1
ly = len(b)-1
ll = m[lx][ly]
while 1:
    qwe = 0
    if(lx != 0):
        if(m[lx-1][ly] == ll):
            lx -=1
            qwe = 1
    if(ly != 0 and qwe == 0):
        if(m[lx][ly-1] == ll):
            ly -=1
            qwe = 1
    if(qwe == 0):
        lcs2 = b[ly]+lcs2
        lx -=1
        ly -=1
        ll = m[lx][ly]
    if(lx == -1 or ly == -1 or m[lx][ly] == 0):
        break
print(lcs)
print(lcs2)