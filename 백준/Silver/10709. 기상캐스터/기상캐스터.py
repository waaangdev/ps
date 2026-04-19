a,b = map(int,input().split())
m = []
m1 = {'c':1,'.':0}
for i in range(a):
    m.append([m1[i] for i in input()])
s = [[-1 for j in range(b)] for i in range(a)]
t= 0
while 1:
    br = 0
    for i in range(a):
        for j in range(b):
            if(m[i][j] == 1):
                s[i][j] = min(s[i][j],t)
                if(s[i][j] == -1):s[i][j]  = t
                br = 1
        m[i].pop()
        m[i].insert(0, 0)
    if(br == 0):
        break
    t+=1
for i in range(a):
    print(*s[i])