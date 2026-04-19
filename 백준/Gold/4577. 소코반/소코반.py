import sys
#from collections import deque
ang = {'U':[-1,0],'L':[0,-1],'D':[1,0],'R':[0,1]}
game =0
while 1:
    game +=1
    a,b = map(int,input().split())
    if(a+b == 0):
        break
    else:
        m = []
        mok = []
        for i in range(a):
            m.append(list(sys.stdin.readline().strip()))
            for j in range(b):
                if (m[i][j] == 'w' or m[i][j] == 'W'):
                    plx = j
                    ply = i
                    if(m[i][j] == 'W'):
                        mok.append([i,j])
                    m[i][j] = '.'
                if(m[i][j] == '+'):
                    mok.append([i,j])
                    m[i][j] = '.'
                if(m[i][j] == 'B'):
                    mok.append([i,j])
                    m[i][j] = 'b'
        plm = input()
        for i in range(len(plm)):
            od = plm[i]
            if(m[ply + ang[od][0]][plx + ang[od][1]] == '.'):
                plx += ang[od][1]
                ply += ang[od][0]
            elif(m[ply + ang[od][0]][plx + ang[od][1]] == 'b' and m[ply + ang[od][0]*2][plx + ang[od][1]*2] == '.'):
                m[ply + ang[od][0]][plx + ang[od][1]] = '.'
                plx += ang[od][1]
                ply += ang[od][0]
                m[ply + ang[od][0]][plx + ang[od][1]] = 'b'
            over = 1
            for i in range(len(mok)):
                if(m[mok[i][0]][mok[i][1]] != 'b'):
                    over = 0
            if(over):
                break
        com = 0
        for i in range(len(mok)):
            if(m[mok[i][0]][mok[i][1]] == 'b'):
                m[mok[i][0]][mok[i][1]] = 'B'
            else:
                com = 1
                m[mok[i][0]][mok[i][1]] = '+'
        if(m[ply][plx] == '+'):
            m[ply][plx] = 'W'
        else:
            m[ply][plx] = 'w'
        print('Game '+str(game)+': '+'in'*com+'complete')
        for i in range(a):
            for j in range(b):
                print(m[i][j],end = '')
            print()