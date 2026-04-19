a = int(input())
od = input()
m = []
pl = [0,0,0]
ang = [[1,0],[0,-1],[-1,0],[0,1]]
ma = [[0 for j in range(a)] for i in range(a)]
ma1 = [[0 for j in range(a)] for i in range(a)]
die = 0

for i in range(a):
    inp = input()
    for j in range(a):
        if (inp[j] == 'S'):
            ma[i][j] = 1
        if (inp[j] == 'Z'):
            m.append([i,j,0])
for i in range(len(od)):
    if(od[i] == 'L'):
        pl[2] -= 1
    elif(od[i] == 'R'):
        pl[2] += 1
    elif(od[i] == 'F' and pl[0]+ang[pl[2]%4][0] < a and pl[0]+ang[pl[2]%4][0] > -1 and pl[1]+ang[pl[2]%4][1] < a and pl[1]+ang[pl[2]%4][1] > -1):
        pl[0] += ang[pl[2]%4][0]
        pl[1] += ang[pl[2]%4][1]
        if(ma[pl[0]][pl[1]] == 1):
            for j in range(-1,2):
                for k in range(-1,2):
                    if(pl[0]+j < a and pl[0]+j > -1 and pl[1]+k < a and pl[1]+k > -1):
                        if(ma[pl[0]+j][pl[1]+k]!= 1):
                            ma[pl[0]+j][pl[1]+k] = 2
    if(ma[pl[0]][pl[1]] == 0):
        if (ma1[pl[0]][pl[1]] == 1):
            die = 1
            break
    for j in range(len(m)):
        ma1[m[j][0]][m[j][1]] = 0
        m[j][0] += ang[m[j][2]%4][0]
        m[j][1] += ang[m[j][2]%4][1]
        if(m[j][0] < 0):
            m[j][0] = 0
            m[j][2] = 0
        elif(m[j][0] > a-1):
            m[j][2] = 2
            m[j][0] = a-1
        ma1[m[j][0]][m[j][1]] = 1
    if(ma[pl[0]][pl[1]] == 0):
        if (ma1[pl[0]][pl[1]] == 1):
            die = 1
            break
if(die == 1):
    print("Aaaaaah!")
else:
    print("Phew...")