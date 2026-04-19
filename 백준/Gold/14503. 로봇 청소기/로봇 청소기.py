a,b = map(int,input().split())
pl = list(map(int,input().split()))
ang = [[-1,0],[0,1],[1,0],[0,-1]]
m = []
for i in range(a):
    m.append(list(map(int,input().split())))
s = 0
while 1:
    if(m[pl[0]][pl[1]] == 0):
        m[pl[0]][pl[1]] = 2
        s +=1
    al = 0
    for i in range(4):
        if(m[pl[0]+ang[i][0]][pl[1]+ang[i][1]] == 0):
            al = 1
    if(al == 0):
        if(m[pl[0]+ang[(pl[2]-2)%4][0]][pl[1]+ang[(pl[2]-2)%4][1]] == 1):
            break
        else:
            pl[0]+= ang[(pl[2]+2)%4][0]
            pl[1]+= ang[(pl[2]+2)%4][1]
    else:
        pl[2] -=1
        if(m[pl[0]+ang[pl[2]%4][0]][pl[1]+ang[pl[2]%4][1]] == 0):
            pl[0]+= ang[(pl[2])%4][0]
            pl[1]+= ang[(pl[2])%4][1]

print(s)