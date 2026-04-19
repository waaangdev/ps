a,b = map(int,input().split())
n,m = map(int,input().split())
pl = [[] for i in range(n)]
ba = {'E':0,'S':1,'W':2,'N':3}
break1 = 0
for i in range(n):
    pl[i] = (list(input().split()))
    pl[i][0] = int(pl[i][0])-1
    pl[i][1] = b - (int(pl[i][1])-1) -1
    pl[i][2] = ba[pl[i][2]]
for i in range(m):
    e = list(input().split())
    for j in range(int(e[2])):
        if(e[1] == 'F'):
            pl[int(e[0])-1][int(pl[int(e[0])-1][2]%2)] -= int(pl[int(e[0])-1][2]/2)*2-1
        if(e[1] == 'L'):
            pl[int(e[0])-1][2] -= 1
            if(pl[int(e[0])-1][2] == -1):
                pl[int(e[0])-1][2] = 3
        if(e[1] == 'R'):
            pl[int(e[0])-1][2] += 1
            if(pl[int(e[0])-1][2] == 4):
                pl[int(e[0])-1][2] = 0
        if(pl[int(e[0])-1][0] < 0 or pl[int(e[0])-1][0] == a or pl[int(e[0])-1][1] < 0 or pl[int(e[0])-1][1] == b):
            print("Robot",e[0],"crashes into the wall")
            break1 = 1
            break
        for k in range(len(pl)):
            if(pl[k][0:2] == pl[int(e[0])-1][0:2] and k != int(e[0])-1):
                print("Robot",e[0],"crashes into robot",k+1)
                break1 = 1
                break
            
        if(break1 == 1):
            break
    if(break1 == 1):
        break
if(break1 == 0):
    print("OK")