import sys
#from collections import deque
al = int(input())
ang = [[-1,0],[0,1],[1,0],[0,-1]]#위,오,아,왼

for i in range(al):
    n,m1 = map(int,input().split())
    m = [[0 for j in range(n+1)] for i in range(n+1)]
    for i in range(m1):
        inp = list(map(int,sys.stdin.readline().strip().split()))
        m[inp[0]][inp[1]] = 1
    x,y = map(int,input().split())
    if(y == 0):
        pla = 2
    elif(x == 0):
        pla = 1
    elif(y == n+1):
        pla = 0
    elif(x == n+1):
        pla = 3
    while 1:
        x+=ang[pla%4][1]
        y+=ang[pla%4][0]
        if(x == 0 or x > n or y == 0 or y > n):
            break
        if(m[x][y] == 1):
            pla -=1
    print(x,y)