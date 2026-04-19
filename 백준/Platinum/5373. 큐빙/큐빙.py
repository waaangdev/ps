"큐빙"

import sys

move = [[[0,0],[0,2],[2,2],[2,0],[0,0]],[[0,1],[1,2],[2,1],[1,0],[0,1]]]
move2 = {'U':0,'D':1,'F':2,'B':3,'L':4,'R':5}
move3 = {'U':[2,4,3,5,2],'D':[3,4,2,5,3],'F':[0,5,1,4,0],'B':[0,4,1,5,0],'L':[1,3,0,2,1],'R':[1,2,0,3,1]}
move4 = {
    'U':[0,0,[0,-1,0],[0,-1,0],[0,-1,0],[0,-1,0]],
    'D':[0,0,[2,-1,0],[2,-1,0],[2,-1,0],[2,-1,0]],
    'F':[[2,-1,0],[0,-1,2],0,0,[-1,2,2],[-1,0,0]],
    'B':[[0,-1,0],[2,-1,2],0,0,[-1,0,2],[-1,2,0]],
    'L':[[-1,0,0],[-1,0,0],[-1,0,0],[-1,2,2],0,0],
    'R':[[-1,2,0],[-1,2,0],[-1,2,0],[-1,0,2],0,0]
    }
move5 = {
    '+':[0,4,1],
    '-':[4,0,-1]
    }


def cube(cmd):

    for j in range(2):
        dum2 = cb[move2[cmd[0]]][move[j][move5[cmd[1]][0]][0]][move[j][move5[cmd[1]][0]][1]]
        for i in range(move5[cmd[1]][0],move5[cmd[1]][1],move5[cmd[1]][2]):
            dum = cb[move2[cmd[0]]][move[j][i+move5[cmd[1]][2]][0]][move[j][i+move5[cmd[1]][2]][1]]
            cb[move2[cmd[0]]][move[j][i+move5[cmd[1]][2]][0]][move[j][i+move5[cmd[1]][2]][1]] = dum2
            dum2 = dum

    for j in range(3):
        dum3 = move4[cmd[0]][move3[cmd[0]][move5[cmd[1]][0]]]
        if(move4[cmd[0]][move3[cmd[0]][0]][0] == -1):
            dum2 = cb[move3[cmd[0]][move5[cmd[1]][0]]][abs(j-dum3[2])][move4[cmd[0]][move3[cmd[0]][move5[cmd[1]][0]]][1]]
        else:
            dum2 = cb[move3[cmd[0]][move5[cmd[1]][0]]][move4[cmd[0]][move3[cmd[0]][move5[cmd[1]][0]]][0]][abs(j-dum3[2])]
        for i in range(move5[cmd[1]][0],move5[cmd[1]][1],move5[cmd[1]][2]):
            dum3 = move4[cmd[0]][move3[cmd[0]][i+move5[cmd[1]][2]]]
            if(dum3[0] == -1):
                dum = cb[move3[cmd[0]][i+move5[cmd[1]][2]]][abs(j-dum3[2])][dum3[1]]
                cb[move3[cmd[0]][i+move5[cmd[1]][2]]][abs(j-dum3[2])][dum3[1]] = dum2
            else:
                dum = cb[move3[cmd[0]][i+move5[cmd[1]][2]]][dum3[0]][abs(j-dum3[2])]
                cb[move3[cmd[0]][i+move5[cmd[1]][2]]][dum3[0]][abs(j-dum3[2])] = dum2
            dum2 = dum

        
                
            
             

case = int(sys.stdin.readline())
for _ in range(case):
    cb = [
        [
        ['w','w','w'],
        ['w','w','w'],
        ['w','w','w']
        ],
        [
        ['y','y','y'],
        ['y','y','y'],
        ['y','y','y']
        ],
        [
        ['r','r','r'],
        ['r','r','r'],
        ['r','r','r']
        ],
        [
        ['o','o','o'],
        ['o','o','o'],
        ['o','o','o']
        ],
        [
        ['g','g','g'],
        ['g','g','g'],
        ['g','g','g']
        ],
        [
        ['b','b','b'],
        ['b','b','b'],
        ['b','b','b']
        ]
    ]
    a = int(sys.stdin.readline())
    li = sys.stdin.readline().split()
    for i in range(a):
        cube(list(li[i]))

    for i in range(3):
        for j in range(3):
            print(cb[0][i][j],end = '')
        print()