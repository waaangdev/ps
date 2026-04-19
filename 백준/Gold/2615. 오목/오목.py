#미완

m = []

for i in range(19):
    m.append(list(map(int,input().split())))
    
x = 5
p = [1,2]
end = 0
end1 = [0,0]

for i in range(len(m)):
    for j in range(len(m[i])):
        for k in p:
            if (j+(x) <= len(m[i])):
                qwe = 0
                qwe1 = 0
                for a in range(x+5):
                    if(j+a >= len(m[i])):
                        break
                    if (m[i][j+a] != k and m[i][j+a] != k*10):
                        break
                    if (m[i][j+a] == k*10):
                        qwe1+=1
                    qwe+=1
                if(qwe1 == qwe):
                    qwe = 0
                if (qwe == x):
                    end = k
                    end1 = [i,j]
                if (qwe > x):
                    for a in range(qwe):
                        m[i][j+a] = k*10
            if (i+(x) <= len(m)):
                qwe = 0
                qwe1 = 0
                for a in range(x+5):
                    if(i+a >= len(m[i])):
                        break
                    if (m[i+a][j] != k and m[i+a][j] != k*10):
                        break
                    if (m[i+a][j] == k*10):
                        qwe1+=1
                    qwe+=1
                if(qwe1 == qwe):
                    qwe = 0
                if (qwe == x):
                    end = k
                    end1 = [i,j]
                if (qwe > x):
                    for a in range(qwe):
                        m[i+a][j] = k*10
            if (i <= len(m)-(x) and j <= len(m)-(x)):
                qwe = 0
                qwe1 = 0
                for a in range(x+5):
                    if(j+a >= len(m[i]) or i+a >= len(m[i])):
                        break
                    if (m[i+a][j+a] != k and m[i+a][j+a] != k*10):
                        break
                    if (m[i+a][j+a] == k*10):
                        qwe1+=1
                    qwe+=1
                if(qwe1 == qwe):
                    qwe = 0
                if (qwe == x):
                    end = k
                    end1 = [i,j]
                if (qwe > x):
                    for a in range(qwe):
                        m[i+a][j+a] = k*10
            if (i <= len(m)-(x) and j >= (x)-1):
                qwe = 0
                qwe1 = 0
                for a in range(x+5):
                    if(j-a < 0 or i+a >= len(m)):
                        break
                    if (m[i+a][j-a] != k and m[i+a][j-a] != k*10):
                        break
                    if (m[i+a][j-a] == k*10):
                        qwe1+=1
                    qwe+=1
                if(qwe1 == qwe):
                    qwe = 0
                if (qwe == x):
                    end = k
                    end1 = [i+x-1,j-x+1]
                if (qwe > x):
                    for a in range(qwe):
                        m[i+a][j-a] = k*10
            if(end != 0): break
        if(end != 0): break
    if(end != 0): break
print(end)
if(end != 0): print(end1[0]+1,end1[1]+1)
