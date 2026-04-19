a = int(input())
m = []
for i in range(a):
    m.append(list(map(int,input().split())))
if(a == 1):
    r = 0
    for j in range(len(m[len(m)-1])):
        r = max(r,m[len(m)-1][j])
    r1 = 100000000
    for j in range(len(m[len(m)-1])):
        r1 = min(r1,m[len(m)-1][j])
else:
    m1 = [m[0][:],[0,0,0]]
    for i in range(1,a):
        for j in range(len(m[i])):
            if(j == 0):
                m1[1][j] = m[i][j] + max(m1[0][j],m1[0][j+1])
            if(j == 1):
                m1[1][j] = m[i][j] + max(max(m1[0][j],m1[0][j+1]),m1[0][j-1])
            if(j == 2):
                m1[1][j] = m[i][j] + max(m1[0][j],m1[0][j-1])
        m1[0] = m1[1][:]
    
    r = 0
    for j in range(len(m1[len(m1)-1])):
        r = max(r,m1[len(m1)-1][j])
    
    m1 = [m[0][:],[0,0,0]]
    for i in range(1,a):
        for j in range(len(m[i])):
            if(j == 0):
                m1[1][j] = m[i][j] + min(m1[0][j],m1[0][j+1])
            if(j == 1):
                m1[1][j] = m[i][j] + min(min(m1[0][j],m1[0][j+1]),m1[0][j-1])
            if(j == 2):
                m1[1][j] = m[i][j] + min(m1[0][j],m1[0][j-1])
        m1[0] = m1[1][:]
    
    r1 = 100000000
    for j in range(len(m1[len(m1)-1])):
        r1 = min(r1,m1[len(m1)-1][j])

print(r,r1)