import sys
a,b = map(int,input().split())
ang = [[1,-1],[1,0],[1,1],[0,-1],[0,0],[0,1],[-1,-1],[-1,0],[-1,1]]
pl = []
an = []
for i in range(a):
    c = sys.stdin.readline().strip()
    for j in range(b):
        if(c[j] == 'I'):
            pl = [i,j]
        elif(c[j] == 'R'):
            an.append([i,j,0])
od = input()
die = 0
for i in range(len(od)):
    pl[0] += ang[int(od[i])-1][0]
    pl[1] += ang[int(od[i])-1][1]
    m = [[0 for j in range(b)] for i in range(a)]
    for j in range(len(an)):
        if(an[j][2] == 0):
            an[j][0]+=(an[j][0] > pl[0])*-1+(an[j][0] < pl[0])*1
            an[j][1]+=(an[j][1] > pl[1])*-1+(an[j][1] < pl[1])*1
            if(m[an[j][0]][an[j][1]] != 0):
                an[j][2] = 1
                m[an[j][0]][an[j][1]] = 2
            else:
                m[an[j][0]][an[j][1]] = 1
            if(an[j][0] == pl[0] and an[j][1] == pl[1]):
                die = 1
                break
    if(die == 1):
        print('kraj',i+1)
        break
    for j in range(len(an)):
        if(an[j][2] == 0):
            if(m[an[j][0]][an[j][1]] == 2):
                an[j][2] = 1
if(die == 0):
    m = [['.' for j in range(b)] for i in range(a)]
    for j in range(len(an)):
        if(an[j][2] == 0):
            m[an[j][0]][an[j][1]] = 'R'
    m[pl[0]][pl[1]] = 'I'
    for i in range(a):
        for j in range(b):
            print(m[i][j],end = '')
        print()